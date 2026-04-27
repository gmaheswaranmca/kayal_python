# Recursion (Intro) — Notes

## What is Recursion?

Recursion is when a function calls itself to solve a problem.

Instead of solving everything at once:

* Solve a smaller version of the problem
* Keep reducing it
* Stop at a simple case

---

## Big Idea

Problem:

Solve **n**

Reduce to:

Solve **n-1**

---

## General Form

```python id="5b9j4p"
def func(n):

   if stopping_condition:
      return answer

   return func(smaller_problem)
```

---

## Recursion has two essential parts:

1. Base Case
2. Recursive Case

Without both, recursion fails.

---

# 61. Recursive Thinking

## What is Recursive Thinking?

Think:

“How can I reduce this problem into a smaller version of itself?”

---

## Example — Counting Down

Print:

5 4 3 2 1

---

Iterative:

```python id="zn52rv"
for i in range(5,0,-1):
   print(i)
```

---

Recursive idea:

Print 5

Then solve:

Print 4..1

Smaller same problem.

---

Code

```python id="5jlxy7"
def countdown(n):

   if n==0:
      return

   print(n)

   countdown(n-1)
```

---

Call

```python id="rz6m4g"
countdown(5)
```

---

## Recursive Thought Pattern

Ask:

Can problem of size n become size n-1 ?

---

## Example — Sum of N Numbers

We know:

Sum(n)=n+Sum(n-1)

This is recursive thinking.

---

## Example

For 5

```text id="7d6yq5"
5 + Sum(4)
```

Then

```text id="b85lwd"
5 + 4 + Sum(3)
```

Continue.

---

## Recursion uses:

* Reduction
* Self-reference
* Repeated smaller solving

---

# 62. Base Case and Recursive Case

## Base Case

Stopping condition.

Without it:

Infinite recursion.

---

## Example

```python id="jlwmn1"
if n==0:
   return
```

Stop.

---

## Recursive Case

Problem reduced.

```python id="jlwmn2"
countdown(n-1)
```

---

## Structure

```python id="jlwmn3"
def solve(n):

   if simple_case:
      return

   return solve(smaller_case)
```

---

## Example — Factorial

Math definition:

n!=n(n-1)!

---

Base case:

0!=1

---

Code

```python id="7g8hlv"
def fact(n):

   if n==0:
      return 1

   return n*fact(n-1)
```

---

Example:

```text id="xk0j5n"
fact(4)
```

Becomes

```text id="q62hdw"
4*fact(3)
```

```text id="pxm3yq"
4*3*fact(2)
```

```text id="m9b81h"
4*3*2*fact(1)
```

```text id="zfg2qy"
4*3*2*1
```

---

Result:

24

---

## Two Common Errors

### Missing Base Case

Wrong

```python id="jlwmn4"
def f(n):
   return f(n-1)
```

Never stops.

---

### Not Making Progress

Wrong

```python id="jlwmn5"
f(n)
```

Problem size unchanged.

Must reduce.

---

## Rule

Each call must move toward base case.

---

# Recursion Call Stack (Concept)

Function calls wait in stack.

Example:

```text id="jlwmn6"
fact(3)
```

Calls:

```text id="jlwmn7"
fact(3)
fact(2)
fact(1)
fact(0)
```

Then returns back upward.

This is unwinding.

---

# 63. Classic Recursive Problems

## 1. Factorial

n!=n(n-1)!

```python id="jlwmn8"
def fact(n):

   if n==0:
      return 1

   return n*fact(n-1)
```

---

## 2. Sum of First N Numbers

Formula:

Sum(n)=n+Sum(n-1)

```python id="jlwmn9"
def total(n):

   if n==1:
      return 1

   return n+total(n-1)
```

---

## 3. Fibonacci

Definition:

F(n)=F(n-1)+F(n-2)

---

Base:

F(0)=0, F(1)=1

---

Code

```python id="jlwmn10"
def fib(n):

   if n<=1:
      return n

   return fib(n-1)+fib(n-2)
```

---

## 4. Reverse String

Idea:

Reverse smaller substring.

```python id="jlwmn11"
def rev(s):

   if len(s)==0:
      return ""

   return rev(s[1:])+s[0]
```

---

## 5. Sum of Digits

Example:

123

Think:

123\to 3+Sum(12)

---

Code

```python id="jlwmn12"
def digit_sum(n):

   if n==0:
      return 0

   return n%10 + digit_sum(n//10)
```

---

## 6. Power

a^n=a\cdot a^{n-1}

```python id="jlwmn13"
def power(a,n):

   if n==0:
      return 1

   return a*power(a,n-1)
```

---

## Common Recursive Problems

* Factorial
* Fibonacci
* Sum of digits
* Reverse string
* Power
* Palindrome check

---

# Recursion vs Loop

| Problem   | Loop | Recursion |
| --------- | ---- | --------- |
| Factorial | Yes  | Yes       |
| Sum 1..n  | Yes  | Yes       |
| Fibonacci | Yes  | Yes       |

Both possible.

---

## When Recursion Feels Natural

Use recursion when problem naturally breaks into smaller similar subproblems.

Examples:

* Tree traversal
* Maze paths
* Backtracking
* Divide-and-conquer

(Advanced later)

---

# Common Mistakes

## Infinite Recursion

```python id="jlwmn14"
f(n):
  return f(n)
```

Never reduces.

---

## Wrong Base Case

Wrong

```python id="jlwmn15"
if n==2:
```

May miss other cases.

---

## Forget Return

Wrong

```python id="jlwmn16"
fact(n-1)
```

Need:

```python id="jlwmn17"
return n*fact(n-1)
```

---

## Too Many Calls (Fibonacci)

Basic recursive Fibonacci repeats work.

Can be slow.

(Optimization comes later.)

---

# Recursive Design Formula

For every recursion problem ask:

1. What is the smallest simple case? (Base case)

2. How can problem size reduce?

3. What recursive rule connects them?

General form:

Problem(n)=CurrentWork+Problem(smaller)

---

# Practice Problems

## Beginner

1. Countdown recursively
2. Sum 1..n
3. Factorial

---

## Intermediate

4. Fibonacci
5. Sum digits
6. Reverse string

---

## Challenge

7. Recursive palindrome
8. Power function
9. Count digits recursively

---

# Summary

## Core Structure

```python id="jlwmn18"
def solve(n):

   if base_case:
      return simple_answer

   return recursive_rule
```

---

## Core Concepts

* Recursive thinking
* Base case
* Recursive case
* Call stack
* Problem reduction

---

## Thinking Skills Used

* Decomposition
* Self-reference
* Pattern recognition
* Mathematical reasoning

---

## Golden Rule of Recursion

Every recursive solution must have:

✔ A base case

✔ A smaller recursive call

✔ Progress toward stopping

That is the foundation of recursion.
