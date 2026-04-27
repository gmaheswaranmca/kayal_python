# Dictionaries — Notes

## What is a Dictionary?

A dictionary stores data as **key → value** pairs.

Think of a real dictionary:

Word → Meaning

Programming dictionary:

Student Name → Marks

```python id="8f1v9a"
marks={
 "Raj":90,
 "Ana":85
}
```

---

## Why Dictionaries?

Useful when data is based on lookup.

Instead of:

```python id="8v7g0w"
if name=="Raj":
   print(90)
```

Use:

```python id="v4n7ph"
print(marks["Raj"])
```

---

## Dictionaries are:

* Unordered mappings (conceptually key-based access)
* Fast lookup
* Good for counting
* Good for search by key

---

# 64. Dictionary Basics

## Creating Dictionary

```python id="bb2chm"
student={
 "name":"Sam",
 "age":15,
 "grade":"A"
}
```

---

## Structure

```text id="k0f5oe"
key : value
```

Example:

```text id="p0u4n6"
name : Sam
```

---

## Access Value

```python id="m0cizj"
student["name"]
```

Output:

```text id="9kbl6x"
Sam
```

---

## Add New Pair

```python id="0hmbjx"
student["city"]="Chennai"
```

---

## Update Value

```python id="2m7n3d"
student["age"]=16
```

---

## Remove Item

```python id="5p2mfi"
del student["age"]
```

---

## Dictionary Length

```python id="9wwjgl"
len(student)
```

---

## Check Key Exists

```python id="f1nt6p"
if "name" in student:
```

---

## Get Method

Safer:

```python id="7abk9o"
student.get("name")
```

---

## Keys

```python id="8a4h2x"
student.keys()
```

---

## Values

```python id="8df9mn"
student.values()
```

---

## Items

```python id="9jf4cb"
student.items()
```

Returns key-value pairs.

---

## Traversing Dictionary

```python id="jlwmd1"
for k,v in student.items():
   print(k,v)
```

---

# 65. Key-Value Problem Solving

Use dictionaries to model relationships.

---

## Example 1 — Student Marks

```python id="jlwmd2"
marks={
 "Raj":90,
 "Ana":85
}
```

Find Raj’s marks:

```python id="jlwmd3"
marks["Raj"]
```

---

## Example 2 — Phone Directory

```python id="jlwmd4"
phone={
 "Tom":"5555",
 "Ann":"2222"
}
```

Lookup by name.

---

## Example 3 — Product Price Lookup

```python id="jlwmd5"
price={
 "Pen":10,
 "Book":50
}
```

---

## Example 4 — Menu Choice Mapping

```python id="jlwmd6"
days={
1:"Mon",
2:"Tue"
}
```

---

## Example 5 — Grade Mapping

```python id="jlwmd7"
grades={
90:"A",
80:"B"
}
```

---

## Problem Pattern

Input key

Search dictionary

Return value

---

## Example — Add Student Marks

```python id="jlwmd8"
name=input()

marks=int(input())

students[name]=marks
```

---

## Example — Find Highest Marks

```python id="jlwmd9"
best=max(marks.values())
```

(Conceptual beginner idea)

---

## Common Key-Value Problems

* Student database
* Phone directory
* Product pricing
* Translation mapping
* Menu lookup

---

# 66. Frequency Counting Problems

## What is Frequency Counting?

Count how many times something appears.

Dictionary is ideal.

---

## Example

Word:

banana

Counts:

```text id="jlwmd10"
b:1
a:3
n:2
```

---

## Algorithm

For each character:

If already seen:

Increase count.

Else:

Start at 1.

---

## Code

```python id="jlwmd11"
freq={}
```

```python id="jlwmd12"
for ch in "banana":

   if ch in freq:
      freq[ch]+=1

   else:
      freq[ch]=1
```

---

## Result

```python id="jlwmd13"
print(freq)
```

---

## Shorter Pattern

```python id="jlwmd14"
freq[ch]=freq.get(ch,0)+1
```

Very common.

---

## Count Numbers in List

```python id="jlwmd15"
nums=[2,3,2,5,3]

freq={}
```

Use same logic.

---

## Output

```text id="jlwmd16"
2:2
3:2
5:1
```

---

## Find Most Frequent Element

Track highest count.

---

## First Non-Repeating Character

Frequency =1

---

## Duplicate Detection

If count >1

Duplicate.

---

## Common Frequency Problems

* Character counts
* Word counts
* Number frequency
* Most frequent value
* Duplicates

---

# 67. Lookup Problems

## What is Lookup?

Retrieve value using key.

Core dictionary strength.

---

## Example

```python id="jlwmd17"
capital={
 "India":"Delhi",
 "Japan":"Tokyo"
}
```

Lookup:

```python id="jlwmd18"
capital["India"]
```

---

## User Search

```python id="jlwmd19"
country=input()

print(capital.get(country,"Not Found"))
```

---

## Membership Search

```python id="jlwmd20"
if "India" in capital:
```

---

## Reverse Lookup (Find key from value)

Given Tokyo find country.

```python id="jlwmd21"
for k,v in capital.items():

   if v=="Tokyo":
      print(k)
```

---

## Default Lookup

```python id="jlwmd22"
d.get(key,default)
```

Example:

```python id="jlwmd23"
marks.get("Joe",0)
```

---

## Caching Concept (Simple Idea)

Dictionary can store answers already computed.

Example:

```python id="jlwmd24"
memo={}
```

(Advanced later.)

---

## Lookup Problems Examples

* Country → capital
* Product → price
* Student → marks
* Employee → salary
* ID → Name

---

# Dictionary Problem Strategies

## Strategy 1 — Mapping Problem?

If data has relationship:

Use dictionary.

---

## Strategy 2 — Counting Problem?

Use frequency dictionary.

```python id="jlwmd25"
freq[item]+=1
```

---

## Strategy 3 — Fast Search by Key?

Use dictionary lookup.

---

## Strategy 4 — Use get()

```python id="jlwmd26"
d.get(key,0)
```

Safer.

---

## Strategy 5 — Update Existing or Create New

Very common pattern:

```python id="jlwmd27"
if key in d:
   d[key]+=1
else:
   d[key]=1
```

---

# Common Mistakes

## Access Missing Key

Wrong

```python id="jlwmd28"
d["x"]
```

May error.

Safer:

```python id="jlwmd29"
d.get("x")
```

---

## Duplicate Keys

Wrong:

```python id="jlwmd30"
d={
 "a":1,
 "a":2
}
```

Second overwrites first.

---

## Forget Update

Wrong:

```python id="jlwmd31"
freq[ch]+1
```

Does nothing.

Correct:

```python id="jlwmd32"
freq[ch]+=1
```

---

## Confusing Keys and Values

```python id="jlwmd33"
for k in d:
```

Iterates keys.

---

# Practice Problems

## Basics

1. Create student dictionary
2. Add/update key
3. Print all items

---

## Key-Value

4. Phone directory lookup
5. Product price lookup
6. Student marks search

---

## Frequency

7. Character frequency
8. Number frequency
9. Find duplicates

---

## Lookup

10. Country-capital search
11. Reverse lookup
12. Find missing key safely

---

# Summary

## Core Syntax

Create

```python id="jlwmd34"
d={}
```

Access

```python id="jlwmd35"
d[key]
```

Update

```python id="jlwmd36"
d[key]=value
```

Safe get

```python id="jlwmd37"
d.get(key,0)
```

---

## Core Patterns

Frequency:

```python id="jlwmd38"
freq[x]=freq.get(x,0)+1
```

Lookup:

```python id="jlwmd39"
if key in d
```

---

## Thinking Skills Used

* Mapping
* Counting
* Lookup reasoning
* Data modeling

---

## Dictionary Problem Formula

For every dictionary problem ask:

1. Is there key → value mapping?
2. Is this frequency counting?
3. Need fast lookup?
4. Need update-or-create pattern?
5. Use normal access or safe get()?

That is the foundation of dictionary programming.
