#!/usr/bin/env python3

# Problem two:
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

# O(log n)
def sum_even_numbers():
    # Set the starting values for current, next, and resulting terms.     
	current_term = 0
	next_term = 1
	resulting_term = 0
    
    # Keep a running sum of the even-valued fib terms.
	sum_of_evens = 0

	while resulting_term <= 4000000:
		# Create the fib sequence terms:
		resulting_term = current_term + next_term

		# Iterate current term:
		current_term = next_term

		# Iterate next term:
		next_term = resulting_term

		# If fibonacci term is even, add the value to the total sums:
		if resulting_term % 2 == 0:
			sum_of_evens += resulting_term

	return sum_of_evens

		
if __name__ == "__main__":
	print('sum of even numbers: {}'.format(sum_even_numbers()))

