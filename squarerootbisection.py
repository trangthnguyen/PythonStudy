#!/usr/bin/env python3
#Find the exact square root or an approximation to a square root using bisection search
x = float(input('Input a positive number:'))
epsilon = 0.01
guessCount = 0
low = 0.0
high = max(1.0, x)
guess = (low + high) / 2
while abs(guess ** 2 - x) >= epsilon:
	if guess ** 2 - epsilon > x:
		high = guess
	else:
		low = guess
	guess = (low + high) / 2
	guessCount += 1
print('The number of guesses =', guessCount)
print('An approximation to the square root of', x, 'is:', guess)
