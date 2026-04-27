# Conditional Statements — Notes

## What is a Conditional Statement?

A conditional statement lets a program make decisions.

It asks:

**If a condition is true, do one thing; otherwise do something else.**

Examples:

* If marks ≥ 50 → Pass
* If age ≥ 18 → Can vote
* If number % 2 == 0 → Even

---

## Comparison Operators

| Operator | Meaning               |
| -------- | --------------------- |
| ==       | Equal to              |
| !=       | Not equal to          |
| >        | Greater than          |
| <        | Less than             |
| >=       | Greater than or equal |
| <=       | Less than or equal    |

Example:

```python
x=10

print(x>5)
```

Output:

```text
True
```

---

## Logical Operators

| Operator | Meaning              |
| -------- | -------------------- |
| and      | Both conditions true |
| or       | At least one true    |
| not      | Reverses condition   |

Example:

```python
age=20
citizen=True

if age>=18 and citizen:
    print("Eligible")
```

---

# 18. `if` Statement Problems

## Syntax

```python
if condition:
    statements
```

---

## Example 1 — Positive Number

```python
n=int(input())

if n>0:
    print("Positive")
```

If condition is false, nothing happens.

---

## Example 2 — Eligible to Vote

```python
age=int(input())

if age>=18:
    print("Can Vote")
```

---

## Example 3 — Divisible by 5

```python
n=int(input())

if n%5==0:
    print("Divisible")
```

---

## Flow

Start
↓
Read Input
↓
Check Condition
↓
If True → Execute
↓
Stop

---

## Common `if` Problems

* Check positive number
* Check even number
* Check divisibility
* Check passing marks

---

# 19. `if-else` Problems

Used when there are two choices.

## Syntax

```python
if condition:
    statements
else:
    statements
```

---

## Example 1 — Even or Odd

```python
n=int(input())

if n%2==0:
    print("Even")
else:
    print("Odd")
```

---

## Example 2 — Pass or Fail

```python
marks=int(input())

if marks>=50:
    print("Pass")
else:
    print("Fail")
```

---

## Example 3 — Larger of Two Numbers

```python
a=int(input())
b=int(input())

if a>b:
    print(a)
else:
    print(b)
```

---

## Decision Structure

Condition ?

Yes → Block 1
No → Block 2

---

## Typical Problems

* Even/Odd
* Pass/Fail
* Profit/Loss
* Positive/Negative

---

# 20. `if-elif-else` Ladder Problems

Used when there are multiple choices.

## Syntax

```python
if condition1:
    statements

elif condition2:
    statements

elif condition3:
    statements

else:
    statements
```

---

## Example — Grade System

```python
marks=int(input())

if marks>=90:
    print("A")

elif marks>=80:
    print("B")

elif marks>=70:
    print("C")

else:
    print("Fail")
```

---

## Flow

Check first condition.

If false, check next.

Stops at first true condition.

---

## Example — Day Number

```python
n=int(input())

if n==1:
    print("Monday")

elif n==2:
    print("Tuesday")

else:
    print("Invalid")
```

---

## Example — Electricity Bill (Simple Slabs)

```python
units=int(input())

if units<=100:
    bill=units*2

elif units<=300:
    bill=units*3

else:
    bill=units*5

print(bill)
```

---

## Common Ladder Problems

* Grade system
* Tax slabs
* Electricity billing
* Menu choices
* Age category

---

## Important Order Matters

Wrong:

```python
if marks>=50:
   print("Pass")

elif marks>=90:
   print("A")
```

90 will never reach second condition.

---

Correct:

```python
if marks>=90:
   print("A")

elif marks>=50:
   print("Pass")
```

---

# 21. Nested Conditions

Condition inside another condition.

## Syntax

```python
if condition1:

    if condition2:
        statements
```

---

## Example — Vote and Senior Citizen

```python
age=int(input())

if age>=18:

    if age>=60:
        print("Senior Citizen")

    else:
        print("Adult")

else:
    print("Not Eligible")
```

---

## Example — Login Check

```python
username=input()
password=input()

if username=="admin":

    if password=="1234":
        print("Login Success")

    else:
        print("Wrong Password")

else:
    print("Wrong User")
```

---

## Example — Largest of Three

```python
a,b,c=map(int,input().split())

if a>b:

    if a>c:
        print(a)

else:

    if b>c:
        print(b)
    else:
        print(c)
```

---

## Use Nested Conditions When:

* One decision depends on another
* Multi-level checking required
* Hierarchical rules exist

---

# 22. Decision-Making Problem Solving

This is applying conditions to solve real problems.

---

## Decision-Making Process

1. Understand rule
2. Convert rule into condition
3. Use if/elif/else
4. Test all cases

---

## Example Problem

Check Leap Year

Rule:

A year is leap if:

* Divisible by 400
  OR

* Divisible by 4 but not by 100

Condition:

```python
if year%400==0 or (year%4==0 and year%100!=0):
```

---

## Full Program

```python
year=int(input())

if year%400==0 or (year%4==0 and year%100!=0):
    print("Leap")

else:
    print("Not Leap")
```

---

## Example — Triangle Validity

A triangle is valid if:

a+b>c

and

a+c>b

and

b+c>a

```python
if a+b>c and a+c>b and b+c>a:
    print("Valid")
```

---

## Real-World Decision Problems

* Grading system
* Bank eligibility
* Ticket pricing
* Tax slabs
* Admission rules
* Discount eligibility

---

# Common Beginner Mistakes

## Using = Instead of ==

Wrong

```python
if x=5:
```

Correct

```python
if x==5:
```

---

## Missing Colon

Wrong

```python
if x>5
```

Correct

```python
if x>5:
```

---

## Indentation Error

Wrong

```python
if x>5:
print("Yes")
```

Correct

```python
if x>5:
    print("Yes")
```

---

## Wrong Logical Operator

Wrong

```python
if age>=18 or citizen:
```

May allow incorrect cases.

Correct

```python
if age>=18 and citizen:
```

---

# Practice Problems

### `if`

1. Check positive number
2. Check divisible by 7
3. Check pass mark

---

### `if-else`

4. Even or odd
5. Larger of two numbers
6. Profit or loss

---

### `if-elif-else`

7. Grade calculator
8. Tax slab
9. Electricity bill

---

### Nested

10. Login validation
11. Triangle type
12. Largest of three

---

# Summary

## Decision Structures

```python
if
```

```python
if else
```

```python
if elif else
```

```python
nested if
```

---

## Thinking Skills Used

* Selection
* Decision Making
* Rule Evaluation
* Logical Reasoning

---

## Problem Solving Pattern

For any condition problem ask:

1. What rule decides output?
2. What condition represents rule?
3. Single decision or multiple decisions?
4. Use if / elif / nested if
5. Test all cases

That is the foundation of conditional problem solving.
