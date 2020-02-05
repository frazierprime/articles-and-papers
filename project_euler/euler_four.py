#!/usr/bin/env

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

# the largest three digit number is 999, so maybe we can work backwards from there, multiplying 999 by other three digit numbers. 
# Once we hit a palindrome, we can assume that is the largest palindrome for two, three digit numbers.
# Problem with this implementation: requires a call to palindrome test every time a product is produced. This seems very inefficient.



MAX_NUMBER_TO_TEST = 999
MIN_NUMBER_TO_TEST = 100
TEN = 10

# O(n) where n is = num digits in num_to_test
def check_for_palindrome(num_to_test):

	# The modulus operator returns unwanted values when operating on negative numbers.
	if num_to_test < 0:
		num_to_test = abs(num_to_test)
	
	# No need to attempt a palindrome check on a single digit.
	if num_to_test < TEN:
		return num_to_test
	
	orginal_num_to_test = num_to_test
	reverse = 0
	while (num_to_test > 0):

		# The remainder of this operation will be the last digit in the integer.
		temp = num_to_test % TEN

		# Ensure that temp is appended to the end of our new integer by shifting the last "temp" into the tens column, and putting the new reverse into the ones column.
		reverse = (reverse * TEN) + temp

		# Divide our num_to_test by ten to remove the last digit.
		num_to_test //= TEN

	if reverse == orginal_num_to_test:
		return True
	else:
		return False


def find_largest_palindrome_product():
	
	# Walk back from our largest possible 3-digit number. If we hit a palindrome, then it is the largest.
	for i in range(MAX_NUMBER_TO_TEST, MIN_NUMBER_TO_TEST, -1):
		for j in range(MAX_NUMBER_TO_TEST, MIN_NUMBER_TO_TEST, -1):
			this_product = i * j
			if check_for_palindrome(this_product):
				return [i, j, this_product]

if __name__ == "__main__":
	palindrome_data = find_largest_palindrome_product()
	print('largest palindrome: {}\nIs a product of: {} and {}'.format(palindrome_data[2], palindrome_data[0], palindrome_data[1]))




