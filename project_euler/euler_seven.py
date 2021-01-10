#!/usr/bin/env python3

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10001st prime number?

from euler_three import is_prime_number_test

MAX_RANGE_TO_CHECK = 300000

# Time to break out the sieve of eratosthenes.
def get_prime_terms_for_range(range_to_check):

	terms_array = [True] * (range_to_check + 1)
	num_primes = 0
	prime = 2

	# O(log n * log n)
	while prime**2 <= range_to_check:
		if terms_array[prime]:
			for i in range(prime * 2, range_to_check + 1, prime):
				terms_array[i] = False

		prime += 1

	# O(n) worst case. 
	for j in range(2, range_to_check):
		if terms_array[j]:
			num_primes += 1

		if num_primes == 10001:
			return j


if __name__ == "__main__":
	ten_thousand_and_one_th_prime = get_prime_terms_for_range(MAX_RANGE_TO_CHECK)
	print(ten_thousand_and_one_th_prime)