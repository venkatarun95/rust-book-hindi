# Introduction

> Note: This edition of the book is the same as [The Rust Programming
> Language][nsprust] available in print and ebook format from [No Starch
> Press][nsp].

[nsprust]: https://nostarch.com/rust
[nsp]: https://nostarch.com/

> लैंग्वेज

आप्का *रस्ट प्रोग्रामिंग भाषा (Rust Programming Language)* में स्वागत है। यह
रस्ट के बारे मे एक परिच्यात्मक किताब है। रस्ट प्रोग्रामिंग लैंग्वेज आप्को ज्यादा
तेज चल्ने वालि, और ज्यादा भरोसेमंद संफ्टवेयर लिख्ने में मदद कर्ता है। अक्सर
प्रोग्रामिंग भाषाओं मे लिख्ने की सुविधा और निम्न-स्तर (low-level) पर नियन्त्रण करने मे
संघर्ष होता है। रस्ट इस संघर्ष को चुनौती देता है। रस्ट आप्को मेमोरी (memory/RAM)
के उप्योग का नियन्त्रण जैसे निम्न स्तर के कर्य भी करने देता है, लेकिन बिना उस्से
जुङे हुए पारंपरिक परेसानियों के।

## रस्ट किस के लिये है?

खूब सारे लोगों के लिये। कुछ उदाहरण देखते है।

<!-- ## Who Rust Is For

Rust is ideal for many people for a variety of reasons. Let’s look at a few of
the most important groups. -->

### प्रोग्रामर के दलों के लिये

यह स्थापित हो रहा है की रस्ट प्रोग्रामर के बङे दलों के लिये, जिन्मे निम्न-स्तर
पे कोङ (code) लिखे की कौशल्ता के कइ स्तर हों, उनके लिये बहुत अच्छा साधन है।
निम्न-स्तर पर लिखे गए कोङ, कई प्रकार के जटिल गलतियों (जिन्हें प्रोग्रामिंग मे
"बग" कहते है) के लिये लिए प्रवण हैं। इन्हें अनुभवित प्रोग्रामरों के द्वारा
लंबा-चौङा जांन्च करके ही पकङा जा सक्ता है। लेकिन रस्ट में कम्पाइलर (compiler) ही
ऐसे कइ गलतियां पकद लेता है, और कोङ को कम्पाइल ही नही कर्ता। इस तरह प्रोग्रामर के
दल अपना समय, प्रोग्राम के तर्क मे ज्यादा और गलतियां खोजने में कम, बिता सकतीं
हैं।

रस्ट कै आधुनिक साधन सिस्टम प्रोग्रामिंग (systems programming) के दुनिया में लाता है।

* Cargo, एक ऐसा साधन है, जो आप्के प्रोग्राम के ङिपेंङेंसीयों को जोङने और चम्पाइल
 करने में मदद करता है।

* Rustfmt सभी प्रोग्रामरों के बीच एक सुसंगत कोङ करने का अंदाज का सुनिश्चित कर्ता है।

* Rust Language Server उप्लब्ध है, जो Integrated Development Environment (IDE)
के लक्षण पुरा करता है, जैसे कोङ लिख्ते हुए उस्को ऑटोमैटिक पुरा कर्ना (code
completion), और गलतियों को लिख्ते हुए ही दिखाना।

इन सधनों को उप्योग कर, प्रोग्रामर तेजी से कोङ लिख सक्ते है।

<!-- ### Teams of Developers

Rust is proving to be a productive tool for collaborating among large teams of
developers with varying levels of systems programming knowledge. Low-level code
is prone to a variety of subtle bugs, which in most other languages can be
caught only through extensive testing and careful code review by experienced
developers. In Rust, the compiler plays a gatekeeper role by refusing to
compile code with these elusive bugs, including concurrency bugs. By working
alongside the compiler, the team can spend their time focusing on the program’s
logic rather than chasing down bugs.

Rust also brings contemporary developer tools to the systems programming world:

* Cargo, the included dependency manager and build tool, makes adding,
  compiling, and managing dependencies painless and consistent across the Rust
  ecosystem.
* Rustfmt ensures a consistent coding style across developers.
* The Rust Language Server powers Integrated Development Environment (IDE)
  integration for code completion and inline error messages.

By using these and other tools in the Rust ecosystem, developers can be
productive while writing systems-level code. -->

### छात्र

रस्ट छत्रों और ऐसे जनों के लिये है, जो कम्प्युटर सिस्टम के बारे मे सिख्ना चाहते
हैं। उदाहरण के लिये, रस्ट के सहरे लोगों ने आपरेटिंग सिस्टम (operating system) को
बनाने की प्रक्रिया के बारे मे सिखा है। रस्ट प्रोग्रामरों की समज नए छात्र और रस्ट
पहली बार सिख्ने वाले लोगों को स्वागत कर्ता है, और मदद करने के लिये खुश है। इस
किताब की तर्हं कइ मध्यों के ज़रिये, रस्ट समज कोशिश कर रहा है, कि सिस्टम
प्रोग्रामिंग के अवधारण, अधिक से अधिक् लोगों तक पहुंचे, खास तौर पर वह जन, जो पहली
बार प्रोग्राम करना सीख रहे हैं।

<!-- ### Students

Rust is for students and those who are interested in learning about systems
concepts. Using Rust, many people have learned about topics like operating
systems development. The community is very welcoming and happy to answer
student questions. Through efforts such as this book, the Rust teams want to
make systems concepts more accessible to more people, especially those new to
programming. -->

### कम्पनियां

कई सौ कम्पनियां, बङी और छोटि, रस्ट को उत्पदन मे प्रोयोग कर्तिं हैं. "फ़ायरफ़ॉक्स
ब्राउज़र" जैसी कई उत्पादनों मे रस्ट का प्रयोग है।

<!-- ### Companies

Hundreds of companies, large and small, use Rust in production for a variety of
tasks. Those tasks include command line tools, web services, DevOps tooling,
embedded devices, audio and video analysis and transcoding, cryptocurrencies,
bioinformatics, search engines, Internet of Things applications, machine
learning, and even major parts of the Firefox web browser. -->

### खुला स्त्रोत

रस्ट उन जनों के लिये खास तौर पर है, जो रस्ट भाषा, समज, रस्ट प्रोग्रामर के साधन,
और "लाइब्रेरी" (libraries) बनाने मे मदद कर्ना चाहते हैं। हमे बहुत खुशी होगी अगर
आप रस्ट भाषा मे किसी भी तौर पर योग्दान करना चाहें।

<!-- ### Open Source Developers

Rust is for people who want to build the Rust programming language, community,
developer tools, and libraries. We’d love to have you contribute to the Rust
language. -->

### जो जन रफ़्तार और स्थिरता पसंद करते हैं

रस्ट उन जनों के लिये है जो रफ्तार और स्थिरता पसंद करते हैं। रफ्तार से हमारा
मत्लब है, आप्के रस्ट प्रोग्राम के चल्ने का रफ्तार और आप जिस्त रफ्तार से रस्ट का
प्रोग्राम लिख पाते हैं। रस्ट कम्पाईलर सुनिश्चित करता है की जब आप अप्ने प्रोग्राम
में अधिक सुविधा दालें, या अप्ने कोङ आयोजन सिद्धांत बदलें, तब भि आप्के प्रोग्राम
क स्थिर्ता बना रहे। इस्के विपरीत, और भषओं मे, प्रोग्रामर कोङ बदल्ने से दरते हैं,
की कहिं प्रोग्राम "टूट" न जाए। रस्ट शुन्य-लागत मे सुविधैं देत है, जिस्से आप आसनी
से कोङ लिख पयें, जो उस्के बावजूद तेज़ चल्ने वालि प्रोग्राम मे कम्पाईल हो सके। वह
उसि रफ्तार से चल सकता है, जैसे की आपने बिना रस्ट के सुविधाओं को प्रयोग करे खुद
कोङ लिखा हो।

रस्ट और कई जनों को भी उपयोग आने की कामना करता है। उपर्युक्त जिन उपयोगकर्ताओं की
चर्चा की गइ है, वो सिर्फ़ प्रमुख हितधारक हैं। रस्ट के साथ हमारा यह आशा है, की जो
सुविधा और रफ्तार मेइं अदला-बदली इतने दिनों से प्रोग्रामर स्वीकार करते आयें है,
वो आगे से करना न पङे। क्रिपया रस्ट का इस्तेमाल करें और देखें की वह आपके जरूरतों
को पूरा कर्ता है, की नही।

<!-- ### People Who Value Speed and Stability

Rust is for people who crave speed and stability in a language. By speed, we
mean the speed of the programs that you can create with Rust and the speed at
which Rust lets you write them. The Rust compiler’s checks ensure stability
through feature additions and refactoring. This is in contrast to the brittle
legacy code in languages without these checks, which developers are often
afraid to modify. By striving for zero-cost abstractions, higher-level features
that compile to lower-level code as fast as code written manually, Rust
endeavors to make safe code be fast code as well.

The Rust language hopes to support many other users as well; those mentioned
here are merely some of the biggest stakeholders. Overall, Rust’s greatest
ambition is to eliminate the trade-offs that programmers have accepted for
decades by providing safety *and* productivity, speed *and* ergonomics. Give
Rust a try and see if its choices work for you. -->

## यह किताब किस के लिये है?

यह किताब मानता है की आपने किसी और प्रोग्रामिंग भाषा का पहले प्रयोग किया है, चाहे
वो कोई भी भाषा हो। हमरी कोशिश रही है की यह किताब कोइ भी व्यक्ति जिस्ने पहले
प्रोग्राम करी है, वो समझ सके। हम इस बात पर ज्यादा गौर नही करते की प्रोग्रामिंग
क्या है, य उस्के बारे में कैसे सोचना चाहिये। अगर पहले आपने कभी प्रोग्रामिंग नही
करी है, तो आपको किसी ऐसी किताब पढने से फ़ायदा होगा जो प्रोग्रामिन्ग का एक सरल
परिचय दे।

<!-- ## Who This Book Is For

This book assumes that you’ve written code in another programming language but
doesn’t make any assumptions about which one. We’ve tried to make the material
broadly accessible to those from a wide variety of programming backgrounds. We
don’t spend a lot of time talking about what programming *is* or how to think
about it. If you’re entirely new to programming, you would be better served by
reading a book that specifically provides an introduction to programming. -->

## किताब का उपयोग

सामन्य तौर पर हम मानते हैं की आप यह किताब शुरुआत से लेकर अन्त तक पढ रहे हैं। आगे
के अध्याय पहले चर्चा किये गये विचारों पर निर्माण कर्ते नैं, और पहले वाले अध्याय
किसी विषय पर पूरी विवरण हमेशा नही करते; अक्सर हम पुराने विचारों का आगे अध्याय मे
विवरण करते हैं।

इस किताब में आप दो तरह के अध्याय पयेंगे: विछारों पर चर्चा करने वाले और रस्ट के
साथ कुछ बनाना सिखाने वले। पहली तरह के अध्याय मे आप रस्ट की किसी हिस्से के बारे
मे सीखेंगे। दूसरी तरह के अध्याय मे आप इन हिस्सों को लेकर कुछ बनान सीखेंगे। इस
किताब में अध्याय २, १२ और २० दूसरी तरह के हैं।

अध्याय १ मे हम सीखेंगे की रस्ट को अपने कम्प्यूटर में "इंस्टांल" करना, एक सरल
बहुत ही प्रोग्राम लिख्ना, और `cargo` साधन का उपयोग करना। अगर आपको रस्ट मे तुरंत
ही प्रोग्राम लिख्ना है, तो क्रिपया अध्याय २ पधे। लेकिन हो सक्ता है की आप सिधा ही
अध्याय ३ पधना चाहें, जो रुस्ट के वह हिस्से प्रकट कर्ता है जो और प्रोग्रामिंग
भाशाओं मे भी मौजूत हैं, जिस्के बाद आप अध्याय ४ पध सकते हैं, जो रस्ट के "ओनरशिप"
प्रणाली का परिचय देता है। यदी आप ऐसे छात्र हैं, जो कुछ करने से पहले सब कुछ
विस्तार से जन्ना चहते हैं, तो आप अध्याय २ को पहले छोङ कर, बादमे भी आ सकते हैं।

<!-- ## How to Use This Book

In general, this book assumes that you’re reading it in sequence from front to
back. Later chapters build on concepts in earlier chapters, and earlier
chapters might not delve into details on a topic; we typically revisit the
topic in a later chapter.

You’ll find two kinds of chapters in this book: concept chapters and project
chapters. In concept chapters, you’ll learn about an aspect of Rust. In project
chapters, we’ll build small programs together, applying what you’ve learned so
far. Chapters 2, 12, and 20 are project chapters; the rest are concept chapters.

Chapter 1 explains how to install Rust, how to write a Hello, world! program,
and how to use Cargo, Rust’s package manager and build tool. Chapter 2 is a
hands-on introduction to the Rust language. Here we cover concepts at a high
level, and later chapters will provide additional detail. If you want to get
your hands dirty right away, Chapter 2 is the place for that. At first, you
might even want to skip Chapter 3, which covers Rust features similar to those
of other programming languages, and head straight to Chapter 4 to learn about
Rust’s ownership system. However, if you’re a particularly meticulous learner
who prefers to learn every detail before moving on to the next, you might want
to skip Chapter 2 and go straight to Chapter 3, returning to Chapter 2 when
you’d like to work on a project applying the details you’ve learned. -->

अध्याय ५ `struct` और 'method' की चर्चा कर्ता है, वुर अध्याय ६ `enum`, `match` और
`if let` की। आप `struct` और `enum` के जरिये रस्ट मे अपने खुद के "टायिप" (type)
बनायेंगे।

अध्याय ७ मे, आप सीखेंगे की रस्ट की कोङ का आयोजन मौद्यूल (module) के जर्रीये कैसे
कर सकते हैं, और किस तर्ह से उस कोङ की सुविधायें (API - Application Programming
Interface) बाहर की दुनिया के लिये प्रकाश मे ला सकते हैं। अध्याय ८ कुच सामन्य
'ङेटा-स्त्रक्चर (datastructure) की चर्चा कर्ता है, जो रस्ट की "स्टैंङर्ङ
लाइब्ररी" (स्तन्दर्द library) मे उप्लब्ध है, जैसे की "वेच्टर" (vector),
"स्त्रिन्ग" (string) और "हैश-मैप" (हश-map). इन्का अर्थ हम उसी अध्याय मे
सम्झेंगे। अध्याय ९ में रस्ट हम देखेंगे की रस्ट मे गलतियों को संभालने के कुछ तरीके सिखेंगे।

अध्यायन १० मे 'generic', 'trait' और 'lifetime' की चर्चा है, जिन्का इस्तेमाल आप
कर सक्ते हैं, ऐसे कोङ लिखने के लिये, जो उन्य "टायिप" (type) पर काम कर सके।
अह्द्याय ११ मे कोङ के जांच क चर्चा है, जो रस्ट मे लिखे गये कोङ के बावजूत ज़रोओरी
है। अध्याय १२ मे हम `grep` नामक एक साधन का एक छोता रूप बनाएंगे जो फ़ैलों मे
"टेक्स्ट" ढुंङने मे काम आता है। इसके लिये हम पुराने अध्यायनों मे से कै सीखों का उप्योग करेंगे।

<!-- Chapter 5 discusses structs and methods, and Chapter 6 covers enums, `match`
expressions, and the `if let` control flow construct. You’ll use structs and
enums to make custom types in Rust.

In Chapter 7, you’ll learn about Rust’s module system and about privacy rules
for organizing your code and its public Application Programming Interface
(API). Chapter 8 discusses some common collection data structures that the
standard library provides, such as vectors, strings, and hash maps. Chapter 9
explores Rust’s error-handling philosophy and techniques.

Chapter 10 digs into generics, traits, and lifetimes, which give you the power
to define code that applies to multiple types. Chapter 11 is all about testing,
which even with Rust’s safety guarantees is necessary to ensure your program’s
logic is correct. In Chapter 12, we’ll build our own implementation of a subset
of functionality from the `grep` command line tool that searches for text
within files. For this, we’ll use many of the concepts we discussed in the
previous chapters. -->

अध्याय १३ मे "च्लोज़र" (closure) और "इटरैटर" (iterator) की चर्चा है: रस्ट के वो
अंक जो "फ़ंच्शनल प्रोग्रामिंग" (functional programming) से आते हैं। अध्यायन १४
मे हम `cargo` को थोङा और गौर से देखेंगे, और अपने कोङ को और लोगों के साथ बांटने
के अच्छे तरिके देखेंगे। अह्द्यायन १५ "स्मर्ट पाइंटर" (smart pointer) की चर्चा
कर्ता है, जो रस्ट के "स्तैंङर्ङ लाइब्ररी" (standard library) मे उप्लब्ध है।

अध्यायन १६ मे हम "कंकरंट प्रोग्रामिंग" की बात करेंगे। "कंकरंट प्रोग्रामिंग"
मत्लब ऐसा कोङ लिखना जो की एक ही समय मे अनेक काम करे। सामन्य रूप से, ऐसा कोङ
लिखना कठिन है, क्युंकि गलतियां आसानी से हो जाती है। लेकिन रस्ट कई सुविधयें
उप्लब्ध कर्ता है, जो आप्को बिना ङर के ऐसा कोङ लिखने मे काबिल करे। अध्यायन १७
रस्ट और  "ऑब्जेक्ट ओरिएंटेड प्रोग्रामिंग" (object oriented programming) के बीच
समानता बताता है, जिस्से शायद आप परिचित होंगे।

अध्यायन १८ मे "पैटर्न" (pattern) और "पैटर्न मैट्चिंग" (pattern matching) चर्चा
है, जो अप्ने विचारों को रस्ट मे प्रखट करने के शक्तिशाली तरीके हैं। अध्यायन १९ मे
हम कै उच्च स्तर वले बतें करेंगे, जैसे की `unsafe` रस्ट और  `lifetime`, `trait`,
"टायीप" आदि।

अध्यायन २० मे हम निम्न-स्तर पर लिख्कर एक पुर्ण "वेब सर्वर" प्रोग्राम बनयेंगे जो
"मल्टी-थ्रेदिद" (multi-threaded) हो, और एक ही समय पर अनेक काम कर पाय।

अंत मे, अप्पेंदिक्स/परिशिष्ट मे हमने रस्ट के बारे मे जान्कारी एक शब्दकोश की तरह दिया है।

इस किताब को पढने का कोइ गलत तरीका नही है: अगर आप सिधा ही आगे की अध्यायन पढना
चाहते हैं, तो ज़रूर कीजिये! हो सकता है की आप्को फिर पीछे आना पङे अगर कोइ चॆज़
समझ मे न आये तो। पर आप वही करिये जो आप के लिये सही हो।

रस्ट सीखने का एक मुख्य अंक है रस्ट कंपाइलर के "एरर संदेश" पढना, जहां वो कोङ मे
रखे गलतियां स्पष्ट कर्ता है। यह संदेश आपको कोङ लिख्ने मे मदद करेंगी। इस लिये, हम
कई जगह गलत कोङ के ऐसे उदाहरण देंगे, जहं कंपाइलर एरर संदेश बतायेगा। इस वजह से याद
रखियेगा की इस किताब मे हर कोङ का उदाहरण कंपाइल नही होग। इन उदाहरणों मे हम आप्को
यह भी बतयेंगे की कंपाइलर के सन्देश पधकर सही कोङ कैसे लिखते हैं।

<!-- Chapter 13 explores closures and iterators: features of Rust that come from
functional programming languages. In Chapter 14, we’ll examine Cargo in more
depth and talk about best practices for sharing your libraries with others.
Chapter 15 discusses smart pointers that the standard library provides and the
traits that enable their functionality.

In Chapter 16, we’ll walk through different models of concurrent programming
and talk about how Rust helps you to program in multiple threads fearlessly.
Chapter 17 looks at how Rust idioms compare to object-oriented programming
principles you might be familiar with.

Chapter 18 is a reference on patterns and pattern matching, which are powerful
ways of expressing ideas throughout Rust programs. Chapter 19 contains a
smorgasbord of advanced topics of interest, including unsafe Rust and more
about lifetimes, traits, types, functions, and closures.

In Chapter 20, we’ll complete a project in which we’ll implement a low-level
multithreaded web server!

Finally, some appendixes contain useful information about the language in a
more reference-like format. Appendix A covers Rust’s keywords, Appendix B
covers Rust’s operators and symbols, Appendix C covers derivable traits
provided by the standard library, and Appendix D covers macros.

There is no wrong way to read this book: if you want to skip ahead, go for it!
You might have to jump back to earlier chapters if you experience any
confusion. But do whatever works for you.

An important part of the process of learning Rust is learning how to read the
error messages the compiler displays: these will guide you toward working code.
As such, we’ll provide many examples of code that doesn’t compile along with
the error message the compiler will show you in each situation. Know that if
you enter and run a random example, it may not compile! Make sure you read the
surrounding text to see whether the example you’re trying to run is meant to
error. In most situations, we’ll lead you to the correct version of any code
that doesn’t compile. -->

## किताब के फ़ाइल

जिन "फ़ाइलों" (files) से हमने यह किताब लिखा है, वह आप निम्न लिंक पर पा सकते हैं।
[GitHub][book].

[book]: https://github.com/rust-lang/book/tree/master/second-edition/src

<!-- ## Source Code

The source files from which this book is generated can be found on
[GitHub][book].

[book]: https://github.com/rust-lang/book/tree/master/second-edition/src -->
