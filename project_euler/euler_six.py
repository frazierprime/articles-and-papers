#!/usr/bin/env python3

# The sum of the squares of the first ten natural numbers is,

# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# Test value to use, to test the validity of our logic.
TEST_MAX_RANGE = 10

# The value to test that satisfies euler #6.
MAX_RANGE_TO_TEST = 100

def get_values_and_diff(max_range_to_sum):
	sum_of_squares = 0
	sum_of_values = 0
	for i in range(1, max_range_to_sum + 1):
		sum_of_values += i
		sum_of_squares += i**2

	return sum_of_values**2 - sum_of_squares

def test_problem_example_parameters():
	diff = get_values_and_diff(TEST_MAX_RANGE)
	assert diff == 2640

def test_problem_solution():
	diff = get_values_and_diff(MAX_RANGE_TO_TEST)
	assert diff == 25164150

if __name__ == "__main__":
	test_problem_example_parameters()
	test_problem_solution()