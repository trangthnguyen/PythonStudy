#!/usr/bin/env python3
#prints the integer cube root, if it exists, of an
#integer. If the input is not a perfect cube, it prints a message to that
#effect.
x = int(input('Enter integer number:'))
for guess in range(abs(x) + 1):
	if guess ** 3 >= abs(x):
		break
if guess ** 3 == abs(x):
	if x < 0:
		guess = - guess
	print('Cube root of', x, 'is:', guess)
else:
	print(x, 'is not a perfect cube')
