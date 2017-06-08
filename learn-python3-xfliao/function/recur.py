#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fact(n):
	if n == 1:
		return 1
	return n * fact(n - 1)

def fact_t(n):
	return fact_iter(n, 1)

def fact_iter(num, product):
	if num == 1:
		return product
	return fact_iter(num - 1, num * product)

print('fact(1)  =', fact(1))
print('fact(5)  =', fact(5))
print('fact(10) =', fact(10))

print('fact_t(1000) =' fact_t(1000))
