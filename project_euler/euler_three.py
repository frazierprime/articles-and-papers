#!/usr/bin/env python3

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143?

TARGET = 600851475143

PRIME_FACTORS = []

# O(log n)
def is_prime_number_test(num_to_check):

	if num_to_check <= 1:
		return False

    # If num_to_check == 2 OR 3.     
	if num_to_check <= 3:
		return True

	if num_to_check % 2 == 0 or num_to_check % 3 == 0:
		return False

	i = 5
	while i * i <= num_to_check:
		if num_to_check % i == 0 or num_to_check % (i + 2) == 0:
			return False
		# Why 6?
		# Our starting value for this control flow is 5, after we validate that i is
		# not a factor of num_to_check, we advance to 11, then 17, then 23, then 29.
		# 6 is simply an optimal incrementer for not having to scan every real number
		# to check if they are a factor of num to check.
		i = i + 6

	return True

# O(log n + log n). Why? The logic for determining factors of "target" is O(log n), 
# as is the algorithm to check if this value is a prime number.
def find_largest_prime_factor(target):
	factors = []

	this_factor = 2

	if is_prime_number_test(target):
		return target
	
	# Squaring this_factor allows us to close the gap between our test factors and the target quicker.
	# (especially helpful in cases where the target is extremely large).
	while this_factor * this_factor <= target:
		if target % this_factor == 0:
			# this_factor is a factor of our target.
			# divide target by this factor and assign the value to target.
			target //= this_factor
			print('target after floor division and assignment: {}'.format(target))
			factors.append(this_factor)
			
		else:
			# move to the next potential factor.
			this_factor += 1

	if is_prime_number_test(target):
		# In this case, target is prime, and is a factor of the original target.
		# Because of the logic, this case does not get added to the factors array, but is likely to be the 
		# larget prime factor of the original target.
		return target
	else:
		# Return the last item in the list of factors.
		return factors[-1]



if __name__ == "__main__":
	result = find_largest_prime_factor(TARGET)
	print('result: {}'.format(result))
	# Verify that the result of our method is, indeed, prime.
	if is_prime_number_test(result):
		print('is result prime factor: {}'.format(True))
	else:
		pass
