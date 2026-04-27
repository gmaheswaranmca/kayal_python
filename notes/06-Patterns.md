# Pattern Problems — Notes

## What is a Pattern Problem?

A pattern problem prints a repeated arrangement of:

* Symbols (`*`)
* Numbers
* Characters
* Shapes

Pattern problems mainly teach:

* Loops
* Nested loops
* Counting logic
* Pattern recognition

---

## Basic Idea

Usually:

* Outer loop → controls rows
* Inner loop → controls columns/items in each row

General structure:

```python
for row in range(...):

    for col in range(...):
        print(...)

    print()
```

---

# 29. Star Patterns

## 1. Single Line Stars

Output

```text
*****
```

Code

```python
for i in range(5):
    print("*",end="")
```

---

## 2. Square Pattern

Output

```text
****
****
****
****
```

Code

```python
for i in range(4):

    for j in range(4):
        print("*",end="")

    print()
```

---

## 3. Right Triangle

Output

```text
*
**
***
****
```

Code

```python
for i in range(1,5):

    for j in range(i):
        print("*",end="")

    print()
```

---

## 4. Inverted Triangle

Output

```text
****
***
**
*
```

Code

```python
for i in range(4,0,-1):

    for j in range(i):
        print("*",end="")

    print()
```

---

## 5. Hollow Square

Output

```text
****
*  *
*  *
****
```

Code

```python
n=4

for i in range(n):

    for j in range(n):

        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end="")

        else:
            print(" ",end="")

    print()
```

---

# 30. Number Patterns

## 1. Repeated Number Pattern

Output

```text
1
22
333
4444
```

Code

```python
for i in range(1,5):

    for j in range(i):
        print(i,end="")

    print()
```

---

## 2. Increasing Numbers

Output

```text
1
12
123
1234
```

Code

```python
for i in range(1,5):

    for j in range(1,i+1):
        print(j,end="")

    print()
```

---

## 3. Continuous Numbers

Output

```text
1
2 3
4 5 6
7 8 9 10
```

Code

```python
num=1

for i in range(1,5):

    for j in range(i):
        print(num,end=" ")
        num+=1

    print()
```

---

## 4. Odd Number Pattern

Output

```text
1
1 3
1 3 5
```

Can be built using arithmetic progression.

---

# 31. Pyramid Patterns

A pyramid usually uses:

* Spaces
* Symbols
* Symmetry

---

## Simple Pyramid

Output

```text
   *
  ***
 *****
*******
```

Code

```python
n=4

for i in range(1,n+1):

    for s in range(n-i):
        print(" ",end="")

    for j in range(2*i-1):
        print("*",end="")

    print()
```

---

## Formula

Stars in each row:

2i-1

---

## Inverted Pyramid

Output

```text
*******
 *****
  ***
   *
```

---

## Number Pyramid

Output

```text
   1
  121
 12321
```

Symmetric pattern.

---

## Diamond Pattern

Combine:

* Normal pyramid
* Inverted pyramid

---

# 32. Nested Loop Techniques

## What is a Nested Loop?

Loop inside another loop.

Syntax:

```python
for i in range(rows):

   for j in range(cols):
      statements
```

---

## Outer Loop Controls

* Rows
* Lines
* Levels

---

## Inner Loop Controls

* Columns
* Symbols per row
* Spaces

---

## Example

```python
for i in range(3):

   for j in range(4):
      print("*",end="")

   print()
```

Output

```text
****
****
****
```

---

## Mixed Nested Loops

Spaces + Stars

```python
for i in range(1,n+1):

    for s in range(n-i):
        print(" ",end="")

    for j in range(i):
        print("*",end="")

    print()
```

---

## Common Nested Loop Structures

### Fixed inner loop

```python
for i in range(5):
   for j in range(3):
```

Same columns every row.

---

### Variable inner loop

```python
for i in range(5):
   for j in range(i):
```

Columns grow.

---

### Reverse inner loop

```python
for i in range(5,0,-1):
```

Columns shrink.

---

## Nested Loop Thinking

Ask:

Rows?

Columns?

Spaces?

Pattern formula?

---

# 33. Pattern Recognition Strategies

This is the most important part.

Do not memorize patterns.

Recognize the rule.

---

## Strategy 1 — Count Rows

Example

```text
*
**
***
****
```

Rows = 4

---

## Strategy 2 — Find Items per Row

Row 1 → 1 star
Row 2 → 2 stars

Rule:

Number of stars = row number

---

## Strategy 3 — Find Formula

Example pyramid:

Stars:

1
3
5
7

Pattern:

2i-1

---

## Strategy 4 — Check Spaces

Example

```text
   *
  ***
 *****
```

Leading spaces:

3
2
1

Formula:

n-i

---

## Strategy 5 — Break into Components

A pyramid has:

* Spaces loop
* Symbols loop
* Newline

Break it apart.

---

## Strategy 6 — Use Tables

Example:

| Row i | Spaces | Stars |
| ----- | ------ | ----- |
| 1     | 3      | 1     |
| 2     | 2      | 3     |
| 3     | 1      | 5     |
| 4     | 0      | 7     |

Find formula.

---

## Strategy 7 — Dry Run Small Cases

Try n=3 first.

Small examples reveal rule.

---

## Pattern Types to Recognize

### Increasing

```text
*
**
***
```

---

### Decreasing

```text
***
**
*
```

---

### Symmetric

```text
  *
 ***
*****
```

---

### Repeating

```text
111
222
333
```

---

### Alternating

```text
1010
0101
```

---

# Common Mistakes

## Missing Newline

Wrong

```python
print("*",end="")
```

without row-level `print()`.

---

## Wrong Inner Loop Range

Wrong

```python
for j in range(i+1)
```

May print extra symbol.

---

## Forgetting Spaces in Pyramid

No spaces gives triangle, not pyramid.

---

## Confusing Rows vs Columns

Outer = rows

Inner = columns

---

# Practice Problems

## Star Patterns

1. Square
2. Triangle
3. Inverted triangle
4. Hollow square

---

## Number Patterns

5. 1234 pattern
6. Repeated row numbers
7. Floyd's triangle

---

## Pyramid

8. Centered pyramid
9. Inverted pyramid
10. Diamond

---

## Advanced

11. Pascal’s triangle
12. Checkerboard pattern
13. Butterfly pattern

---

# Summary

## Core Structure

```python
for row:

   for col:

   print()
```

---

## Core Formulas

Increasing:

j=i

---

Pyramid stars:

2i-1

---

Spaces:

n-i

---

## Skills Learned

* Nested loops
* Pattern recognition
* Counting logic
* Formula discovery
* Iterative thinking

---

## Pattern Solving Formula

For every pattern ask:

1. How many rows?
2. How many symbols each row?
3. Any spaces?
4. What formula generates symbols?
5. Outer loop?
6. Inner loop?

That is the foundation of pattern programming.
