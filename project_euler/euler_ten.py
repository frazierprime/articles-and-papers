#!/usr/bin/env python3

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

import operator
from functools import reduce

MAX_RANGE = 2000000

def get_prime_terms_for_range(range_to_check):

	terms_array = [True] * (range_to_check + 1)
	prime_terms = []
	prime = 2

	while prime**2 <= range_to_check:
		if terms_array[prime]:
			for i in range(prime * 2, range_to_check + 1, prime):
				terms_array[i] = False


		prime += 1

	for j in range(2, range_to_check):
		if terms_array[j]:
			prime_terms.append(j)

	return prime_terms

def sum_prime_terms(prime_terms):
	return reduce(operator.add, prime_terms)

if __name__ == "__main__":
	prime_terms = get_prime_terms_for_range(MAX_RANGE)
	print(sum_prime_terms(prime_terms))
