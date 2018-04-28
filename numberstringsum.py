#!/usr/bin/env python3
#Let s be a string that contains a sequence of decimal numbers
#separated by commas, e.g., s = '1.23,2.4,3.123'. Write a program that prints
#the sum of the numbers in s.
x = input('Enter a string:')
count = 0
sum = 0
for i in x:
	if i in '0123456789':
		count = count + 1
		sum = sum + int(i)
if count > 0:
	print('Sum of the numbers in', x, 'is', sum)
else:
	print('There is no number in', x)
