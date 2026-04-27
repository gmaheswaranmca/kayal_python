# Functions — Notes

## What is a Function?

A function is a named block of code that performs a task.

Instead of repeating code:

```python id="q1bn3k"
a=5
b=3
print(a+b)

x=10
y=4
print(x+y)
```

Use a function.

---

## Why Functions?

Functions help:

* Reuse code
* Break big problems into smaller parts
* Reduce repetition
* Improve readability
* Make testing easier

---

## Real-Life Analogy

A function is like a machine.

Input → Processing → Output

Example:

Calculator:

Input:
2,3

Process:
Addition

Output:
5

---

# 57. Defining Functions

## Syntax

```python id="ugvxg6"
def function_name():
    statements
```

---

## Example

```python id="j67d7w"
def hello():
    print("Hello")
```

---

## Calling a Function

```python id="ltj2d0"
hello()
```

Output

```text id="z54pb0"
Hello
```

---

## Function with Multiple Statements

```python id="4hxj07"
def show():

    print("Python")
    print("Programming")
```

---

## Function Can Be Called Many Times

```python id="mkljlwm"
show()
show()
```

---

## Example — Square

```python id="cl3ecv"
def square():

   n=5

   print(n*n)
```

---

## Naming Rules

Use meaningful names.

Good:

```python id="sd3fl7"
find_sum()
```

Bad:

```python id="6m7wy4"
f1()
```

---

## Common Beginner Functions

* add_numbers()
* check_even()
* find_factorial()
* print_pattern()

---

# 58. Parameters and Return Values

## Parameters

Parameters are inputs given to a function.

---

## Example

```python id="4pmksj"
def add(a,b):

   print(a+b)
```

a and b are parameters.

---

## Calling

```python id="dfrg5w"
add(5,3)
```

Output

```text id="b7q06g"
8
```

---

## Arguments

Actual values passed:

```python id="7d0x2p"
5 and 3
```

called arguments.

---

## Return Value

A function can give back a result.

---

## Syntax

```python id="c7l50e"
return value
```

---

## Example

```python id="mjbxg2"
def add(a,b):

   return a+b
```

---

Call:

```python id="it6gr5"
x=add(5,3)

print(x)
```

---

## Difference

### Print inside function

```python id="whp1be"
def add(a,b):
   print(a+b)
```

Displays result.

---

### Return result

```python id="ew10mb"
def add(a,b):
   return a+b
```

Returns value for reuse.

Usually better.

---

## Example — Even Check

```python id="z5gkq8"
def is_even(n):

   return n%2==0
```

---

## Example — Factorial

```python id="rzv3fw"
def factorial(n):

   fact=1

   for i in range(1,n+1):
      fact*=i

   return fact
```

---

## Types of Functions

### No parameters, no return

```python id="y0c1zy"
def show():
```

---

### Parameters, no return

```python id="9bdscs"
def add(a,b):
```

---

### Parameters with return

```python id="c33tln"
def add(a,b):
   return a+b
```

---

# 59. Decomposing Problems Using Functions

## What is Decomposition?

Break a big problem into smaller problems.

---

## Example

Student Report Card

Instead of one huge program:

Break into functions:

* read_marks()
* find_total()
* find_average()
* find_grade()
* display_result()

---

## Example Structure

```python id="ks75f1"
def total(marks):
```

```python id="33lxfj"
def average(total,count):
```

```python id="vls2a2"
def grade(avg):
```

---

## Main Program Calls Pieces

```python id="yxhx0d"
marks=[80,90,70]

t=total(marks)

avg=average(t,3)

g=grade(avg)
```

---

## Example — Prime Check Decomposition

Break into:

* check_prime()
* print_result()

---

## Example

```python id="c7z0br"
def is_prime(n):
```

Reusable helper.

---

## ATM Example

Break into:

* check_balance()
* deposit()
* withdraw()
* menu()

---

## Benefits

* Easier to understand
* Easier debug
* Easier test
* Easier reuse

---

# 60. Reusable Problem-Solving Patterns

These are common function patterns used repeatedly.

---

## Pattern 1 — Calculator Function

```python id="ksql4v"
def add(a,b):
    return a+b
```

Reusable.

---

## Pattern 2 — Validator Function

Checks condition.

```python id="3d9u7v"
def is_even(n):
    return n%2==0
```

---

## Pattern 3 — Search Function

```python id="feuv1m"
def linear_search(arr,key):
```

Reusable.

---

## Pattern 4 — Aggregation Function

```python id="xphwul"
def find_sum(arr):
```

---

## Pattern 5 — Transformation Function

```python id="rzq3pc"
def square_list(arr):
```

---

## Pattern 6 — Utility Helper Function

GCD helper.

```python id="q1fqgk"
def gcd(a,b):
```

Used in many problems.

---

## Pattern 7 — Input → Process → Return

General model:

```python id="nhwxqj"
def solve(input):

   process

   return result
```

---

## Example Reuse

One prime function:

```python id="xvws44"
def is_prime(n):
```

can be used for:

* Check one prime
* Count primes
* Print primes in range

Reuse.

---

## Example — Formula Function

Simple Interest

SI=\frac{PRT}{100}

```python id="2mbrjh"
def simple_interest(p,r,t):

   return (p*r*t)/100
```

Reusable.

---

## Example — Temperature Converter

F=\frac95C+32

```python id="2f2tcc"
def c_to_f(c):
```

---

# Variable Scope (Important)

## Local Variable

Inside function only.

```python id="k5n1lt"
def test():

   x=5
```

x exists only inside.

---

## Global Variable

Outside function.

```python id="q6yecj"
x=10
```

---

## Example

```python id="zjlwm3"
def show():

   a=5

print(a)
```

Error.

a local only.

---

# Common Mistakes

## Forget Calling Function

Wrong

```python id="nn0dhk"
def hello():
   print("Hi")
```

Nothing runs.

Need:

```python id="fjlwmn"
hello()
```

---

## Forget Return

Wrong

```python id="byl5xd"
def add(a,b):

   a+b
```

No returned value.

---

## Wrong Parameters

Wrong

```python id="0lzq1e"
add(5)
```

Missing parameter.

---

## Confusing Print vs Return

```python id="5jlwmq"
print()
```

Displays.

```python id="yw9g1q"
return
```

Sends value back.

Different.

---

# Practice Problems

## Defining Functions

1. Create hello()
2. Create square()
3. Create multiplication table function

---

## Parameters/Return

4. Add two numbers
5. Check even
6. Find factorial

---

## Decomposition

7. Student grading system
8. ATM menu
9. Prime checker with helper functions

---

## Reusable Patterns

10. GCD function
11. Search function
12. Sum list function

---

# Summary

## Core Syntax

Define

```python id="uw88c4"
def name():
```

---

Parameter

```python id="fxvpkq"
def add(a,b):
```

---

Return

```python id="e3ejgc"
return value
```

---

Call

```python id="lljlwm"
add(5,3)
```

---

## Core Problem Types

* Calculator functions
* Validation functions
* Search functions
* Utility helper functions

---

## Thinking Skills Used

* Decomposition
* Abstraction
* Reuse
* Modular thinking

---

## Function Problem Formula

For every function problem ask:

1. What task should function do?
2. What inputs (parameters)?
3. What output (return)?
4. Can problem be split into smaller functions?
5. Can function be reused elsewhere?

That is the foundation of functional problem solving.
