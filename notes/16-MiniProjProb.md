# Mini Real-World Programs — Notes

These combine multiple concepts:

* Input/Output
* Conditions
* Loops
* Functions
* Lists/Dictionaries
* Problem decomposition

These are small applications, not just isolated coding exercises.

---

# 77. Student Grade Calculator

## Problem Idea

Given student marks:

* Calculate total
* Calculate average
* Assign grade
* Display result

---

## Inputs

* Student name
* Marks in subjects

Example:

```text
Math = 80
Science = 75
English = 90
```

---

## Step 1 — Total

Total = m_1+m_2+m_3

```python id="sg1"
total=math+science+english
```

---

## Step 2 — Average

Average=\frac{Total}{3}

```python id="sg2"
avg=total/3
```

---

## Step 3 — Grade Decision

Example rule:

* 90+ → A
* 80+ → B
* 70+ → C
* Else Fail

```python id="sg3"
if avg>=90:
   grade="A"

elif avg>=80:
   grade="B"

else:
   grade="C"
```

---

## Step 4 — Output Report

```text
Name: Raj
Total:245
Average:81.6
Grade:B
```

---

## Decomposition

Functions:

```python id="sg4"
find_total()
```

```python id="sg5"
find_average()
```

```python id="sg6"
find_grade()
```

---

## Extensions

Can add:

* Highest subject mark
* Pass/fail per subject
* Class rank

---

## Skills Used

* Sequence
* Selection
* Aggregation
* Decomposition

---

# 78. Billing System

## Problem Idea

Calculate bill for purchased items.

---

## Inputs

Example:

```text
Pen   10 × 2
Book  50 × 1
```

---

## Item Total

Formula

ItemTotal=Price\times Quantity

---

## Total Bill

```python id="bs1"
bill=0

bill += price*qty
```

Accumulator.

---

## Tax

Example:

10%

Final=Bill+Tax

---

```python id="bs2"
tax=bill*0.10

final=bill+tax
```

---

## Discount (Optional)

```python
if bill>500:
   discount=50
```

---

## Output

```text
Subtotal:300
Tax:30
Final:330
```

---

## Multi-Item Loop

```python id="bs3"
for i in range(n):

   price=int(input())
   qty=int(input())

   bill+=price*qty
```

---

## Skills Used

* Accumulator
* Looping
* Financial calculation
* Conditional discount

---

# 79. ATM Simulation

## Problem Idea

Simulate banking actions.

Options:

1 Deposit

2 Withdraw

3 Check Balance

4 Exit

---

## Balance Variable

```python id="atm1"
balance=1000
```

State variable.

---

## Deposit

```python id="atm2"
amount=int(input())

balance+=amount
```

---

## Withdraw

```python id="atm3"
if amount<=balance:

   balance-=amount
```

---

## Menu Loop

```python id="atm4"
while True:

   choice=int(input())

   if choice==4:
      break
```

---

## Simple Menu

```text
1 Deposit
2 Withdraw
3 Balance
4 Exit
```

---

## State Changes

Deposit:

Balance increases.

Withdraw:

Balance decreases.

Simulation means state changes over time.

---

## Decomposition

Functions:

```python id="atm5"
deposit()
```

```python id="atm6"
withdraw()
```

```python id="atm7"
check_balance()
```

---

## Skills Used

* Simulation
* State management
* Loops
* Decisions
* Decomposition

---

# 80. Library Fine Calculator

## Problem Idea

Calculate overdue fine.

Inputs:

* Due days
* Returned days
* Fine rule

---

## Days Late

LateDays=Returned-Due

---

```python id="lf1"
late=returned-due
```

---

## Fine Rule Example

If late <=5

₹2/day

If late <=10

₹5/day

Else

₹10/day

---

```python id="lf2"
if late<=5:
   fine=late*2

elif late<=10:
   fine=late*5

else:
   fine=late*10
```

---

## Output

```text
Late Days:7
Fine:35
```

---

## Possible Extensions

Add:

* Lost book penalty
* Membership type rules
* Max fine cap

---

## Skills Used

* Sequence
* Selection
* Formula problems

---

# 81. Small Project Problem Solving

## What is a Small Project?

Combining multiple subproblems into a mini application.

---

## General Project Pattern

Input

↓

Validation

↓

Processing

↓

Output

---

## Example Projects

### 1. Student Management Mini App

Store:

* Name
* Marks
* Grade

Operations:

* Add student
* Search student
* Show topper

---

## 2. Grocery Billing App

* Add products
* Compute bill
* Apply tax
* Print invoice

---

## 3. Simple Bank App

* Deposit
* Withdraw
* Balance

---

## 4. Quiz Program

* Ask questions
* Check answers
* Compute score

---

## 5. Expense Tracker

Store expenses.

Compute total.

Show categories.

---

## Project Decomposition Template

Break into modules:

```python id="pr1"
input_data()
```

```python id="pr2"
validate()
```

```python id="pr3"
process()
```

```python id="pr4"
display()
```

---

## Example Workflow

ATM

```text
Menu
↓
Choose action
↓
Update balance
↓
Repeat
```

---

## Design Questions Before Coding

Ask:

1. What data is needed?
2. What operations exist?
3. What rules apply?
4. What outputs needed?
5. Can problem be split into functions?

---

# Common Beginner Mistakes

## One Giant Program

Wrong:

Everything in one huge block.

Better:

Use functions.

---

## No Input Validation

Wrong:

Negative withdrawal accepted.

Check:

```python
if amount>0:
```

---

## No State Tracking

ATM without balance variable.

Wrong simulation.

---

## Hardcoding Values

Wrong

```python
marks=80
```

Use input.

---

# Practice Mini Projects

1. Student Grade Calculator
2. Billing System
3. ATM Simulator
4. Library Fine Calculator
5. Grocery Invoice Generator
6. Quiz App
7. Expense Tracker

---

# Summary

## Core Real-World Patterns

### Formula-based

Grade, fine, bill

---

### State-based

ATM

```python id="sum1"
balance
```

---

### Menu-driven

```python id="sum2"
while True
```

---

### Decomposition

```python id="sum3"
functions
```

---

## Thinking Skills Used

* Decomposition
* Simulation
* Selection
* Iteration
* Data modeling

---

## Real-World Problem Formula

For every mini project ask:

1. What data (inputs)?
2. What rules?
3. What state changes?
4. What repeated menu/actions?
5. What functions break problem apart?

That is the foundation of mini real-world programming.
