# String Problems — Notes

## What is a String?

A string is a sequence of characters.

Examples:

```python
"Python"
"Hello"
"12345"
```

Characters can be:

* Letters
* Digits
* Spaces
* Symbols

---

# 39. String Basics

## Creating Strings

```python
name="Python"
```

```python
msg='Hello'
```

---

## String is a Sequence

"Python"

Positions:

| Index | Character |
| ----- | --------- |
| 0     | P         |
| 1     | y         |
| 2     | t         |
| 3     | h         |
| 4     | o         |
| 5     | n         |

---

## Access Characters

```python
s="Python"

print(s[0])
```

Output

```text
P
```

---

## Negative Index

```python
s[-1]
```

Last character.

---

## Length of String

```python
len(s)
```

Example:

```python
len("Python")
```

Output

```text
6
```

---

## Slicing

Syntax

```python
s[start:end]
```

Example

```python
s="Python"

print(s[0:3])
```

Output

```text
Pyt
```

---

## Concatenation

```python
a="Hello"
b="World"

print(a+b)
```

Output

```text
HelloWorld
```

---

## Repetition

```python
print("Hi"*3)
```

Output

```text
HiHiHi
```

---

## Common String Methods

```python
s.lower()
```

```python
s.upper()
```

```python
s.strip()
```

```python
s.replace("a","x")
```

```python
s.split()
```

---

# 40. Traversing Strings

## What is Traversing?

Processing characters one by one.

---

## Method 1 — `for` Loop

```python
s="Python"

for ch in s:
    print(ch)
```

---

## Method 2 — Using Index

```python
for i in range(len(s)):
    print(s[i])
```

---

## Count Vowels

```python
count=0

for ch in s:

   if ch in "aeiouAEIOU":
      count+=1
```

---

## Print Characters in Reverse

```python
for i in range(len(s)-1,-1,-1):
    print(s[i])
```

---

## Reverse a String

```python
rev=""

for ch in s:
    rev=ch+rev
```

---

## Typical Traversal Problems

* Count vowels
* Count consonants
* Reverse string
* Check palindrome
* Find digits in string

---

# 41. String Manipulation Problems

Changing or transforming strings.

---

## Reverse String

```python
s="hello"

rev=s[::-1]
```

Output

```text
olleh
```

---

## Palindrome Check

```python
if s==s[::-1]:
   print("Palindrome")
```

---

## Convert Case

```python
s.upper()
```

```python
s.lower()
```

---

## Replace Characters

```python
s.replace("a","x")
```

---

## Remove Spaces

```python
s.replace(" ","")
```

---

## Remove Duplicate Characters

```python
result=""

for ch in s:

   if ch not in result:
      result+=ch
```

---

## Find Longest Word

```python
words=s.split()
```

Compare lengths.

---

## Anagram Check

Two strings have same letters.

Example:

listen

silent

Method:

```python
sorted(a)==sorted(b)
```

---

## Common Manipulation Problems

* Reverse
* Palindrome
* Remove duplicates
* Replace characters
* Anagrams

---

# 42. Character Frequency Problems

Count occurrences of characters.

---

## Frequency of One Character

```python
count=0

for ch in s:

   if ch=="a":
      count+=1
```

---

## Frequency of All Characters

Example:

banana

Output

```text
b:1
a:3
n:2
```

---

## Using Dictionary

```python
freq={}
```

```python
for ch in s:

   if ch in freq:
      freq[ch]+=1

   else:
      freq[ch]=1
```

---

## Count Digits in String

```python
count=0

for ch in s:

   if ch.isdigit():
      count+=1
```

---

## Count Letters

```python
if ch.isalpha()
```

---

## Count Spaces

```python
if ch==" "
```

---

## Most Frequent Character

Find character with maximum count.

---

## Common Frequency Problems

* Count vowels
* Frequency of each char
* Most repeated char
* First non-repeating char

---

# 43. Pattern Matching in Strings

Searching patterns inside strings.

---

## Membership Test

```python
if "cat" in s:
```

---

## Find Substring

```python
s.find("cat")
```

Returns position.

---

## Starts With

```python
s.startswith("Py")
```

---

## Ends With

```python
s.endswith(".txt")
```

---

## Manual Pattern Search

Find occurrences of "ab"

```python
count=0

for i in range(len(s)-1):

   if s[i:i+2]=="ab":
      count+=1
```

---

## First Occurrence

```python
for i in range(len(s)):

   if s[i]=="a":
      print(i)
      break
```

---

## Prefix

Beginning part.

Example:

pre in preview

---

## Suffix

Ending part.

Example:

ing in coding

---

## Longest Common Prefix

cat

car

can

Common prefix:

ca

---

## Common Pattern Matching Problems

* Find substring
* Count substring occurrences
* Prefix check
* Suffix check
* Word search

---

# String Problem Strategies

## Strategy 1

Character-by-character traversal.

```python
for ch in s:
```

---

## Strategy 2

Index-based access.

```python
s[i]
```

---

## Strategy 3

Use slicing.

```python
s[i:j]
```

---

## Strategy 4

Use frequency counting.

```python
freq[ch]+=1
```

---

## Strategy 5

Search using sliding window.

Example:

```python
s[i:i+3]
```

---

# Common Mistakes

## Off-by-One Error

Wrong

```python
for i in range(len(s)):
   s[i+1]
```

May go out of bounds.

---

## Forget Strings are Immutable

Wrong

```python
s[0]="A"
```

Not allowed.

---

## Case Sensitivity

```python
A != a
```

Use lower():

```python
s.lower()
```

---

## Counting Overlapping Patterns

Example:

aaa

Pattern aa

Overlapping count can be 2.

Need careful logic.

---

# Practice Problems

## Basics

1. Find length
2. Print first and last character
3. Slice first 3 characters

---

## Traversal

4. Count vowels
5. Reverse string
6. Check palindrome

---

## Manipulation

7. Remove duplicates
8. Replace spaces
9. Check anagram

---

## Frequency

10. Character frequency
11. Most frequent character
12. First non-repeating character

---

## Pattern Matching

13. Find substring
14. Count pattern occurrences
15. Longest common prefix

---

# Summary

## Core Operations

Access:

```python
s[i]
```

Length:

```python
len(s)
```

Slice:

```python
s[a:b]
```

Traversal:

```python
for ch in s
```

---

## Core Problem Types

* Traversal
* Manipulation
* Frequency counting
* Pattern matching

---

## Thinking Skills Used

* Iteration
* Pattern recognition
* Decomposition
* Search logic

---

## String Problem Formula

For every string problem ask:

1. Need character-by-character processing?
2. Need counting?
3. Need substring search?
4. Need transformation?
5. Use traversal, slicing, or frequency map?

That is the foundation of string programming.
