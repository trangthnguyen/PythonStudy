#!/usr/bin/env python3
#Find the exact square root or an approximation to a square root using Newton-Raphson approximation
x = float(input('Input a positive number:'))
epsilon = 0.01
guessCount = 0
guess = x
while abs(guess ** 2 - x) >= epsilon:
	guess = guess - (guess ** 2 - x) / (2 * guess)
	guessCount = guessCount + 1
print('The number of guesses =', guessCount)
print('An approximation to the square root of', x, 'is:', guess)
