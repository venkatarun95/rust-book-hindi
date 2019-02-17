from bs4 import BeautifulSoup
import markdown

import pickle
import re
import sys

#import nltk

def read_glossary(filename="glossary.csv"):
    '''Return dictionary of english words -> hindi words'''
    file = open(filename, 'r')
    glossary = {}
    for line in file.readlines():
        if line.startswith('#'):
            # Ignore comment
            continue
        eng, hin, _type, _descr = line.split(',')
        glossary[eng.strip()] = hin.strip()
    return glossary

def replace_with_placeholder(text, reg, holder_id, name):
    '''Replace all instances of the given regex with placeholders. @name gives
    the name of the placeholder.'''

    out = ""
    md = {}
    prev_start = 0
    for match in reg.finditer(text):
        out += text[prev_start:match.span()[0]] + ("_HOLDER_%d" % holder_id)
        prev_start = match.span()[1]
        md[holder_id] = (name, match.group())
        holder_id += 1
    out += text[prev_start:]
    return (out, md, holder_id)


def strip_markdown(input_text, holder_id = 0):
    '''Process markdown text, returning simpler text with placeholders and some
    metadata. The simple text, after machine translation, can be combined with
    the placeholders to produce final text.

    holder_id is used internally. It is the placeholder id, and is incremented
    each time'''

    out = ""
    md = {}

    # Some regular expressions
    re_head = re.compile('(#+ )(.*)')
    re_comment = re.compile('(<!--.*-->)')

    # Whether or not we are currently processing a code-block
    code_block_mode = None

    for line in input_text.split('\n'):
        if code_block_mode != None:
            if line.startswith('```'):
                # Code block finished. Add placeholder
                # Add placeholder
                out += "_HOLDER_%d\n\n" % holder_id
                code_block_mode += line + '\n'
                md[holder_id] = ("CodeBlock", code_block_mode)
                holder_id += 1
                code_block_mode = None
            else:
                code_block_mode += line + '\n'
            continue

        if line.startswith('```'):
            assert(code_block_mode == None)
            code_block_mode = line + '\n'
            continue
        elif line.startswith('#'):
            # Add placeholder
            head, text = re_head.match(line).groups()
            out += "_HOLDER_%d\n\n" % holder_id
            md[holder_id] = ("Head", head)
            holder_id += 1

            # Parse recursively
            o, m, holder_id = strip_markdown(text, holder_id)
            out += o
            md.update(m)
            continue

        out += line + '\n'

    # Replace all single-quoted pieces of code
    re_single_code = re.compile('(\`[^`]+\`)')
    out, new_md, holder_id = replace_with_placeholder(out, re_single_code, holder_id, 'Code')
    md.update(new_md)

    # Replace all spans
    re_span = re.compile('(\<span.+\</span\>)')
    out, new_md, holder_id = replace_with_placeholder(out, re_span, holder_id, 'Span')
    md.update(new_md)

    return (out, md, holder_id)

def replacement_word(word):
    return '_%s_' % (word.replace(' ', '_').upper())

def replace_words(text, glossary):
    # The most horrible, inefficient way to do this. But computers are fast!

    for en_word in glossary:
        new_out = ""
        md = {}
        prev_start = 0
        for match in re.compile('\W(%ss?)\W' % en_word).finditer(text.lower()):
            new_out += text[prev_start:match.span()[0] + 1] \
            + replacement_word(match.groups()[0])
            prev_start = match.span()[1] - 1
        new_out += text[prev_start:]
        text = new_out

    # Replace all single newlines with a space
    text = re.sub(r'([^\n])\n([^\n])', r'\1 \2', text)

    return text

def decode(text, glossary, md):
    re_special = re.compile('\W(_[A-Z0-9_]+_[0-9]*)\W')
    out = ""
    prev_start = 0
    for match in re_special.finditer(text):
        #print(match, match.groups())
        word = match.groups()[0]

        # Append the string so far
        out += text[prev_start:match.span()[0] + 1]
        prev_start = match.span()[1] - 1

        if word.startswith('_HOLDER_'):
            holder_id = int(word.split('_')[-1])
            if holder_id in md:
                cmd = md[holder_id][0]
                if cmd != 'Head':
                    out += md[holder_id][1]
                else:
                    out += word
        else:
            unproc_word = word.lower().replace('_', ' ').strip()
            if unproc_word in glossary:
                out += glossary[unproc_word]
            elif unproc_word[-1] == 's' and unproc_word[:-1] in glossary:
                out += glossary[unproc_word[:-1]]
            else:
                # We don't know what this is. So let it be
                out += word
    return out

if sys.argv[1] == 'enc':
    in_file = open(sys.argv[2], 'r')

    simple_text, md, holder_id = strip_markdown(in_file.read())
    pickle.dump(md, open('metadata.pkl', 'wb'))

    glossary = read_glossary()

    final = replace_words(simple_text, glossary)
    print(final)
elif sys.argv[1] == 'dec':
    in_file = open(sys.argv[2], 'r')
    md = pickle.load(open('metadata.pkl', 'rb'))

    glossary = read_glossary()

    decoded = decode(in_file.read(), glossary, md)
    print(decoded)
