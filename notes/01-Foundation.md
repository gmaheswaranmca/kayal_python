# Foundations — Notes

## 1. Introduction to Problem Solving

### What is Problem Solving?

Problem solving is the process of understanding a problem, designing a method to solve it, implementing the solution, and verifying the result.

In programming, problem solving means:

* Understanding what the problem asks
* Finding logical steps to solve it
* Converting those steps into code
* Testing whether the code works correctly

---

### Basic Problem-Solving Steps

1. Understand the problem
2. Identify inputs and outputs
3. Break the problem into smaller steps
4. Design a solution
5. Write the program
6. Test the program
7. Improve if needed

---

### Example

Problem: Find sum of two numbers.

Input:

* Number1
* Number2

Process:

* Add the two numbers

Output:

* Sum

---

### Computational Thinking Skills

Important thinking skills used in programming:

* Decomposition
* Pattern Recognition
* Abstraction
* Algorithm Design

### Example:

Problem: Student Grade System

Break into smaller parts:

* Read marks
* Compute total
* Compute average
* Decide grade
* Display result

This is decomposition.

---

## 2. Problem Analysis (Input → Process → Output)

A simple model for analyzing problems:

## IPO Model

### Input

Data given to the program.

Examples:

* Numbers
* Names
* Marks
* Prices

---

### Process

Operations performed.

Examples:

* Addition
* Comparison
* Sorting
* Decision making

---

### Output

Result produced.

Examples:

* Sum
* Largest value
* Grade
* Sorted list

---

## Example

Problem: Area of Rectangle

Input:

* Length
* Width

Process:
Area = Length × Width

Output:

* Area

---

## Another Example

Problem: Even or Odd

Input:

* Number

Process:
Check Number % 2

Output:

* Even or Odd

---

## 3. Writing Algorithms

### What is an Algorithm?

An algorithm is a step-by-step procedure to solve a problem.

Characteristics of a good algorithm:

* Clear
* Finite
* Correct
* Efficient

---

## Example Algorithm

Problem: Find largest of two numbers

Step 1: Start
Step 2: Read A and B
Step 3: If A > B
Step 4: Print A
Step 5: Else Print B
Step 6: Stop

---

## Another Example

Problem: Find factorial

Step 1: Start
Step 2: Read N
Step 3: Set fact = 1
Step 4: Repeat from 1 to N
Step 5: fact = fact × i
Step 6: Print fact
Step 7: Stop

---

## Types of Algorithm Logic

### Sequence

Steps executed in order.

Example:

* Read number
* Multiply by 2
* Print result

---

### Selection

Decision based logic.

Example:

* If number > 0 print Positive

---

### Iteration

Repeated steps.

Example:

* Print 1 to N

---

## 4. Flowcharts Basics

### What is a Flowchart?

A graphical representation of an algorithm.

Uses symbols to show steps.

---

## Common Symbols

![Image](https://images.openai.com/static-rsc-4/oIY0nmC95AVP0P4aSPK0HURl6CFEjWb3jTn2zx1DMESD2QsFhKc23E0qfdWdwTBIOEeRhVn8SBMrDOMHbvAByPQEgb3iC1rqA4_U13_fkJWq5sGUIijhsJ-UjlCRQACqtt5FhMorhdegIioI4MguISEcRIHiNZurJMCD80PUOtOMH4jY5YNz99GLBXQZ3YJA?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/KoDdpf3m9aULL4dSafxuVELS4lctKeqvvUuvJEWiVGi3cS_ssNleirSjl3Uf3BzpkkFOBjj7AIVWlojhsqS1FW_2yjSeeM1I3kz1arysFJn1om5d0ntyIQXCiLTIACtPsJEn9Bsk6pe7iIASfO4SHCVs-uFwQovztAxj-os15lqwGQEmLEpsUw6bDfCo8lH1?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/0Ct3GoUcKnRYjnRBvlAde3o78az1C3HtK3SqDrCtTTp1O8cRIsH1SNc90cCE0nIaRjW4MdXUYoZ8WWGeUxeFAmaHIMEV1kylQJNSZ9rr2M59pLpYJqSZ62sXjX0oZ61W16whYFEkGDybRHJCNLA2dCa_82eWFEROsBcxSCVfKgDT6bq4OBDdfJKvxLaeiwX8?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/s2HXmN2NGS-k2zKVnttuQBYxp-o6_gWif6dn-BST-YWLuhLAZjkNFvkXEbZID7mDMbuyMJRwG3h8TjwrYye6n6wrNY7b9vJpCmsTDIyfqy0bMSHDzjmb0W6OtuExL1V5qDwgF2SmVbYn4_A5b73AHTjgdx2MRKVKAJKf7qVBkWBmuEzHNSgN9undLx9IL0jo?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/Vmn-IzNy1ajSuHkPv0jg0JvmJuumn3PKjeZMYCnU5icjQnECD7jzeiyEIbBk6apt3G5E9za9zcJsgnVpIYVxtUQMXWZJVdzk11HoWyYj03yvfgx9TkTF0xikVcTIe7sQdbUKI4sl7ofdI_5jhMui0a7yH19EZ2Aw1l9qR3VI3F-KAQghDeWzNwy6PB4pqbDx?purpose=fullsize)

![Image](https://images.openai.com/static-rsc-4/jhc3BjLdqjkcYEiHYvgcIW9C0RZzCne1sw31FY1DU3RaiHZZposoPo6N2-YnCYjK43kDf-vXgrhIQAsWXjRG0CaUoUsbxhdPuY6hOptCPxxZDUi8_5jSkdyNO9p_pq-GeKAczMB2fBYkxPe3WPE7_rwtfUmpSZ5v7408QsaUPJXfJW-vYwQ1s19r10GwsO9C?purpose=fullsize)

* Oval → Start / End
* Parallelogram → Input/Output
* Rectangle → Process
* Diamond → Decision
* Arrow → Flow direction

---

## Example Flowchart Logic

Problem: Even or Odd

Start
↓
Read N
↓
N % 2 == 0 ?
↓ Yes → Print Even
↓ No → Print Odd
↓
Stop

---

## Why Flowcharts?

* Easy to understand
* Visualizes logic
* Helps before coding
* Reduces errors

---

## 5. Pseudocode Basics

### What is Pseudocode?

Pseudocode is an informal way of writing program logic using simple English-like statements.

It is not real code.

---

## Example

Problem: Sum of two numbers

BEGIN
Read A
Read B
Sum = A + B
Print Sum
END

---

## Example

Problem: Find larger number

BEGIN
Read A,B
IF A > B
Print A
ELSE
Print B
END IF
END

---

## Common Pseudocode Words

* BEGIN
* END
* INPUT
* OUTPUT
* IF
* ELSE
* WHILE
* FOR

---

## Difference

| Algorithm | Flowchart | Pseudocode         |
| --------- | --------- | ------------------ |
| Steps     | Diagram   | English-like logic |
| Text form | Visual    | Text form          |
| Planning  | Planning  | Planning           |

---

## 6. Python Syntax Fundamentals

### Basic Python Program

```python
print("Hello")
```

---

## Variables

```python
x = 10
name = "Sam"
```

Rules:

* Cannot start with number
* No spaces
* Case sensitive

---

## Data Types

```python
a = 10        # int
b = 5.5       # float
c = "Python"  # string
d = True      # boolean
```

---

## Input

```python
n = int(input("Enter number: "))
```

---

## Arithmetic Operators

```python
+  addition
-  subtraction
*  multiplication
/  division
%  modulus
```

---

## Conditions

```python
if x > 10:
    print("Large")
```

---

## Loops

```python
for i in range(5):
    print(i)
```

---

## Functions

```python
def add(a,b):
    return a+b
```

---

## Indentation

Python uses indentation instead of braces.

Correct:

```python
if x>5:
    print("Yes")
```

Wrong:

```python
if x>5:
print("Yes")
```

---

## 7. Running and Testing Programs

## Running a Program

Save file:

```python
test.py
```

Run:

```bash
python test.py
```

---

## Ways to Run Python

* Python IDLE
* VS Code
* PyCharm
* Jupyter Notebook
* Online Compiler

---

## Testing Programs

### Dry Run

Manually trace program.

Example:

```python
a=5
b=2
print(a+b)
```

Output:
7

---

## Test Cases

Input:
5 3

Expected Output:
8

---

Input:
10 20

Expected Output:
30

---

## Types of Errors

### Syntax Error

```python
if x>5
```

Missing colon.

---

### Runtime Error

```python
10/0
```

Division by zero.

---

### Logical Error

```python
area = l + w
```

Should be multiplication.

---

## Debugging

Finding and fixing errors.

Methods:

* Print debugging
* Step-by-step tracing
* Test cases
* Using debugger

---

## Foundation Formula for Solving Any Problem

Think:

1. What is input?
2. What process is needed?
3. What is output?
4. Write algorithm
5. Write pseudocode
6. Convert to Python
7. Test with cases

This is the full problem-solving cycle.
