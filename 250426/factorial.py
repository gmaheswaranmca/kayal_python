# to find factorial of N
N = int(input('N:')) # to find n! # N=5
fact = 1
for I in range(N,0,-1): # 5, 4, 3, 2, 1, [0 stop]
    fact *= I #fact = fact * I

print(f'factorial of {N} is {fact}')