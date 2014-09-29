
# Give two lists of numbers, find the smallest difference between two numbers, one from each array
def smallest_difference(a, b):
	min_diff = 999999999
	a_index = b_index = 0

	i = j = 0
	while i < len(a) and j < len(b):
		if a[i] >= b[j]:
			diff = a[i] - b[j]
		else:
			diff = b[j] - a[i]

		if diff < min_diff: 
			min_diff = diff
			a_index = i
			b_index = j

		if a[i] >= b[j]:
			j += 1
		else:
			i += 1

	return (a_index, b_index, min_diff)

a = [1, 5, 10, 15, 20]
b = [4, 7, 12]
print smallest_difference(a, b)