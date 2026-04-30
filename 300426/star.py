# Print a star triangle (Left-Aligned Triangle)
'''
*
**
***
****
***** N lines
'''

N = int(input('Enter N (number of lines):'))

for I in range(1,N+1):
    for J in range(1,I+1):
        print('*', end='')
    #
    print()
#



