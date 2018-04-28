#!/usr/bin/env python3
#Find the exact square root or an approximation to a square root.
x = float(input('Input a positive number:'))
epsilon = 0.01
step = epsilon ** 2
guessCount = 0
guess = 0.0
while abs(guess ** 2 - x) >= epsilon and guess <= x:
	guess += step
	guessCount += 1
print('The number of guesses =', guessCount)
if abs(guess ** 2 - x) >= epsilon:
	print('Failed to find an approximation to the square root of', x)
else:
	print('An approximation to the square root of', x, 'is:', guess)
