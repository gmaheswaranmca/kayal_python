# 1,2,3,4,5,6, ... for N terms
N = int(input('N:'))
print('Series:')
term = 1
for I in range(N): # I -> 0,1,2,3,...,N-1 -> N times
    print(term, end=' ')
    term = term + 1
