---
title: "Morse Code Translator In Python"
author: "chalamohamed93"
date: 2022-09-22
description: "Morse code is a method of transmitting text information as a series of on-off tones, lights, or clicks that can be directly understood by a skilled listener or observer without special equipment. It..."
categories: ["Python"]
image: images/4dbd28_f0628b9f7b4d4b2fba3f01987b976be7.webp
wix-url: https://www.datainsightonline.com/post/morse-code-translator-in-python
---
Morse code is a method of transmitting text information as a series of on-off tones, lights, or clicks that can be directly understood by a skilled listener or observer without special equipment. It is named for Samuel F. B. Morse, an inventor of the telegraph.
The algorithm is very simple. Every character in the English language is substituted by a series of dots and dashes or sometimes just singular dot or dash and vice versa as described below :

![](images/4dbd28_f0628b9f7b4d4b2fba3f01987b976be7.webp)

```python
def convert_morse(code):

    code = code.replace("a", ".-")
    code = code.replace("b", "-...")
    code = code.replace("c", "-.-.")
    code = code.replace("d", "-..")
    code = code.replace("e", ".")
    code = code.replace("f", "..-.")
    code = code.replace("g", "--.")
    code = code.replace("h", "....")
    code = code.replace("i", "..")
    code = code.replace("j", ".---")
    code = code.replace("k", "-.-")
    code = code.replace("l", ".-..")
    code = code.replace("m", "--")
    code = code.replace("n", "-.")
    code = code.replace("o", "---")
    code = code.replace("p", ".--.")
    code = code.replace("q", "--.-")
    code = code.replace("r", ".-.")
    code = code.replace("s", "...")
    code = code.replace("t", "-")
    code = code.replace("u", "..-")
    code = code.replace("v", "...-")
    code = code.replace("w", ".--")
    code = code.replace("x", "-..-")
    code = code.replace("y", "-.--")
    code = code.replace("z", "--..")

    code = code.replace("1", ".----")
    code = code.replace("2", "..---")
    code = code.replace("3", "...--")
    code = code.replace("4", "....-")
    code = code.replace("5", ".....")
    code = code.replace("6", "-....")
    code = code.replace("7", "--...")
    code = code.replace("8", "---..")
    code = code.replace("9", "----.")
    code = code.replace("0", "-----")

    code = code.replace(",", "--..--")
    code = code.replace(".", ".-.-.")
    code = code.replace("?", "..--..")
    code = code.replace("/", "-..-.")
    code = code.replace("-", "-....-")
    code = code.replace("(", "-.--.")
    code = code.replace(")", "-.--.-")

    return code
```

covert_morse has a string argument and split each character to replace it bu their corresponding one to construct the morse code.

msg = input("Enter any message: ")
print(f"Initial code :{msg}")
morse = convert_morse(msg)
print(f"Morse code: {morse}")
