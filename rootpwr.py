#!/usr/bin/env python3
#Write a program that asks the user to enter an integer and
#prints two integers, root and pwr, such that 0 < pwr < 6 and root**pwr is equal
#to the integer entered by the user. If no such pair of integers exists, it should
#print a message to that effect.
x = int(input('Input an integer:'))
root = 0
countFindings = 0
while root <= x:
	pwr = 1
	while pwr < 6:
		if root ** pwr == x:
			print(root, '**', pwr, '=', x)
			countFindings = countFindings + 1
		pwr = pwr + 1
	root = root + 1
if countFindings == 0:
	print('There is no pair of root and pwr such that root ** pwr =', x) 		
