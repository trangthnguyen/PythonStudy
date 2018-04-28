#!/usr/bin/env python
#Write a program that asks the user to input 10 integers, and
#then prints the largest odd number that was entered. If no odd number was
#entered, it should print a message to that effect.
max = None
for i in range(10):
	x = input('Enter integer number ' + str(i + 1) + ':')
	x = int(x)
	if x % 2 != 0:
		if max == None or x > max:
			max = x
if max == None:
	print('There is no odd number')
else:
	print('The largest odd number is:', max)
