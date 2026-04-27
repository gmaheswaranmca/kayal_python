# Number Theory Problems — Notes

## What is Number Theory?

Number theory studies properties of integers (whole numbers).

In programming, number theory problems often involve:

* Divisibility
* Factors
* Prime numbers
* Digits
* Mathematical properties

These problems develop logical reasoning and algorithmic thinking.

---

# 34. Prime Number Problems

## What is a Prime Number?

A prime number has exactly **two factors**:

* 1
* Itself

Examples:

2, 3, 5, 7, 11

Not prime:

4 (1,2,4)

---

## Prime Check Logic

A number is prime if factor count = 2.

---

## Brute Force Method

```python id="a4dn4l"
n=int(input())

count=0

for i in range(1,n+1):

    if n%i==0:
        count+=1

if count==2:
    print("Prime")

else:
    print("Not Prime")
```

---

## Better Idea

Check divisors only up to:

\sqrt{n}

Because if a factor exists above √n, a matching one exists below it.

---

## Improved Prime Check

```python id="sq31tt"
n=17
prime=True

i=2

while i*i<=n:

    if n%i==0:
       prime=False
       break

    i+=1
```

---

## Print Primes up to N

```python id="hsk8j1"
for n in range(2,21):

    count=0

    for i in range(1,n+1):

       if n%i==0:
          count+=1

    if count==2:
       print(n)
```

---

## Common Prime Problems

* Check prime
* Print primes in range
* Count primes
* Find nth prime

---

# 35. Factors and Multiples

## Factor

A factor divides a number exactly.

Example:

Factors of 12:

1,2,3,4,6,12

---

## Find Factors

```python id="r9kgj6"
n=12

for i in range(1,n+1):

   if n%i==0:
      print(i)
```

---

## Count Factors

```python id="ql4v7w"
count=0

for i in range(1,n+1):

   if n%i==0:
      count+=1
```

---

## Largest Factor (Except Number)

```python id="9e5r3e"
largest=1

for i in range(1,n):

   if n%i==0:
      largest=i
```

---

## Multiple

A multiple is obtained by multiplying.

Multiples of 5:

5,10,15,20,...

---

## Check Multiple

```python id="gjtp4v"
if a%b==0:
   print("Multiple")
```

---

## Common Problems

* Find factors
* Count factors
* Common factors
* Multiples in range

---

# 36. GCD and LCM Problems

## GCD

Greatest Common Divisor

Largest number dividing both.

Example:

12 and 18

Factors:

12 → 1,2,3,4,6,12

18 → 1,2,3,6,9,18

Greatest common factor:

6

---

## Brute Force GCD

```python id="miykh8"
a=12
b=18

gcd=1

for i in range(1,min(a,b)+1):

   if a%i==0 and b%i==0:
      gcd=i

print(gcd)
```

---

## Euclidean Algorithm

Key idea:

GCD(a,b)=GCD(b,a\bmod b)

---

## Code

```python id="4j6c11"
a=12
b=18

while b!=0:

   a,b=b,a%b

print(a)
```

---

## LCM

Least Common Multiple

Smallest common multiple.

Example:

12 multiples:

12,24,36...

18 multiples:

18,36...

LCM=36

---

## Formula

LCM = \frac{a \times b}{GCD}

---

## Code

```python id="gdc71m"
lcm=(a*b)//gcd
```

---

## Problems

* Find GCD
* Find LCM
* Simplify fractions
* Coprime check

---

# 37. Digit-Based Problems

These use digits of a number.

Use:

Last digit:

```python id="nsdph4"
digit=n%10
```

Remove digit:

```python id="zlbv6j"
n=n//10
```

---

## Sum of Digits

123

1+2+3=6

```python id="6ljx2k"
sum=0

while n>0:

   digit=n%10

   sum+=digit

   n=n//10
```

---

## Count Digits

```python id="4d4h4o"
count=0

while n>0:

   count+=1

   n=n//10
```

---

## Reverse Number

```python id="3c7s3d"
rev=0

while n>0:

   digit=n%10

   rev=rev*10+digit

   n=n//10
```

---

## Palindrome Number

121

Reverse equals original.

---

## Product of Digits

```python id="9n66xu"
product=1
```

Multiply digits.

---

## Largest Digit

```python id="h9yvpk"
largest=0
```

Compare each digit.

---

## Problems

* Sum digits
* Reverse number
* Palindrome
* Largest digit
* Even digits count

---

# 38. Mathematical Property Problems

Numbers with special mathematical properties.

---

## Armstrong Number

A number where:

sum of digits raised to power of digits count equals number.

Example:

153

1^3+5^3+3^3=153

---

## Code

```python id="66nsdj"
orig=n

sum=0

while n>0:

   digit=n%10

   sum+=digit**3

   n=n//10

if sum==orig:
   print("Armstrong")
```

---

## Perfect Number

Sum of proper factors equals number.

Example:

6

1+2+3=6

---

## Check Perfect

```python id="0v7f5y"
sum=0

for i in range(1,n):

   if n%i==0:
      sum+=i

if sum==n:
   print("Perfect")
```

---

## Harshad Number

Divisible by sum of digits.

Example:

18

Digits sum=9

18 divisible by 9

---

## Automorphic Number

Square ends in same digits.

Example:

5

5²=25

Ends in 5.

---

## Strong Number

Sum of factorials of digits equals number.

145

1!+4!+5!=145

---

## Common Property Problems

* Armstrong
* Perfect
* Harshad
* Strong
* Automorphic

---

# Efficiency Idea

Many number problems use repeated digit extraction:

```python id="f7abj5"
digit=n%10
n=n//10
```

This is a standard pattern.

---

# Common Mistakes

## Prime Check Starting from 1

Wrong:

```python id="iw9rz5"
for i in range(1,n):
```

May miss factor n.

---

## Forget Original Number

Wrong

```python id="d01jfs"
while n>0:
```

After loop n becomes 0.

Save:

```python id="mt7l6y"
orig=n
```

---

## Wrong LCM Formula

Wrong:

```python id="smihf3"
a*b*gcd
```

Correct

\frac{ab}{GCD}

---

# Practice Problems

## Prime

1. Check prime
2. Print primes 1–100
3. Count primes in range

---

## Factors

4. Find factors
5. Count factors
6. Common factors

---

## GCD/LCM

7. Find GCD
8. Find LCM
9. Simplify fraction

---

## Digits

10. Reverse number
11. Sum digits
12. Largest digit

---

## Properties

13. Armstrong
14. Perfect
15. Harshad

---

# Summary

## Core Number Tools

Divisibility:

```python id="shxk66"
n%i==0
```

Digit extraction:

```python id="wln7rz"
n%10
```

Digit removal:

```python id="e6ebgf"
n//10
```

---

## Core Concepts

* Prime
* Factors
* GCD/LCM
* Digit processing
* Special properties

---

## Thinking Skills Used

* Pattern recognition
* Iteration
* Mathematical reasoning
* Algorithmic thinking

---

## Number Theory Problem Formula

For every problem ask:

1. Divisibility involved?
2. Factors needed?
3. Digits to process?
4. Property formula exists?
5. Use loop or repeated digit extraction?

That is the foundation of number theory programming.
