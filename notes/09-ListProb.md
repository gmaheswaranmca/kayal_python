# List Problems — Notes

## What is a List?

A list is an ordered collection of items.

It can store:

* Numbers
* Strings
* Mixed data

Example:

```python
nums=[10,20,30]
```

---

## Why Use Lists?

Instead of:

```python
a=10
b=20
c=30
```

Use:

```python
nums=[10,20,30]
```

Store many values in one variable.

---

# 44. List Basics

## Creating Lists

```python
a=[1,2,3]
```

```python
names=["Sam","Raj","Ana"]
```

---

## Indexing

| Index | Value |
| ----- | ----- |
| 0     | 10    |
| 1     | 20    |
| 2     | 30    |

```python
nums=[10,20,30]

print(nums[0])
```

Output:

```text
10
```

---

## Negative Index

```python
nums[-1]
```

Last item.

---

## Length

```python
len(nums)
```

---

## Reading a List

```python
arr=list(map(int,input().split()))
```

Input

```text
10 20 30
```

---

## Slicing

```python
nums[1:3]
```

---

## Update Element

```python
nums[1]=50
```

---

## Add Elements

```python
nums.append(40)
```

---

## Insert

```python
nums.insert(1,99)
```

---

## Remove

```python
nums.remove(20)
```

---

## Pop

```python
nums.pop()
```

Removes last element.

---

## Sort

```python
nums.sort()
```

---

## Reverse

```python
nums.reverse()
```

---

# 45. Traversing Lists

## What is Traversing?

Processing elements one by one.

---

## Method 1 — For Each

```python
for x in nums:
    print(x)
```

---

## Method 2 — Index Based

```python
for i in range(len(nums)):
    print(nums[i])
```

---

## Reverse Traversal

```python
for i in range(len(nums)-1,-1,-1):
    print(nums[i])
```

---

## Print Even Elements

```python
for x in nums:

   if x%2==0:
      print(x)
```

---

## Search Element

```python
key=20

for x in nums:

   if x==key:
      print("Found")
```

---

## Count Positives

```python
count=0

for x in nums:

   if x>0:
      count+=1
```

---

## Typical Traversal Problems

* Search
* Count positives
* Print even numbers
* Find negatives

---

# 46. Aggregation Problems on Lists

## What is Aggregation?

Combine many values into one result.

Examples:

* Sum
* Product
* Maximum
* Average

---

## Sum of List

```python
total=0

for x in nums:
   total+=x
```

---

## Average

Average=\frac{Sum}{Count}

```python
avg=total/len(nums)
```

---

## Product

```python
product=1

for x in nums:
   product*=x
```

---

## Largest Element

```python
largest=nums[0]

for x in nums:

   if x>largest:
      largest=x
```

---

## Smallest Element

```python
smallest=nums[0]
```

Compare each element.

---

## Second Largest

Keep:

* largest
* second

Update carefully.

---

## Count Elements Greater than 50

```python
count=0

for x in nums:

   if x>50:
      count+=1
```

---

## Common Aggregation Problems

* Sum
* Average
* Largest
* Smallest
* Second largest

---

# 47. List Transformation Problems

## What is Transformation?

Convert list into modified form.

---

## Square Every Element

Input:

```text
2 3 4
```

Output

```text
4 9 16
```

```python
result=[]

for x in nums:
   result.append(x*x)
```

---

## Double Each Value

```python
result=[]

for x in nums:
   result.append(2*x)
```

---

## Reverse List

```python
rev=[]

for i in range(len(nums)-1,-1,-1):
   rev.append(nums[i])
```

---

## Rotate Left by One

Input

```text
1 2 3 4
```

Output

```text
2 3 4 1
```

```python
rot=nums[1:]+nums[:1]
```

---

## Convert Positives to Zero

```python
for i in range(len(nums)):

   if nums[i]>0:
      nums[i]=0
```

---

## Mapping Example

Transform Celsius to Fahrenheit.

F=\frac{9}{5}C+32

Apply to every list item.

---

## Common Transform Problems

* Square values
* Double values
* Reverse
* Rotate
* Scale numbers

---

# 48. Duplicate and Filtering Problems

## Duplicate

Repeated values.

Example

```text
2 3 2 5 3
```

Duplicates:

2,3

---

## Remove Duplicates

```python
result=[]

for x in nums:

   if x not in result:
      result.append(x)
```

---

## Count Duplicates

Use frequency counting.

```python
freq={}
```

---

## Find First Duplicate

```python
seen=[]

for x in nums:

   if x in seen:
      print(x)
      break

   seen.append(x)
```

---

## Filtering

Selecting elements satisfying condition.

---

## Filter Even Numbers

```python
result=[]

for x in nums:

   if x%2==0:
      result.append(x)
```

---

## Filter Positives

```python
if x>0
```

---

## Filter Multiples of 5

```python
if x%5==0
```

---

## Remove Negatives

```python
result=[]

for x in nums:

   if x>=0:
      result.append(x)
```

---

## List Comprehension (Intro)

Filter:

```python
evens=[x for x in nums if x%2==0]
```

Transform:

```python
sq=[x*x for x in nums]
```

---

## Common Duplicate/Filter Problems

* Remove duplicates
* Find repeated elements
* Keep evens only
* Remove negatives
* Keep numbers above threshold

---

# Problem-Solving Strategies

## Strategy 1 — Traversal

```python
for x in nums
```

Process each element.

---

## Strategy 2 — Accumulator

```python
total+=x
```

Used for sum.

---

## Strategy 3 — Compare-and-Update

```python
if x>largest:
```

Used for max.

---

## Strategy 4 — Build New Result List

```python
result.append(...)
```

For transformation.

---

## Strategy 5 — Membership Check

```python
if x not in result
```

For duplicates.

---

# Common Mistakes

## Index Out of Range

Wrong

```python
nums[len(nums)]
```

Last valid index:

```python
len(nums)-1
```

---

## Wrong Largest Initialization

Wrong

```python
largest=0
```

Fails for negative lists.

Correct

```python
largest=nums[0]
```

---

## Modifying While Traversing

Risky:

```python
for x in nums:
   nums.remove(x)
```

Can skip values.

---

## Using `==` Instead of Assignment

Wrong

```python
nums[i]==0
```

Correct

```python
nums[i]=0
```

---

# Practice Problems

## Basics

1. Read a list
2. Print first and last item
3. Update an element

---

## Traversal

4. Search element
5. Count positives
6. Print even elements

---

## Aggregation

7. Find sum
8. Find largest
9. Find second largest

---

## Transformation

10. Square list
11. Reverse list
12. Rotate left

---

## Duplicates/Filtering

13. Remove duplicates
14. Filter evens
15. Remove negatives

---

# Summary

## Core Operations

Access

```python
nums[i]
```

Traversal

```python
for x in nums
```

Append

```python
result.append(x)
```

Length

```python
len(nums)
```

---

## Core Problem Types

* Traversal
* Aggregation
* Transformation
* Filtering
* Duplicate handling

---

## Thinking Skills Used

* Iteration
* Decomposition
* Pattern recognition
* Data processing

---

## List Problem Formula

For every list problem ask:

1. Need to visit each element?
2. Need single result (sum/max)?
3. Need transformed list?
4. Need filter condition?
5. Need duplicate handling?

That is the foundation of list programming.
