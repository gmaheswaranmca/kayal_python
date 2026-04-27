# Sorting Problems — Notes

## What is Sorting?

Sorting means arranging data in an order.

Common orders:

* Ascending (small to large)

```text
2 5 7 9
```

* Descending (large to small)

```text
9 7 5 2
```

---

## Why Sorting?

Sorting helps in:

* Searching faster
* Finding median
* Ranking students
* Removing duplicates
* Preparing data for analysis

---

## Fundamental Idea

Sorting repeatedly compares elements and reorders them.

Many beginner algorithms use:

* Compare
* Swap

---

## Swap Two Values

```python id="a2n14z"
a=5
b=8

a,b=b,a
```

---

# 53. Bubble Sort

## Idea

Largest element "bubbles" to the end each pass.

---

## Example

Input:

```text id="8vxt6u"
5 2 8 1
```

---

### Pass 1

Compare 5 and 2

Swap

```text id="w7gwf8"
2 5 8 1
```

Compare 5 and 8

No swap

Compare 8 and 1

Swap

```text id="aq1u6p"
2 5 1 8
```

Largest (8) reached end.

---

### Pass 2

```text id="vz7qun"
2 1 5 8
```

---

### Pass 3

```text id="td0k7j"
1 2 5 8
```

Sorted.

---

## Algorithm

For each pass:

Compare adjacent elements.

Swap if out of order.

---

## Code

```python id="0bn01m"
nums=[5,2,8,1]

n=len(nums)

for i in range(n-1):

   for j in range(n-1-i):

      if nums[j] > nums[j+1]:

         nums[j],nums[j+1]=nums[j+1],nums[j]
```

---

## Why inner loop shrinks?

After each pass, largest is already placed.

No need revisit.

---

## Complexity

Comparisons roughly:

n^2

Time:

O(n²)

---

## Bubble Sort Problems

* Sort marks
* Sort ages
* Sort without built-in sort()

---

# 54. Selection Sort

## Idea

Find smallest element.

Place it first.

Then repeat for remaining part.

---

## Example

Input

```text id="wmtovz"
64 25 12 22
```

---

Find smallest:

12

Swap with first.

```text id="zcq7zw"
12 25 64 22
```

---

Next smallest from remaining:

22

```text id="s73c5y"
12 22 64 25
```

---

Continue.

Sorted.

---

## Code

```python id="63m11v"
nums=[64,25,12,22]

n=len(nums)

for i in range(n-1):

   min_index=i

   for j in range(i+1,n):

      if nums[j] < nums[min_index]:
         min_index=j

   nums[i],nums[min_index]=nums[min_index],nums[i]
```

---

## Logic

* Search smallest
* Swap once per pass

---

## Difference from Bubble

Bubble:
Many swaps.

Selection:
Usually one swap each pass.

---

## Complexity

O(n^2)

---

# 55. Insertion Sort

## Idea

Build sorted part gradually.

Insert each new value into correct position.

---

## Like arranging playing cards.

---

## Example

Input

```text id="e3j4ez"
5 2 4 6
```

---

Start:

5 sorted.

---

Insert 2 before 5

```text id="2smnr6"
2 5
```

---

Insert 4

```text id="k46x4m"
2 4 5
```

---

Insert 6

```text id="thkl13"
2 4 5 6
```

---

Sorted.

---

## Code

```python id="c2t7g7"
nums=[5,2,4,6]

for i in range(1,len(nums)):

   key=nums[i]

   j=i-1

   while j>=0 and nums[j] > key:

      nums[j+1]=nums[j]

      j=j-1

   nums[j+1]=key
```

---

## Key Idea

Shift bigger elements right.

Insert key.

---

## Complexity

Worst:

O(n^2)

---

## Best (already sorted)

O(n)

---

# Compare Three Sorts

| Sort      | Idea                    | Swaps    | Time  |
| --------- | ----------------------- | -------- | ----- |
| Bubble    | Adjacent swaps          | Many     | O(n²) |
| Selection | Pick minimum            | Few      | O(n²) |
| Insertion | Insert into sorted part | Moderate | O(n²) |

---

# 56. Sorting-Based Problem Solving

Sorting is often a tool, not final goal.

---

## Problem 1 — Find Median

Sort first.

Middle element.

Example:

```text id="vrjlwm"
7 2 5
```

Sorted:

```text id="z9v63n"
2 5 7
```

Median:

5

---

## Problem 2 — Find Second Largest

Sort ascending.

Second last element.

```python id="wzwf9h"
nums[-2]
```

---

## Problem 3 — Remove Duplicates After Sorting

Sorted:

```text id="jlwm91"
1 1 2 2 3
```

Duplicates become adjacent.

Easy remove.

---

## Problem 4 — Two Sum Using Sorted Data (Intro idea)

Sorting can help search efficiently.

---

## Problem 5 — Rank Students

Sort marks descending.

Highest first.

---

## Problem 6 — Find Minimum Difference Pair

Sort first.

Check adjacent differences only.

---

## Problem 7 — Merge Sorted Lists

```text id="joh1kk"
1 3 5

2 4 6
```

Merge into sorted order.

---

## Sorting as Preprocessing

Sometimes sort first, solve later.

Very common strategy.

---

# Common Mistakes

## Wrong Inner Loop Limit

Bubble wrong:

```python id="3bqocg"
range(n)
```

Can access out of range.

Use:

```python id="5qtkva"
range(n-1-i)
```

---

## Forget Updating min_index

Selection fails.

---

## Forget Final Insertion

Insertion sort:

```python id="t6l09d"
nums[j+1]=key
```

Very important.

---

## Comparing Wrong Direction

Ascending:

```python id="x5mwlm"
>
```

Descending:

```python id="5h1d6c"
<
```

---

# Optimization Idea (Bubble Early Stop)

If no swaps in a pass, stop.

Already sorted.

```python id="a2yxez"
swapped=False
```

Useful improvement.

---

# Practice Problems

## Bubble

1. Sort 5 numbers
2. Sort descending
3. Count swaps

---

## Selection

4. Find smallest each pass
5. Sort student marks
6. Sort names alphabetically (concept)

---

## Insertion

7. Insert element in sorted list
8. Sort partially sorted data
9. Track shifts

---

## Sorting-Based

10. Find median
11. Find second largest
12. Remove duplicates after sorting

---

# Summary

## Core Patterns

Bubble:

Compare adjacent

```python id="bhl7q6"
nums[j] > nums[j+1]
```

---

Selection:

Track minimum

```python id="4xgk4f"
min_index
```

---

Insertion:

Shift and insert

```python id="t6j0mn"
key
```

---

## Core Complexities

Bubble:

O(n^2)

Selection:

O(n^2)

Insertion:

O(n^2)

---

## Thinking Skills Used

* Compare-and-swap
* Iterative refinement
* Ordering logic
* Problem reduction through sorting

---

## Sorting Problem Formula

For every sorting problem ask:

1. Need ascending or descending?
2. Compare-and-swap or select minimum?
3. Can sorting help solve bigger problem?
4. Need full sort or partial information only?
5. Complexity concern?

That is the foundation of sorting problems.
