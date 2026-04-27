# Searching Problems — Notes

## What is Searching?

Searching means finding whether a target value exists in data, and possibly where it exists.

Questions search can answer:

* Is 25 in the list?
* At what position is "Sam"?
* How many times does 5 occur?
* Where should a value be inserted?

---

## Two Fundamental Search Methods

1. Linear Search
2. Binary Search

---

# 49. Linear Search Problems

## What is Linear Search?

Check elements one by one until target is found.

---

## Idea

List:

```text
10 20 30 40 50
```

Search for 30:

* Check 10 ❌
* Check 20 ❌
* Check 30 ✅ Found

---

## Basic Algorithm

1. Start at first element
2. Compare with target
3. If match → found
4. Otherwise move next
5. If end reached → not found

---

## Code

```python id="74rt32"
nums=[10,20,30,40]

key=30

found=False

for x in nums:

    if x==key:
       found=True
       break

if found:
   print("Found")
else:
   print("Not Found")
```

---

## Find Position

```python id="d2eh5z"
for i in range(len(nums)):

   if nums[i]==key:
      print(i)
      break
```

---

## Find All Occurrences

```python id="8l4ylv"
for i in range(len(nums)):

   if nums[i]==key:
      print(i)
```

---

## Count Occurrences

```python id="v0k8kr"
count=0

for x in nums:

   if x==key:
      count+=1
```

---

## Search Largest Element (scan search)

```python id="jfx0bi"
largest=nums[0]

for x in nums:

   if x>largest:
      largest=x
```

Searching for best value.

---

## Common Linear Search Problems

* Search element
* Find index
* Count occurrences
* First occurrence
* Last occurrence

---

# 50. Binary Search Problems

## What is Binary Search?

Search in a **sorted list** by repeatedly dividing search space in half.

Requires:

✅ Sorted data

---

## Idea

List:

```text
10 20 30 40 50 60
```

Find 50.

Middle:

30

50 > 30

Search right half only.

---

## Repeat.

This removes half each step.

---

## Binary Search Steps

1. Low = first index
2. High = last index
3. Find middle

mid=\left\lfloor\frac{low+high}{2}\right\rfloor

4. Compare:

* equal → found
* smaller → go left
* larger → go right

Repeat.

---

## Code

```python id="brx8e5"
nums=[10,20,30,40,50]

key=40

low=0
high=len(nums)-1

while low<=high:

   mid=(low+high)//2

   if nums[mid]==key:
      print("Found")
      break

   elif key<nums[mid]:
      high=mid-1

   else:
      low=mid+1
```

---

## Example Walkthrough

Find 50

```text
10 20 30 40 50 60
```

Middle=30

Go right

40 50 60

Middle=50

Found.

---

## Binary Search Problems

* Find element
* Search insert position
* First occurrence in sorted array
* Last occurrence
* Find square root (basic search idea)

---

## Important

Binary search only works properly on sorted data.

Wrong:

```text
20 5 30 10
```

Unsorted.

Cannot use binary search.

---

# 51. Search Problem Strategies

## Strategy 1 — Ask: Sorted or Unsorted?

If unsorted:

Use linear search.

If sorted:

Consider binary search.

---

## Strategy 2 — What Must Be Returned?

Need:

* Found / not found?
* Position?
* First occurrence?
* Count?

Different problem.

---

## Strategy 3 — Brute Force First

Start simple:

Linear search.

Optimize later.

---

## Strategy 4 — Search Pattern

General pattern:

```python id="3gll8r"
for item in data:

   if item matches target:
      return found
```

---

## Strategy 5 — Search by Compare-and-Eliminate

Binary search:

Remove half.

---

## Strategy 6 — Searching for Extremes

Sometimes "search" means find:

* Minimum
* Maximum
* Second largest

Scan through data.

---

## Example — First Even Number

```python id="j99o8q"
for x in nums:

   if x%2==0:
      print(x)
      break
```

---

## Example — Search in String

```python id="lcbnsf"
for ch in s:

   if ch=="a":
      print("Found")
```

---

## Search Variations

### Membership search

Is value present?

---

### Position search

Where is value?

---

### Frequency search

How many occurrences?

---

### Optimization search

Find best candidate.

---

# 52. Complexity Awareness (Intro)

## What is Complexity?

How much work an algorithm does.

Usually measured as growth when data increases.

---

## Example

Search 5 items:

Maybe 5 comparisons.

Search 1000 items:

Maybe 1000 comparisons.

Growth matters.

---

## Linear Search Complexity

Worst case:

Check every element.

If n items:

At most:

n

comparisons.

Called:

O(n)

---

## Binary Search Complexity

Each step halves data.

Comparisons:

\log_2 n

Called:

O(log n)

---

## Comparison Example

1000 items.

Linear:

May check 1000.

Binary:

About

\log_2(1000)\approx10

Huge difference.

---

## Visual Idea

Linear:

100 → 99 → 98 ...

One-by-one.

---

Binary:

100 → 50 → 25 → 12 ...

Half-half-half.

---

## Best / Worst Case

### Linear Search

Best case:

Target first item.

1 comparison.

---

Worst case:

Target last item or absent.

n comparisons.

---

## Binary Search

Best case:

Middle first try.

---

Worst:

Repeated halving.

Still very small.

---

## Why Complexity Matters

Small input:

Either method okay.

Large input:

Better algorithm matters.

---

## Beginner Rule

Use:

* Correct algorithm first
* Efficient algorithm next

Correctness before optimization.

---

# Common Mistakes

## Using Binary Search on Unsorted Data

Wrong.

Must sort first.

---

## Wrong Mid Update

Wrong:

```python id="kk6t2i"
low=mid
```

Can cause infinite loop.

Correct:

```python id="6glkh0"
low=mid+1
```

---

## Forget Break in Linear Search

May keep searching after found.

---

## Off-by-One Error

Wrong:

```python id="y2wkrl"
while low<high
```

May miss last element.

Usually:

```python id="txvmem"
while low<=high
```

---

# Practice Problems

## Linear Search

1. Find target in list
2. Find first occurrence
3. Count occurrences

---

## Binary Search

4. Search sorted list
5. Find insert position
6. First occurrence in sorted duplicates

---

## Strategy Problems

7. Find largest
8. Find smallest positive
9. Search character in string

---

## Complexity Thinking

10. Compare linear vs binary comparisons for 64 items.

---

# Summary

## Core Search Types

Linear:

```python id="s4dxjw"
for x in nums
```

---

Binary:

```python id="o28sv6"
while low<=high
```

---

## Core Formula

Middle:

\frac{low+high}{2}

---

Linear complexity:

O(n)

---

Binary complexity:

O(\log n)

---

## Thinking Skills Used

* Search logic
* Elimination
* Compare-and-update
* Efficiency awareness

---

## Search Problem Formula

For every search problem ask:

1. Sorted or unsorted?
2. Need presence, position, or count?
3. Use linear or binary?
4. Need full scan or elimination?
5. Complexity concern?

That is the foundation of searching problems.
