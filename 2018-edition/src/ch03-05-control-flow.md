## कोड के बहाव पर नियंत्रण

ज्यादातर परोगरामिंग भा‍षा मे दो महत्वपूरण भाग होते हैं: एक, किसी "कंडि‍षन" (condition) या शरथ के आधार पर यह तै करना कि कोड को किसी हिस्से चलाना है कि नही। दो, किसी कोड के हिस्से को बार-बार चलाना जब तक कि कोइ कंडिषन सच रहे। रस्ट मे यह नियंत्रन आम तौर पर `if` एक्सप्रेशन और loop के द्वारा होता है।

### `if` एक्सप्रेशन

`if` एक्सप्रेशन आपको अपको यह कहने देता है कि, "अगर ये कंडिषन सच हुआ तो कोड के इस भाग को चलाओ, वरना इस दूसरे भाग को"

`if` एक्सप्रेशन को देखने के लिए, अपने *projects* फ़ोलडर मे *branches* नाम से एक नया प्राजेक्ट बनाओ। उसके *src/main.rs* फ़ाईल मे, यह लिखो:

<span class="filename">Filename: src/main.rs</span>

```rust
fn main() {
    let number = 3;

    if number < 5 {
        println!("condition was true");
    } else {
        println!("condition was false");
    }
}
```

<!-- NEXT PARAGRAPH WRAPPED WEIRD INTENTIONALLY SEE #199 -->

सारे `if` एक्सप्रेशन `if` शब्द से आरंभ होते हैं, और उसके आगे एक कंडिषन लिखा जाता है। ऊपर के कोड मे कंडिषन यह
देखता है कि `number` मे जानकारी `5` है कि नही। कंडिषण के तुरंत बाद, हम उस कोढ बलांक को लिखते हैं जो चाहते हैं कि कंडिषण के सच होने पर चले। `if` एक्सप्रेशन से संबंधित कोड बलांक को हम कभी कभी *हाथ* (arm) भी बोलते हैं, ठीक उसी तरह जैसे हमने `match` एक्सप्रेशन मे देखा था अधयाय 2 मे।

हम चाहें तो, `if` के साथ `else` एक्सप्रेशन भी जोड सकते हैं। इसका उपयोग हम ऊपर करते हैं एक कोड बलांक लीखने के लिये जो तब चलेगा, जब कंडीशन सच ना हो। अगर `else` नही लिखा गया हो, और कंडिषन गलत है, तो प्रोग्राम `if` बलांक को छोडकर आगे बढ जाएगा।

आप यह कोड चलाएंगे तो यह देखेंगे।

```text
$ cargo run
   Compiling branches v0.1.0 (file:///projects/branches)
    Finished dev [unoptimized + debuginfo] target(s) in 0.31 secs
     Running `target/debug/branches`
condition was true
```

देखते हैं क्या होता है अगर हम `number` को बदल दें ताकी कंडिषन जलत (`false`) हो।

```rust,ignore
let number = 7;
```

फिरसे प्रोगराम चलाएं, तो यह दिखेगा।

```text
$ cargo run
   Compiling branches v0.1.0 (file:///projects/branches)
    Finished dev [unoptimized + debuginfo] target(s) in 0.31 secs
     Running `target/debug/branches`
condition was false
```

ध्यान दें कि कंडिषन को `bool` होना ज़रूरी है। नही तो एरर मिलेगा। उदाहरण से:

<span class="filename">Filename: src/main.rs</span>

```rust,ignore
fn main() {
    let number = 3;

    if number {
        println!("number was three");
    }
}
```

इस बार `if` कंडिषन की जानकारी `3` है, और रस्ट कंपाइलर एरर देती है।

```text
error[E0308]: mismatched types
 --> src/main.rs:4:8
  |
4 |     if number {
  |        ^^^^^^ expected bool, found integral variable
  |
  = note: expected type `bool`
             found type `{integer}`
```

एरर कहता है कि रस्ट कंपाइलर अपेक्षा कर रही थी कि कंडिषन मे `bool` मिलेगा, लिकिन `integer` (संख्या) मिल गया। Ruby और Javascript के विपरीत, रस्ट अपने आप चीज़ों को `bool` मे नही बदलता। आपको स्पष्ट होकर कंडिषन मे `bool` देना होगा। उदाहरण से, यदी चाहें कि `if` सिर्फ़ नभी चले जब `number` मे `0` न हो, तो ऐसे लिख सकते हैं।

<span class="filename">Filename: src/main.rs</span>

```rust
fn main() {
    let number = 3;

    if number != 0 {
        println!("number was something other than zero");
    }
}
```

यह चलाने पर दिखेगा: `number was something other than zero`.

#### `else if` के साथ अनेक कंडिषन

आप `else if` को प्रयोग करके, अनेक कंडिषन लिख सकते हैं। उदाहरण से:

<span class="filename">Filename: src/main.rs</span>

```rust
fn main() {
    let number = 6;

    if number % 4 == 0 {
        println!("number is divisible by 4");
    } else if number % 3 == 0 {
        println!("number is divisible by 3");
    } else if number % 2 == 0 {
        println!("number is divisible by 2");
    } else {
        println!("number is not divisible by 4, 3, or 2");
    }
}
```

यह प्रोग्राम चार अलग-अलग प्रकार से चल सकता है। चलाने पर आपको यह दिखना चाहिए:

```text
$ cargo run
   Compiling branches v0.1.0 (file:///projects/branches)
    Finished dev [unoptimized + debuginfo] target(s) in 0.31 secs
     Running `target/debug/branches`
number is divisible by 3
```

चलते समय, यह प्रोग्राम हर `if` एक्सपरेशन को देखता है, और ऐसे पहली कोड बलांक को चला देता है जिस के लिए कंडिषन सच हो। ध्यान दें, कि 6, 2 से विभाज्य है, लेकिन इसके बावजूद हम आउटपुट मे `number is divisible by 2` या `number is not divisible by 4, 3 or 2` नही देखते। यह इस लिए क्योंकी रस्ट सिर्फ़ पहली ऐसी बलांक को चलाता है जिसकी कंडिषन सच हो। ऐसी बलांक मिलने के बाद, बाकी देखता तक नही है।

बहुत सारे `else if` एक्सप्रेसन प्रयोग करने पर, आपके कोड को पढने मे मुशकिल हो सकती है। इस लिये, एक से अधिक होने पर, आप अपने कोड को ऐसे लिखने कि कोशिश कर सकते हैं कि पढने मे आसानी हो। अधयाय 6 मे हम यह करने के लिये एक बहुत ही अच्छा `match` एक्सपरेशन के बारे मे सीखेंगे।

#### `let` वाक्य मे `if` का प्रयोग

क्योंकी `if` एक एक्सप्रेसन है, हम उसे `let` के दायें हात की तरफ़ इसतेमाल कर सकते हैं। उदाहरण से:
<span class="filename">Filename: src/main.rs</span>

```rust
fn main() {
    let कंडिषन = true;
    let संख्या = if कंडिषन { 5 } else { 6 };

    println!("संख्या की जानकारी: {}", संख्या);
}
}
```

<span class="caption">Listing 3-2: `if` से मिले जानकारी को किसी चर (यहां, `संख्या`) मे भरना।</span>

`if` एक्सप्रेसन के अनुसार, `संख्या` चर मे जानकारी भरी जायगी। कोड चला के देखें कि क्या होता है:

```text
$ cargo run
   Compiling branches v0.1.0 (file:///projects/branches)
    Finished dev [unoptimized + debuginfo] target(s) in 0.30 secs
     Running `target/debug/branches`
संख्या की जानकारी: 5
```

याद करें की कोड बलांक कि जानकारी उनके आखरी एक्सप्रेशन के बराबर होती है, और संख्या अपने आप मे एक्सप्रेसन होते हैं। यहां, पुरे `if` एक्सप्रेसन की जानकारी निर्भर है की कौंसी कोड बलांक चली। इसका अर्थ यह है कि `if` एक्सपरेशन के सारे कोड बलांक का टाइप एक ही होना चाहिये, क्योंकी उसकी जानकारी कोई भी बलांक से आ सकती है। उपर लिखे कोड मे, दोनो हिस्सों के टाइप `i32` हैं। अगर टाइप अलग-अलग हों, जैसे कि नीचे वाली उदाहरण मे है, तो हमे एरर मिलेगा:

<span class="filename">Filename: src/main.rs</span>

```rust,ignore
fn main() {
    let कंडिशन = true;

    let संख्या = if कंडिेशन {
        5
    } else {
        "छह"
    };

    println!("संख्या की जानकारी: {}", संख्या);
}
```

इस कोड को कंपाइल करने पर एरर मिलता है। `if` और `else` के टाइप अलग-अलग हैं, और रस्ट कंपाइलर हमे बता देती है कि समस्या कहां है।

```text
error[E0308]: if and else have incompatible types
 --> src/main.rs:4:18
  |
4 |       let संख्या = if कंडिशन {
  |  __________________^
5 | |         5
6 | |     } else {
7 | |         "छह"
8 | |     };
  | |_____^ expected integral variable, found &str
  |
  = note: expected type `{integer}`
             found type `&str`
```

`if` बलांक का एक्सप्रेसन integer है और `else` बलांक का एक्सप्रेशन string है। यह नही काम करेगा क्योंकी दोनो का टाइप एक होना जरूरी है। कंपाइल करते समय रस्ट कंपाइलर को रह जानना ज़रूरी है की `संख्या` चर का क्या टाइप है, ताकी वह कंपाइल करते समय ही यह निस्चित कर सकती है कि `संख्या` का जहा भी प्रयोग हो रहा है, वहा उसका टाइप सही है। अगर `संख्या` का टाइप कंपाइल करते समह निशचित ना होकर सिर्फ़ कोड चलाते समय निशचित हो, तो कंपाइलर और जटिल हो जायगी और कोड मे गलतियां कम निकाल पाएगी। यह इसलिए क्योंकी उसे किसी भी चर के लिए अनेक टाइप का ध्यान रखना होगा।

### कोड को बार-बार चलाना

अक्सर एक कोड बलांक को बार-बार चलाने से फ़ायदा होता है। इस काम के लिए रस्ट मे कई *लूप* (loop) हैं। लूप अपने कोड बलांक को चलाकर, फिर से शुरुआत से चलाना आरंभ करते हैं। लूप सीखने के लिए चलो *loops* नामक एक नया प्रोग्राम बनाते हैं।

रस्ट मे तीन तरह के लूप हैं: `loop`, `while`, और `for`। चलो एक-एक करके सबको परखते हैं।

#### `loop` का उप्योग

`loop` रस्ट को आदेश देता है कि वह उसके अगले कोड बलांक को बार-बार चलाए, जब तक आप उसे स्पष्ट तौर से रुकने ना बोलते।

उदाहरण से, *loops* फ़ोलडर मे *src/main.rs* फ़ाइल को ऐसे बदलो कि निम्नलिखित कोड जैसे दिखे:

<span class="filename">Filename: src/main.rs</span>

```rust,ignore
fn main() {
    loop {
        println!("फ़िरसे!");
    }
}
```

प्रोग्राम चलाने पर हम देखेंगे कि `फ़िरसे!` बार-बार लिखता है। अधिकतर टरमिनल (terminal) <span class="keystroke">ctrl-c</span> द्वारा आपको किसी प्रोग्राम को रोकने देते हैं। कोशिश कीजिए:

When we run this program, we’ll see `again!` printed over and over continuously
until we stop the program manually. Most terminals support a keyboard shortcut,
<span class="keystroke">ctrl-c</span>, to halt a program that is stuck in a
continual loop. Give it a try:

```text
$ cargo run
   Compiling loops v0.1.0 (file:///projects/loops)
    Finished dev [unoptimized + debuginfo] target(s) in 0.29 secs
     Running `target/debug/loops`
फ़िरसे!
फ़िरसे!
फ़िरसे!
फ़िरसे!
^Cफ़िरसे!
```

`^C` उस समय का संकेत करता है जब आपने <span class="keystroke">ctrl-c</span> दबाया। हो सकता है कि आपको `फ़िरसे` दिखे या ना दिखे, जो इस पर निर्भर करता है कि लूप मे कोड काहां थी जब आपने <span class="keystroke">ctrl-c</span> दबाकर प्रोग्राम के गती को रोका।

रस्ट एक और, ज्यादा भरोसेमंद, लूप से बाहर निकलने का तरीका देती है। आप कहीं भी `break` लिखकर रस्ट को बता सकते हैं कि लूप से बाहर कब निकलना है। याद करें कि हमने यह व्यवसथा अध्याय 2: "अंक अनुमान खेल बनाना" वाले हिस्से मे उपयोग किया था प्रोग्राम को तब बंद करने के लिए जब इंसान ने संख्या का सही अनुमान लगा लिया हो।

#### लूप से बाहर आना

`loop` का एक मुख्य उपयोग है किसी कार्य को करने की कोशिश तब तक करते रहना जब तक वह सफ़ल न हो जाय। उदाहरण से, देखना कि किसी थ्रेड (thread) ने अपना काम खतम किया कि नही। यह करते समय आपको उस कार्य के नतीजे के बारे मे बाकी के प्रोग्राम को बताने कि ज़रूरत पड सकती है। इस स्थिती मे, लूप खतम करते समय, आप उस नतीजे की जानकारी `break` मे जोड सकते है। ऐसा करेंगे तो वह लूप एक्सप्रेशन का जानकारी बन जाएगा।

```rust
fn main() {
    let mut संख्या = 0;

    let नतीजा = loop {
        संख्या += 1;

        if संख्या == 10 {
            break संख्या * 2;
        }
    };

    assert_eq!(नतीजा, 20);
}
```

#### `while` लूप का प्रयोग

अक्सर लूप के अंदर किसि कंडिषन पर निगरानी रखने से फ़ायदा होता है। जब तक कंडिषन सच है, तब तक लूप चलेगी। कंडिषन के गलत होने पर, प्रोग्राम `break` चलाकर लूप से बाहर आ सकती है। इस प्रकार के लूप को `loop`, `if` और `break` द्वारा लखा जा सकता है; चाहें तो आप यह अब लिखकर देख सकते हैं।

लेकिन इस तरह के लूप प्रोग्राम मे इतने बार लिखे जाते हैं, कि रस्ट मे इसके लिये `while` नामक एक खास व्यवसथा है। निम्नलिखित प्रोग्राम 3 बार तूप चलाती है, हर बार एक संदेश लिखकर `संख्या` को कम करते हुए, और लूप के बाद एक और संदेश `बढिया!!!` लिखकर खतम कर देती है।

<span class="filename">Filename: src/main.rs</span>

```rust
fn main() {
    let mut संख्या = 3;

    while संख्या != 0 {
        println!("{}!", संख्या);

        संखया = संख्या - 1;
    }

    println!("बढिया!!!");
}
```

<span class="caption">Listing 3-3: `while` लूप का उपयोग करके, कोड को तब तक चलाना जब तक एक कंडिशन (`संख्या != 0`) सच है।</span>

यह व्यवसथा हमे `loop`, `if`, `else` औेर `break` बचाती है, और कोड को और आसानी से पढने लायक बना देती है।

#### `for` का प्रयोग


You could use the `while` construct to loop over the elements of a collection,
such as an array. For example, let’s look at Listing 3-4:

<span class="filename">Filename: src/main.rs</span>

```rust
fn main() {
    let a = [10, 20, 30, 40, 50];
    let mut index = 0;

    while index < 5 {
        println!("the value is: {}", a[index]);

        index = index + 1;
    }
}
```

<span class="caption">Listing 3-4: Looping through each element of a collection
using a `while` loop</span>

Here, the code counts up through the elements in the array. It starts at index
`0`, and then loops until it reaches the final index in the array (that is,
when `index < 5` is no longer true). Running this code will print every element
in the array:

```text
$ cargo run
   Compiling loops v0.1.0 (file:///projects/loops)
    Finished dev [unoptimized + debuginfo] target(s) in 0.32 secs
     Running `target/debug/loops`
the value is: 10
the value is: 20
the value is: 30
the value is: 40
the value is: 50
```

All five array values appear in the terminal, as expected. Even though `index`
will reach a value of `5` at some point, the loop stops executing before trying
to fetch a sixth value from the array.

But this approach is error prone; we could cause the program to panic if the
index length is incorrect. It’s also slow, because the compiler adds runtime
code to perform the conditional check on every element on every iteration
through the loop.

As a more concise alternative, you can use a `for` loop and execute some code
for each item in a collection. A `for` loop looks like this code in Listing 3-5:

<span class="filename">Filename: src/main.rs</span>

```rust
fn main() {
    let a = [10, 20, 30, 40, 50];

    for element in a.iter() {
        println!("the value is: {}", element);
    }
}
```

<span class="caption">Listing 3-5: Looping through each element of a collection
using a `for` loop</span>

When we run this code, we’ll see the same output as in Listing 3-4. More
importantly, we’ve now increased the safety of the code and eliminated the
chance of bugs that might result from going beyond the end of the array or not
going far enough and missing some items.

For example, in the code in Listing 3-4, if you removed an item from the `a`
array but forgot to update the condition to `while index < 4`, the code would
panic. Using the `for` loop, you wouldn’t need to remember to change any other
code if you changed the number of values in the array.

The safety and conciseness of `for` loops make them the most commonly used loop
construct in Rust. Even in situations in which you want to run some code a
certain number of times, as in the countdown example that used a `while` loop
in Listing 3-3, most Rustaceans would use a `for` loop. The way to do that
would be to use a `Range`, which is a type provided by the standard library
that generates all numbers in sequence starting from one number and ending
before another number.

Here’s what the countdown would look like using a `for` loop and another method
we’ve not yet talked about, `rev`, to reverse the range:

<span class="filename">Filename: src/main.rs</span>

```rust
fn main() {
    for number in (1..4).rev() {
        println!("{}!", number);
    }
    println!("LIFTOFF!!!");
}
```

This code is a bit nicer, isn’t it?

## Summary

You made it! That was a sizable chapter: you learned about variables, scalar
and compound data types, functions, comments, `if` expressions, and loops! If
you want to practice with the concepts discussed in this chapter, try building
programs to do the following:

* Convert temperatures between Fahrenheit and Celsius.
* Generate the nth Fibonacci number.
* Print the lyrics to the Christmas carol “The Twelve Days of Christmas,”
taking advantage of the repetition in the song.

When you’re ready to move on, we’ll talk about a concept in Rust that *doesn’t*
commonly exist in other programming languages: ownership.
