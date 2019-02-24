# सामन्य प्रोग्रामिंग अवधारणाएं

<!-- # Common Programming |ोन्चेप्त्स -->

इस अध्याय मे हम उन अवधारणों का चरचा करेंगे जो लगभग हर प्रोग्रामिंग भाषा मे होते है, और यह बताएंगे कि यह रस्ट मे कैसे काम करते हैं। अशिकांश प्रोग्रामिंग भाषाओं मे कैइ चीज़ें एक जैसे होते हैं। इस अध्याय मे कोई भी अवधारण रस्ट मे विशेश नही हैं, परंतू हम इनकी रस्ट के संदर्भ मे चर्चा करेंगे, और इनके मध्यम से रस्ट के प्रथाओं को स्पष्ट करेंगे।

<!-- This chapter covers concepts that appear in almost every programming language
and how they work in Rust. Many programming languages have much in common at
their core. None of the concepts presented in this chapter are unique to Rust,
but we’ll discuss them in the context of Rust and explain the conventions
around using these concepts. --->

विशेष रूप से, आप चर, बुनियादी टाइप, फ़ंक्शन, कम्मेंट, और प्रोग्राम के बहाव के बारे मे आप सिखेंगे। यह अवधारण हर रस्ट प्रोग्राम मे होंगे, और उन्हें जलदी सीखने से आपको एक अच्छा आधार मिलेगा।

<!-- Specifically, you’ll learn about variables, basic types, functions, comments,
and control flow. These foundations will be in every Rust program, and learning
them early will give you a strong core to start from. -->

> ### कीवर्ङ
>

> रस्ट भाषा मे है *कीवर्ङ* हैं, जो भाषा के प्रयोग के लिये आरक्षित हैं, जैसे कि
> और हाषाओं मे भी होता है। ध्यान रहे, कि इनहें आप किसि चर या फ़ंक्शन के नाम के
> लिये नही प्रयोग कर सकते। ज्यादतर कीवर्ङ के खास अर्थ होते हैं, और रस्ट मे आप
> उनहें कैइ कामों को पूरा करने के लिये प्रयोग करेंगे; कुछ कीवर्ङों का अभी कोइ
> काम नही है, लेकिन उनहें भविश्य के प्रयोग के लिये आरक्षित किया गया है। आप
> कीवर्ङ का सूची परिशिष्ट A मे देख सकते हैं।

<!--
> ### Keywords
>
> The Rust language has a set of *keywords* that are reserved for use by
> the language only, much as in other languages. Keep in mind that you cannot
> use these words as names of variables or functions. Most of the keywords have
> special meanings, and you’ll be using them to do various tasks in your Rust
> programs; a few have no current functionality associated with them but have
> been reserved for functionality that might be added to Rust in the future. You
> can find a list of the keywords in Appendix A.
-->
