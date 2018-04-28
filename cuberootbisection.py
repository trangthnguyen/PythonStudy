#!/usr/bin/env python3
#Find an approximation to a cube root using bisection search
x = float(input('Input a number:'))
epsilon = 0.01
guessCount = 0
low = 0.0
high = max(1.0, abs(x))
guess = (low + high) / 2
while abs(guess ** 3 - abs(x)) >= epsilon:
	if guess ** 3 - epsilon > abs(x):
		high = guess
	else:
		low = guess
	guess = (low + high) / 2
	guessCount += 1
print('The number of guesses =', guessCount)
if x < 0:
	guess = - guess
print('An approximation to the cube root of', x, 'is:', guess)
