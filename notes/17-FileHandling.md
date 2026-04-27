# File Handling Basics — Notes

## What is File Handling?

File handling means storing data in files and reading data back from files.

Without files:

Data disappears when program ends.

With files:

Data can be saved permanently.

---

## Why Use Files?

Files help store:

* Student records
* Marks
* Reports
* Logs
* Configuration data

---

## Real-Life Analogy

Notebook:

* Write information
* Read later

File works similarly.

---

## Types of Files

### Text Files

Human readable.

Examples:

```text id="l1"
marks.txt
students.txt
```

---

### Binary Files

Machine-oriented data.

(Advanced later.)

---

# 82. Reading Files

## Opening a File

```python id="f1"
file=open("data.txt","r")
```

Mode:

```text id="f2"
r = read
```

---

## Read Entire File

```python id="f3"
content=file.read()

print(content)
```

---

## Example File

data.txt

```text id="f4"
Raj 90
Ana 85
Tom 78
```

---

## Read Line by Line

```python id="f5"
for line in file:
    print(line)
```

---

## Read One Line

```python id="f6"
line=file.readline()
```

---

## Read All Lines into List

```python id="f7"
lines=file.readlines()
```

---

## Close File

```python id="f8"
file.close()
```

Important.

---

## Better Way — `with`

```python id="f9"
with open("data.txt","r") as file:

   data=file.read()
```

Automatically closes file.

Preferred.

---

## Example — Count Lines

```python id="f10"
count=0

with open("data.txt") as file:

   for line in file:
      count+=1
```

---

## Example — Sum Numbers from File

File:

```text id="f11"
10
20
30
```

Code

```python id="f12"
total=0

with open("nums.txt") as file:

   for line in file:

      total+=int(line)
```

---

## Reading Skills Used

* Traversal
* Parsing
* Accumulation

---

# 83. Writing Files

## Open for Writing

```python id="f13"
file=open("out.txt","w")
```

Mode:

```text id="f14"
w = write
```

---

## Write Data

```python id="f15"
file.write("Hello")
```

---

## Close

```python id="f16"
file.close()
```

---

## Example

```python id="f17"
with open("marks.txt","w") as file:

   file.write("Raj 90\n")
   file.write("Ana 85\n")
```

---

## Important

Mode `"w"` overwrites old content.

---

## Append Mode

```python id="f18"
open("marks.txt","a")
```

```text id="f19"
a = append
```

Adds at end.

---

## Example Append

```python id="f20"
with open("marks.txt","a") as file:

   file.write("Tom 78\n")
```

---

## Write Using Loop

```python id="f21"
for i in range(5):

   name=input()

   file.write(name+"\n")
```

---

## Write Numbers

```python id="f22"
file.write(str(num))
```

Convert to string.

---

## Common Write Modes

| Mode | Meaning         |
| ---- | --------------- |
| r    | Read            |
| w    | Write (replace) |
| a    | Append          |
| r+   | Read and Write  |

---

# 84. File-Based Problem Solving

Now use files to solve problems.

---

## Problem Pattern

Read data

↓

Process data

↓

Produce result

---

## Example 1 — Find Highest Mark

File:

```text id="f23"
Raj 90
Ana 85
Tom 95
```

---

Process:

Track maximum.

```python id="f24"
highest=0
topper=""
```

---

Read each line.

Split data.

```python id="f25"
parts=line.split()
```

---

Compare marks.

Update highest.

---

## Example 2 — Count Words in File

```python id="f26"
count=0

with open("data.txt") as file:

   for line in file:

      words=line.split()

      count+=len(words)
```

---

## Example 3 — Search Word in File

```python id="f27"
for line in file:

   if "Python" in line:
      print("Found")
```

---

## Example 4 — Student Report from File

Read marks.

Compute average.

Average=\frac{Total}{Count}

---

## Example 5 — Frequency Count from File

Count repeated words.

Use dictionary.

```python id="f28"
freq={}
```

---

## Example 6 — Copy One File to Another

```python id="f29"
with open("a.txt") as src:

   data=src.read()

with open("b.txt","w") as dst:

   dst.write(data)
```

---

## File Processing Pattern

Very common:

```python id="f30"
for line in file:

   process(line)
```

---

## Parsing Data

Suppose line:

```text id="f31"
Raj,90
```

Split:

```python id="f32"
name,mark=line.split(",")
```

Parsing converts text into usable pieces.

---

# File + Dictionary Example

Build student lookup from file.

File:

```text id="f33"
Raj 90
Ana 85
```

Code

```python id="f34"
students={}
```

Read lines.

Store:

```python id="f35"
students[name]=mark
```

Now lookup possible.

---

# Common File Problems

## Reading Problems

* Count lines
* Count words
* Sum numbers
* Search data

---

## Writing Problems

* Save records
* Append entries
* Generate reports

---

## Processing Problems

* Find highest
* Compute average
* Frequency counts

---

# Common Mistakes

## Forget Close

```python id="f36"
file.close()
```

Use `with`.

---

## Using Write for Numbers

Wrong

```python id="f37"
file.write(25)
```

Need:

```python id="f38"
file.write(str(25))
```

---

## Using "w" Accidentally

Can erase old file.

---

## Forget Strip Newline

Lines often contain:

```text id="f39"
\n
```

Remove:

```python id="f40"
line.strip()
```

---

## Wrong Split Format

File format mismatch causes errors.

---

# Practice Problems

## Reading

1. Read file contents
2. Count lines
3. Sum numbers in file

---

## Writing

4. Store student names
5. Append marks
6. Generate report file

---

## File-Based Problems

7. Find topper from file
8. Search word in file
9. Count word frequency

---

# Summary

## Core Syntax

Open

```python id="f41"
open("a.txt","r")
```

---

Read

```python id="f42"
file.read()
```

---

Write

```python id="f43"
file.write()
```

---

Append

```python id="f44"
open("a.txt","a")
```

---

Safe style

```python id="f45"
with open(...) as file
```

---

## Core Problem Types

* Reading
* Writing
* Appending
* Parsing
* File processing

---

## Thinking Skills Used

* Data persistence
* Traversal
* Parsing
* Aggregation
* Problem decomposition

---

## File Problem Formula

For every file problem ask:

1. Read or write?
2. What file format?
3. Process each line how?
4. Need parsing?
5. Need aggregate result or report?

That is the foundation of file handling.
