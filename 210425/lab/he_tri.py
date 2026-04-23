# area of heron's triangle, given three sides a,b,c
a = float(input('side 1(a):'))
b = float(input('side 2(b):'))
c = float(input('side 3(c):'))

s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** (1 / 2)
print(f'side 1:{a}')
print(f'side 2:{b}')
print(f'side 3:{c}')
print(f'Area:{area:0.2f}')