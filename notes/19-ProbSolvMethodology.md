# Problem Solving Methodology — Notes

This section is about **how to approach problems systematically**, especially coding challenges.

Think:

Not just *write code*
But:

Understand → Design → Test → Improve

---

# 89. Understanding Constraints

## What are Constraints?

Constraints are limits or conditions in a problem.

Examples:

* Input size
* Value ranges
* Time limits
* Memory limits
* Special rules

---

## Example

Given:

```text id="c1"
1 ≤ n ≤ 100
```

n is small.

Simple methods may work.

---

Another:

```text id="c2"
1 ≤ n ≤ 1,000,000
```

Large input.

Need efficient solution.

---

## Types of Constraints

### Size Constraint

How much data?

Example:

10 items vs 1 million items.

---

### Value Constraint

Example:

```text id="c3"
0 ≤ marks ≤100
```

---

### Performance Constraint

Must finish quickly.

---

### Rule Constraint

Example:

* Array is sorted
* No duplicates
* Positive numbers only

Very important.

---

## Why Constraints Matter

They help choose algorithm.

Example:

Linear search

O(n)

may be fine for n=10.

Not ideal for n=1,000,000.

---

## Questions to Ask

* How large is input?
* Sorted or unsorted?
* Can duplicates exist?
* Can negatives appear?
* Edge cases?

---

# 90. Brute Force First Approach

## What is Brute Force?

Solve using simplest correct method first.

Even if slow.

---

## Why Start with Brute Force?

Because correctness comes first.

Optimization later.

---

## Example — Two Sum

Try every pair.

```python id="p1"
for i in range(n):

 for j in range(i+1,n):
```

Check all pairs.

---

## Example — Prime

Test every divisor.

Simple.

Correct.

---

## Strategy

Step 1

Build working solution.

Step 2

Improve later.

---

## Advantages

* Easy to think about
* Easier debug
* Baseline solution

---

## Beginner Rule

First ask:

Can I solve it by checking everything?

---

# 91. Improving Solutions

## After Brute Force…

Ask:

Can it be improved?

---

## Example

Linear search:

O(n)

---

If sorted…

Use binary search:

O(\log n)

Improvement.

---

## Example

Brute force prime:

Check all divisors.

Improve:

Check only up to

\sqrt n

---

## Common Improvement Methods

### Use better algorithm

Search:

Linear → Binary

---

### Use better data structure

List → Dictionary lookup

---

### Remove repeated work

Reuse computations.

---

### Reduce search space

Halve possibilities.

---

## Improvement Questions

* Can I do fewer comparisons?
* Can I avoid repeated work?
* Can data be preprocessed?
* Can sorting help?

---

# 92. Thinking in Algorithms

## What is Algorithmic Thinking?

Design a repeatable step-by-step solution.

---

## Instead of:

Trying random ideas.

Think:

What process always works?

---

## Example — Linear Search

Algorithm:

1 Check first element

2 Compare

3 Move next

4 Stop when found

Systematic.

---

## Algorithm Design Pattern

Input

↓

Process Steps

↓

Output

---

## Example — Find Largest

Algorithm:

* Assume first largest

* Compare each element

* Update largest

* Return result

---

## Algorithmic Thinking Questions

* What steps solve this?
* Are they always correct?
* Can I describe them clearly?
* Can someone else follow them?

---

## Pseudocode Example

```text id="c4"
Read n

largest=first

for each value

 if bigger

   update largest
```

Algorithm.

---

# 93. Writing Test Cases

## What is a Test Case?

Input + expected output.

Used to verify correctness.

---

## Example

Problem:

Even/Odd

---

Test Case 1

Input:

4

Expected:

Even

---

Test Case 2

Input:

7

Expected:

Odd

---

## Types of Test Cases

### Normal Cases

Typical inputs.

---

### Edge Cases

Boundary values.

Example:

0

1

Empty list

---

### Extreme Cases

Very large inputs.

---

### Invalid Cases

Unexpected inputs.

Example:

Negative age.

---

## Example — Factorial

Test:

```text id="c5"
5 ->120
1 ->1
0 ->1
```

---

## Good Practice

Always test:

Small cases first.

---

## Test Case Checklist

* Small input
* Large input
* Boundary values
* Special cases
* Error cases

---

# 94. Dry Run Techniques

## What is Dry Run?

Execute program manually on paper.

Trace variables step by step.

---

## Example

```python id="p2"
sum=0

for i in range(1,4):

   sum+=i
```

---

Trace table

| i | sum |
| - | --- |
| 1 | 1   |
| 2 | 3   |
| 3 | 6   |

Output:

6

---

## Example — Largest

```python id="p3"
largest=3

nums=[3,7,2]
```

Trace:

| Current | Largest |
| ------- | ------- |
| 3       | 3       |
| 7       | 7       |
| 2       | 7       |

---

## Dry Run Steps

1 Track inputs

2 Track variables

3 Track loop changes

4 Track condition results

5 Verify final output

---

## Useful For

* Debugging
* Understanding loops
* Output prediction
* Verifying algorithms

---

## Dry Run Small Inputs First

Use:

n=3

Not n=100.

Makes logic clearer.

---

# Full Problem-Solving Workflow

Use this for any coding problem:

---

## Step 1

Understand problem.

---

## Step 2

Study constraints.

---

## Step 3

Create brute force solution.

---

## Step 4

Dry run it.

---

## Step 5

Write test cases.

---

## Step 6

Improve if needed.

---

## Step 7

Implement final solution.

---

# Common Beginner Mistakes

## Coding Before Understanding Constraints

Wrong.

Understand problem first.

---

## Optimizing Too Early

Don't start with clever solution.

Start correct.

---

## No Test Cases

Dangerous.

---

## No Dry Run

Logic errors stay hidden.

---

## Ignoring Edge Cases

Example:

Empty list.

Can break solution.

---

# Practice Problems

## Constraints

1. Decide if linear search okay for n=20

2. Decide if binary search better for n=1 million

---

## Brute Force

3. Two Sum all pairs

4. Prime all divisors

---

## Improve

5. Optimize prime using √n

6. Replace search with dictionary

---

## Algorithms

7. Write algorithm for largest element

---

## Test Cases

8. Create 5 tests for factorial

---

## Dry Run

9. Trace bubble sort pass

---

# Summary

## Core Methodology

Understand constraints

↓

Brute force first

↓

Improve

↓

Think algorithmically

↓

Test

↓

Dry run

---

## Thinking Skills Used

* Problem analysis
* Algorithm design
* Optimization thinking
* Verification
* Debugging

---

## Universal Problem Formula

For every coding problem ask:

1. What are constraints?
2. What is simplest correct solution?
3. Can it be improved?
4. What algorithm describes it?
5. What test cases verify it?
6. Can I dry run it?

That is the foundation of structured problem solving.
