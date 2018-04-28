#!/usr/bin/env python3
nameHandle = open('nameHandleFile.tex', 'w')
for i in range(2):
	name = input('Enter name: ')
	nameHandle.write(name + '\n')
nameHandle.close()
