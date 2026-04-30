'''
    *
   **
  ***
 ****
***** N=5
'''
N = int(input('Number of lines:'))

for I in range(1,N+1):
    print((' ' * (N-I)), ('*' * I), sep='')