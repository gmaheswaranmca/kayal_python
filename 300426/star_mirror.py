'''
    *
   **
  ***
 ****
***** N=5
'''
N = int(input('Number of lines:'))

for I in range(1,N+1):
    for J in range(1,N-I+1):
        print(' ', end='')
    #
    for J in range(1,I+1):
        print('*', end='')
    #
    print()