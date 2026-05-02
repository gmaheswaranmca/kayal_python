```py
n=int(input('n:'))

for i in range(n):

    for j in range(n):

        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end="")

        else:
            print(" ",end="")

    print()
```

Explanation for n=5:
                  or
        ------------------------
i   j   1st     last   1st  last
        row     row    col  col 
        i==0    i==n-1 j==0 j==n-1
0   0    T       -      -    -          *
    1    T       -      -    -          *
    2    T       -      -    -          *
    3    T       -      -    -          *
    4    T       -      -    -          *
                                        \n
1   0    F      F       T    -          *
    1    F      F       F   F           ' '
    2    F      F       F   F           ' '
    3    F      F       F   F           ' '
    4    F      F       F   T           *
                                        \n
2   0   FFT-    *
    1   FFFF    ' '
    2   FFFF    ' '
    3   FFFF    ' '
    4   FFFT    *
                \n
3   0   FFT-    *
    1   FFFF    ' '
    2   FFFF    ' '
    3   FFFF    ' '
    4   FFFT    *
                \n
4   0   FT--    *
    1   FT--    *
    2   FT--    *
    3   FT--    *
    4   FT--    *
    \n
End of i loop

*****\n
*   *\n
*   *\n
*   *\n
*****\n