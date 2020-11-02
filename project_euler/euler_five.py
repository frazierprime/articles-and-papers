#!/usr/bin/env python3

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

from functools import reduce

# TODO: Refactor the prime number test code into its own helper module.
from euler_three import is_prime_number_test

def gcd(a: int, b: int):

	a, b = sorted((a,b))

	while b:
		a, b = b, a % b

	return a

def get_lcm(a: int, b: int):
	return a * b // gcd(a, b)

def define_ranged_list(max_range):
	ranged_list = []
	for i in range(1, max_range + 1):
		ranged_list.append(i)
	return ranged_list

if __name__ == "__main__":
	RANGED_LIST = define_ranged_list(20)

	# This turned out to be VERY handy. We call get_lcm on each item in the range(1, 20)
	LCM = reduce(lambda x, y: get_lcm(x, y), RANGED_LIST)
	print(LCM)
