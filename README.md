#  Python Text Analyzer

A beginner-friendly Python script that takes a sentence from the user and reports three things: the **number of characters**, the **number of words**, and how many times a **chosen letter** appears.

---

##  Overview

This project practices core Python fundamentals: taking user input, working with strings, splitting text into words, and looping through characters with a counter.

**The script:**

1. Asks the user to type a sentence
2. Prints the total number of characters (including spaces and punctuation)
3. Prints the number of words
4. Asks for a letter to look for
5. Prints how many times that letter appears

---

##  How to Run

Make sure [Python 3](https://www.python.org/downloads/) is installed, then run:

```bash
python text_analyzer.py
```


**Example**

```
Put in a sentence: Hello world
11
2
Which letter do you want to count? l
3
```

| Output | Meaning |
|---|---|
| `11` | Characters in "Hello world" (the space counts) |
| `2` | Words |
| `3` | Times the letter `l` appears |

---

##  Concepts Demonstrated

| Concept | Where it appears |
|---|---|
| **User input** | `input()` collects the sentence and the letter |
| **String length** | `len(text)` counts every character |
| **Splitting strings** | `text.split()` breaks the sentence into a list of words |
| **Loops** | `for char in text` visits each character one at a time |
| **Conditionals** | `if char == target_letter` checks for a match |
| **Counter variable** | `letter_count` increases by 1 on every match |

---



