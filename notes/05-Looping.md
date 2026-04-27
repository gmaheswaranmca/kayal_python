# Looping Problems — Notes

## What is a Loop?

A loop repeats a block of code multiple times.

Instead of writing:

```python
print(1)
print(2)
print(3)
```

Use a loop.

---

## Why Loops?

Loops help in:

* Repetition
* Counting
* Summation
* Pattern printing
* Number processing
* Iterative problem solving

---

## Types of Loops in Python

1. `for` loop
2. `while` loop

---

# 23. `for` Loop Basics

## What is a `for` loop?

Used when number of repetitions is known.

## Syntax

```python
for variable in sequence:
    statements
```

---

## Using `range()`

### Print 0 to 4

```python
for i in range(5):
    print(i)
```

Output

```text
0
1
2
3
4
```

---

## Print 1 to 5

```python
for i in range(1,6):
    print(i)
```

---

## Syntax of `range`

```python
range(start,stop,step)
```

Examples:

```python
range(1,6)
```

1 to 5

---

```python
range(2,11,2)
```

2,4,6,8,10

---

## Reverse Loop

```python
for i in range(5,0,-1):
    print(i)
```

Output

```text
5
4
3
2
1
```

---

## Example — Multiplication Table

```python
n=5

for i in range(1,11):
    print(n*i)
```

---

## Traversing a String

```python
for ch in "Python":
    print(ch)
```

---

## Traversing a List

```python
for x in [10,20,30]:
    print(x)
```

---

# 24. `while` Loop Basics

## What is a `while` loop?

Repeats while a condition is true.

Used when repetitions are not known in advance.

---

## Syntax

```python
while condition:
    statements
```

---

## Example

```python
i=1

while i<=5:
    print(i)
    i=i+1
```

---

## Loop Parts

Every while loop needs:

1. Initialization

```python
i=1
```

2. Condition

```python
i<=5
```

3. Update

```python
i=i+1
```

---

## Example — Reverse Counting

```python
n=5

while n>=1:
    print(n)
    n=n-1
```

---

## Infinite Loop (Danger)

Wrong:

```python
i=1

while i<=5:
    print(i)
```

No update.

Runs forever.

---

## Sentinel Example

Read until user enters -1

```python
n=int(input())

while n!=-1:
    print(n)

    n=int(input())
```

---

# 25. Counter-Controlled Loops

## What is a Counter?

A variable that tracks repetition.

Example:

```python
count=0
```

---

## Counter Example

```python
for i in range(5):
    count=count+1

print(count)
```

Output

```text
5
```

---

## Counting Even Numbers

```python
count=0

for i in range(1,11):

    if i%2==0:
        count=count+1

print(count)
```

---

## Counting Digits

```python
n=12345

count=0

while n>0:
    count=count+1
    n=n//10

print(count)
```

---

## Count Positives in List

```python
count=0

for x in [2,-1,5,-3]:

    if x>0:
       count+=1
```

---

## Typical Counter Problems

* Count digits
* Count vowels
* Count factors
* Count even numbers
* Count occurrences

---

# 26. Accumulator Problems

## What is an Accumulator?

A variable that stores a running total.

Example:

```python
sum=0
```

---

## Sum 1 to N

```python
sum=0

for i in range(1,6):
    sum=sum+i

print(sum)
```

Output

```text
15
```

---

## Product Accumulator (Factorial)

```python
fact=1

for i in range(1,6):
    fact=fact*i

print(fact)
```

Output

```text
120
```

---

## Sum of Even Numbers

```python
total=0

for i in range(1,11):

    if i%2==0:
        total+=i

print(total)
```

---

## Average Using Accumulator

Average = \frac{Total}{Count}

```python
total=0

for i in range(5):
    x=int(input())
    total+=x

avg=total/5
```

---

## Accumulator Pattern

Initialize

```python
total=0
```

Update

```python
total=total+value
```

---

# 27. Number Processing Problems

Processing digits or numeric properties.

---

## Sum of Digits

Example:

123

Calculation

1+2+3=6

```python
n=123
sum=0

while n>0:

    digit=n%10

    sum+=digit

    n=n//10

print(sum)
```

---

## Reverse Number

123

Becomes

321

```python
n=123
rev=0

while n>0:

    digit=n%10

    rev=rev*10+digit

    n=n//10

print(rev)
```

---

## Palindrome Number

121

Reverse equals original.

```python
orig=n

# reverse logic

if orig==rev:
   print("Palindrome")
```

---

## Find Factors

```python
n=12

for i in range(1,n+1):

   if n%i==0:
      print(i)
```

---

## Prime Check

```python
count=0

for i in range(1,n+1):

   if n%i==0:
      count+=1

if count==2:
   print("Prime")
```

---

## Fibonacci Series

```python
a=0
b=1

for i in range(5):

   print(a)

   c=a+b
   a=b
   b=c
```

---

## Common Number Problems

* Factorial
* Prime
* Fibonacci
* Sum digits
* Reverse number
* Palindrome

---

# 28. Iterative Problem Solving

## What is Iteration?

Solving a problem by repeated steps.

Repeat until goal achieved.

---

## Problem Solving Pattern

1. Initialize variables

```python
sum=0
```

---

2. Repeat

```python
for ...
```

or

```python
while ...
```

---

3. Update

```python
sum+=i
```

---

4. Stop condition

```python
i<=n
```

---

## Example — Find Largest of N Numbers

```python
largest=-9999

for i in range(5):

   x=int(input())

   if x>largest:
      largest=x

print(largest)
```

Repeated improvement.

---

## Example — Guessing Game

```python
secret=7

guess=0

while guess!=secret:

   guess=int(input())
```

Stops when condition met.

---

## Iterative Thinking Used In

* Searching
* Sorting
* Simulation
* Optimization
* Repeated approximation

---

## Loop Control Statements

## break

Stops loop.

```python
for i in range(10):

   if i==5:
      break

   print(i)
```

---

## continue

Skips one iteration.

```python
for i in range(5):

   if i==2:
      continue

   print(i)
```

---

# Common Mistakes

## Forget Update

Wrong

```python
while i<=5:
   print(i)
```

Infinite loop.

---

## Wrong Accumulator Start

Wrong for factorial:

```python
fact=0
```

Correct

```python
fact=1
```

---

## Off by One Error

Wrong

```python
range(1,5)
```

Gives 1 to 4

Not 1 to 5.

Correct

```python
range(1,6)
```

---

# Practice Problems

### `for`

1. Print 1 to N
2. Multiplication table
3. Print even numbers

---

### `while`

4. Reverse counting
5. Read until -1
6. Guessing game

---

### Counter

7. Count digits
8. Count factors
9. Count vowels

---

### Accumulator

10. Sum numbers
11. Factorial
12. Average marks

---

### Number Processing

13. Prime
14. Fibonacci
15. Palindrome

---

# Summary

## Core Loop Structures

```python
for
```

```python
while
```

---

## Core Patterns

Counter:

```python
count+=1
```

Accumulator:

```python
total+=value
```

---

## Thinking Skills Used

* Iteration
* Repetition
* Counting
* Number Processing
* Step-by-step refinement

---

## Loop Problem Formula

For every looping problem ask:

1. What repeats?
2. How many times?
3. Use `for` or `while`?
4. Need counter or accumulator?
5. What updates each iteration?
6. When should loop stop?

That is the foundation of iterative programming.
