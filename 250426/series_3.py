# 100,95, 85, 70, 50, 25, ... for 6 terms
# -5 -10 -15 -20 -25 <--- diff start at -5 add 5 for next diff continue 
N = int(input('N:'))
print('Series:')
term = 100
diff = 5
for I in range(N): # I -> 0,1,2,3,...,N-1 -> N times
    print(term, end=' ') # 100 95 85 70 ... 
    term = term - diff 
    diff = diff + 5     # 5 10 15 20