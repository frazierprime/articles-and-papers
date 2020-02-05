#!/usr/bin/env python3

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2

# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
MAX_VALUE = 1000

def is_pythagorean_triplet(a, b, c):
	if a**2 + b**2 == c**2:
		return True
	else:
		return False


def find_pythagorean_triplets_in_range(max_range):
	for i in range(max_range):
		for j in range(i + 1, max_range):
			for k in range(i + 2, max_range):
				if i + j + k == MAX_VALUE:
					if is_pythagorean_triplet(i, j, k):
						print('found the magical tiplet')
						return i * j * k
				else:
					pass


if __name__ == "__main__":
	product = find_pythagorean_triplets_in_range(500)
	print(product)