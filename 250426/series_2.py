# 1,4,7,10,13,16,19,22,25,28, .... for N terms 
#  3 3 3 <--- difference static 3
N = int(input('N:'))
print('Series:')
term = 1
for I in range(N): # I -> 0, 1, .., N-1 -> N times 
    print(term,end=' ') # 1, 4, 7, 10, ...
    term = term + 3