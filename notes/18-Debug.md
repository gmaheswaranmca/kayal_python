# Debugging Challenges — Notes

## What is Debugging?

Debugging means finding and fixing mistakes (bugs) in a program.

A bug is an error that causes:

* Program won’t run
* Program crashes
* Wrong output

---

## Main Types of Errors

1. Syntax Errors
2. Logical Errors
3. Runtime Errors

Also:

4. Output Prediction Problems (used to train debugging thinking)

---

# 85. Syntax Errors

## What is a Syntax Error?

Breaking Python grammar rules.

Like writing incorrect English grammar.

Program usually will not run.

---

## Example — Missing Colon

Wrong

```python id="d1"
if x>5
   print("Yes")
```

Problem:

Missing:

```python id="d2"
:
```

Correct

```python id="d3"
if x>5:
   print("Yes")
```

---

## Example — Missing Parenthesis

Wrong

```python id="d4"
print("Hello"
```

Correct

```python id="d5"
print("Hello")
```

---

## Example — Indentation Error

Wrong

```python id="d6"
if x>5:
print("Yes")
```

Correct

```python id="d7"
if x>5:
   print("Yes")
```

---

## Example — Assignment Instead of Comparison

Wrong

```python id="d8"
if x=5:
```

Correct

```python id="d9"
if x==5:
```

---

## Common Syntax Errors

* Missing colon
* Missing bracket
* Wrong indentation
* Misspelled keyword

Wrong

```python id="d10"
whlie x<5:
```

Should be:

```python id="d11"
while
```

---

## How to Fix Syntax Errors

1. Read error message
2. Check line number
3. Check previous line too
4. Verify punctuation
5. Verify indentation

---

# 86. Logical Errors

## What is a Logical Error?

Program runs…

But gives wrong answer.

Most dangerous error.

---

## Example

Area of rectangle:

Wrong

```python id="d12"
area=l+w
```

Should be:

```python id="d13"
area=l*w
```

Program runs.

But wrong result.

---

## Example — Wrong Average

Wrong

```python id="d14"
avg=a+b+c/3
```

Due to precedence.

Correct

```python id="d15"
avg=(a+b+c)/3
```

---

## Example — Wrong Condition

Wrong

```python id="d16"
if marks>50:
```

If 50 should pass, use:

```python id="d17"
if marks>=50:
```

---

## Example — Off-by-One

Wrong

```python id="d18"
range(1,5)
```

Gives 1..4

If need 1..5:

```python id="d19"
range(1,6)
```

---

## Common Logical Errors

* Wrong formula
* Wrong comparison
* Wrong loop bounds
* Wrong variable update
* Wrong algorithm

---

## Finding Logical Errors

Use:

### Dry Run

Trace manually.

---

### Print Debugging

```python id="d20"
print(total)
```

Check variable values.

---

### Test Cases

Use known answers.

---

# 87. Runtime Errors

## What is Runtime Error?

Program starts…

Then crashes while running.

---

## Example — Division by Zero

Wrong

```python id="d21"
10/0
```

Crash.

---

## Example — Index Out of Range

Wrong

```python id="d22"
a=[1,2]

print(a[5])
```

No element 5.

---

## Example — Undefined Variable

Wrong

```python id="d23"
print(x)
```

x not defined.

---

## Example — Invalid Conversion

Wrong

```python id="d24"
int("abc")
```

Cannot convert.

---

## Example — File Not Found

```python id="d25"
open("missing.txt")
```

---

## Common Runtime Errors

* Division by zero
* Index errors
* Type errors
* Name errors
* File errors

---

## Preventing Runtime Errors

Check before risky operation.

Example

```python id="d26"
if b!=0:
   print(a/b)
```

---

Check index:

```python id="d27"
if i<len(arr):
```

---

Validate input:

```python id="d28"
if s.isdigit():
```

---

## Exception Handling (Intro)

```python id="d29"
try:

   x=10/0

except:

   print("Error")
```

---

# 88. Output Prediction Problems

## What are Output Prediction Problems?

Given code…

Predict output without running.

Excellent debugging training.

---

## Example

```python id="d30"
x=5
y=2

print(x+y)
```

Output?

Answer:

7

---

## Example

```python id="d31"
for i in range(3):
   print(i)
```

Output

```text id="d32"
0
1
2
```

---

## Example

```python id="d33"
x=5

if x>3:
   print("A")
else:
   print("B")
```

Output:

A

---

## Example — Tricky

```python id="d34"
x=5

x=x+2

print(x)
```

Output:

7

---

## Example — Nested Loop

```python id="d35"
for i in range(2):

   for j in range(2):

      print("*",end="")
```

Output

```text id="d36"
****
```

---

## Why Output Prediction Helps

Builds:

* Dry-run skill
* Trace skill
* Bug detection
* Logic understanding

---

# Trace Table Method

Example:

```python id="d37"
sum=0

for i in range(1,4):
   sum+=i
```

Trace:

| i | sum |
| - | --- |
| 1 | 1   |
| 2 | 3   |
| 3 | 6   |

Final:

6

---

# Debugging Process (General)

## Step 1

Understand bug.

---

## Step 2

Classify error:

* Syntax?
* Logic?
* Runtime?

---

## Step 3

Reproduce error.

---

## Step 4

Inspect variables.

```python id="d38"
print(x)
```

---

## Step 5

Fix and retest.

---

# Common Debugging Strategies

## 1. Print Debugging

```python id="d39"
print(i,total)
```

---

## 2. Dry Run

Trace by hand.

---

## 3. Simplify Problem

Test smaller input.

---

## 4. Check Assumptions

Did you assume sorted list?

Correct input?

---

## 5. Use Known Test Cases

Example:

Factorial 5 should be:

120

---

# Common Beginner Mistakes

## Ignoring Error Messages

Read them.

They help.

---

## Changing Many Things at Once

Fix one thing at a time.

---

## Not Testing Edge Cases

Examples:

0

Negative values

Empty list

---

## Confusing Runtime vs Logical Error

Crash?

Runtime.

Wrong answer?

Logical.

---

# Practice Debugging Challenges

## Syntax

1. Fix missing colon
2. Fix indentation
3. Fix wrong keyword

---

## Logical

4. Fix wrong average formula
5. Fix off-by-one error
6. Fix wrong prime logic

---

## Runtime

7. Prevent divide-by-zero
8. Fix index error
9. Handle invalid input

---

## Output Prediction

10. Predict loop output
11. Predict nested loop output
12. Trace variable values

---

# Summary

## Error Types

Syntax

Program won’t start.

---

Logical

Runs, wrong answer.

---

Runtime

Crashes while running.

---

## Debugging Tools

```python id="d40"
print()
```

---

```text id="d41"
Dry Run
```

---

```text id="d42"
Trace Table
```

---

```python id="d43"
try/except
```

---

## Thinking Skills Used

* Error diagnosis
* Trace reasoning
* Problem isolation
* Logical verification

---

## Debugging Formula

For every bug ask:

1. Does program run?

If no → syntax error.

---

2. Does it crash?

If yes → runtime error.

---

3. Runs but wrong output?

Logical error.

---

4. Can I trace variables step by step?

Use dry run.

That is the foundation of debugging.
