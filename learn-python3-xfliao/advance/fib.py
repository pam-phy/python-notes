#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fib(n):
	m, a, b = 0, 0, 1
	while m < n:
		yield b
		a, b = b, a + b
		m = m + 1
	return 'Done!'

fib(20)
