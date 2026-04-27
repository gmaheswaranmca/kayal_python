# Arithmetic Problems — Notes

# 13. Operators in Python

## What is an Operator?

An operator is a symbol used to perform operations on values (operands).

Example:

```python
5 + 3
```

* 5 and 3 → operands
* * → operator

---

## Arithmetic Operators

| Operator | Meaning        | Example | Result |
| -------- | -------------- | ------- | ------ |
| +        | Addition       | 5+2     | 7      |
| -        | Subtraction    | 5-2     | 3      |
| *        | Multiplication | 5*2     | 10     |
| /        | Division       | 5/2     | 2.5    |
| //       | Floor Division | 5//2    | 2      |
| %        | Modulus        | 5%2     | 1      |
| **       | Power          | 5**2    | 25     |

---

## Examples

### Addition

```python
a=10
b=20

print(a+b)
```

---

### Modulus (Remainder)

```python
print(17%5)
```

Output:

```text
2
```

Used in:

* Even/Odd checks
* Divisibility problems

---

### Exponent

```python
print(2**4)
```

Output:

```text
16
```

---

## Assignment Operators

```python
x=5
x+=3
```

Equivalent:

```python
x=x+3
```

Common ones:

* +=
* -=
* *=
* /=

---

## Operator Precedence

Python follows order of operations.

PEMDAS:

1. Parentheses
2. Exponents
3. Multiplication/Division
4. Addition/Subtraction

Example:

```python
2+3*4
```

Result:

```text
14
```

---

With parentheses:

```python
(2+3)*4
```

Result:

```text
20
```

---

# 14. Mathematical Expressions

## What is an Expression?

Combination of:

* Variables
* Constants
* Operators

Example:

```python
a+b*c
```

---

## Formula Expressions

Area of Rectangle

A = l \times w

Python:

```python
area=l*w
```

---

## Expression Examples

### Average

Average = \frac{a+b+c}{3}

```python
avg=(a+b+c)/3
```

---

### Simple Interest

SI = \frac{PRT}{100}

```python
si=(p*r*t)/100
```

---

## Using Parentheses

Good:

```python
avg=(a+b+c)/3
```

Bad:

```python
avg=a+b+c/3
```

Wrong due to precedence.

---

## Expression Evaluation

```python
x=5
y=3

z=x*y+2
```

Calculation:

```text
5×3 +2 =17
```

---

## Common Mathematical Functions

```python
import math
```

Examples:

```python
math.sqrt(25)
```

```python
math.pow(2,3)
```

```python
math.ceil(4.2)
```

```python
math.floor(4.8)
```

---

# 15. Solving Formula-Based Problems

## Formula Problem Strategy

1. Identify formula
2. Read inputs
3. Substitute values
4. Compute result
5. Print output

---

## Problem 1 — Area of Circle

Formula:

genui{"math_block_widget_always_prefetch_v2":{"content":"A = \pi r^2"}}

```python
r=float(input())

area=3.14*r*r

print(area)
```

---

## Problem 2 — Perimeter of Rectangle

P = 2(l+w)

```python
p=2*(l+w)
```

---

## Problem 3 — Speed

Speed = \frac{Distance}{Time}

```python
speed=d/t
```

---

## Problem 4 — BMI

BMI = \frac{Weight}{Height^2}

```python
bmi=w/(h*h)
```

---

## Problem 5 — Volume of Cube

genui{"math_block_widget_always_prefetch_v2":{"content":"V = a^3"}}

```python
volume=a**3
```

---

## Common Formula Problems

* Area
* Perimeter
* Speed
* Distance
* Time
* Interest
* Temperature
* Volume

---

# 16. Unit Conversion Problems

## What is Unit Conversion?

Changing value from one measurement unit to another.

Examples:

* km to m
* Celsius to Fahrenheit
* Hours to Minutes

---

## Length Conversion

1 km = 1000 m

```python
km=float(input())

m=km*1000

print(m)
```

---

## Time Conversion

1 hour = 60 minutes

```python
hours=2

minutes=hours*60
```

---

## Temperature Conversion

F = \frac{9}{5}C+32

---

## Sample Interactive Converter

(You can explore more conversions.)

---

## Weight Conversion

1 kg = 1000 g

```python
grams=kg*1000
```

---

## Common Conversion Problems

* cm → m
* m → km
* kg → grams
* hours → seconds
* liters → milliliters
* Celsius → Fahrenheit

---

## Example

Convert minutes to seconds

```python
minutes=int(input())

seconds=minutes*60

print(seconds)
```

---

# 17. Financial Calculations Problems

## Simple Interest

Formula:

SI = \frac{PRT}{100}

Where:

* P = Principal
* R = Rate
* T = Time

```python
si=(p*r*t)/100
```

---

## Amount

A = P + SI

---

## Compound Interest

Formula:

A = P\left(1+\frac{R}{100}\right)^T

Interest:

```text
CI = A-P
```

---

Python:

```python
amount=p*(1+r/100)**t

ci=amount-p
```

---

## Discount

Formula:

Discount = \frac{Rate \times Price}{100}

Final price:

```text
Price - Discount
```

---

## Profit and Loss

Profit:

Profit = SP-CP

Loss:

Loss = CP-SP

---

## Tax Calculation

```python
tax=income*0.10
```

---

## Total Bill with Tax

```python
total=price+(price*tax/100)
```

---

## EMI (Simple Intro)

EMI = \frac{Loan}{Months}

(Simple beginner version)

---

## Example Program

```python
p=1000
r=5
t=2

si=(p*r*t)/100

print(si)
```

Output

```text
100
```

---

# Common Mistakes

## Wrong Formula

Wrong:

```python
si=p+r+t/100
```

---

Correct:

```python
si=(p*r*t)/100
```

---

## Missing Parentheses

Wrong

```python
avg=a+b+c/3
```

---

Correct

```python
avg=(a+b+c)/3
```

---

## Using Integer Division Accidentally

```python
5//2
```

Gives:

```text
2
```

Not 2.5

---

# Problem Solving Pattern for Arithmetic Problems

1. Identify formula
2. Read values
3. Substitute into expression
4. Use operators correctly
5. Print result
6. Verify with sample values

---

# Summary

## Core Operators

```python
+  -  *  /  //  %  **
```

---

## Core Problem Types

* Formula problems
* Unit conversions
* Financial calculations
* Expression evaluation

---

## Core Thinking Skills

* Sequence
* Arithmetic reasoning
* Formula application
* Computational accuracy
