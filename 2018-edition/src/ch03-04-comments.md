## "विवरण" (comment)

सारे परोगरांमर चाहते हैं कि वह कोड ऐसा लिखें कि आसानी से समझ मे आ जाय। फिर भी,
कभी कभी सपष्टिकरण की जरूरत पदती है। ऐसे स्थिती मे, परोगरामर कोड मे विवरण लिख
देते हैं, जो कंपाइलर नज़रअंदाज कर देता है, लेकिन इंसानों को कोड पढते समय सहायना
मिल सकता है।

विवरण का उदाहरण:

```rust
// Hello, world.
```

रस्ट मे विवरण `//` से शुरू होते हैं और लाइन के अंत तक जारी रहते हैं। अगर आप
चाहते हैं कि विवरण एक लाइन से अधिक चले, तो हर लाइन के आगे `//` जोडें, ऐसे:

```rust
// So we’re doing something complicated here, long enough that we need
// multiple lines of comments to do it! Whew! Hopefully, this comment will
// explain what’s going on.
```

विवरण को कोड वाले लाइन के अंत पर भि रख सकते हैं:

<span class="filename">Filename: src/main.rs</span>

```rust
fn main() {
    let lucky_number = 7; // I’m feeling lucky today.
}
```

लेकिन ज़्यादातर आप विवरण को इस रूप मे देखेंगे, जहां वह अलग लाइन मे लिखा हो।
प्रथानुसार, विवरण को उस कोड के ऊपरी लाइन मे लिखा जाता है, जिस कोड कि वह व्याखया
दे रहा हो।

<span class="filename">Filename: src/main.rs</span>

```rust
fn main() {
    // I’m feeling lucky today.
    let lucky_number = 7;
}
```

रस्ट मे एक और प्रकार से विवरण लिख सकते हैं, जो हम अध्याय 14 मे देखेंगे।
