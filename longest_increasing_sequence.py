# http://stackoverflow.com/questions/2631726/how-to-determine-the-longest-increasing-subsequence-using-dynamic-programming

# NOTE: values in DP seem to be 1 too high
max_length = 0		
best_end = 0

array = [3, -1, 2, 3, 4, -5, 6, 7, 9]

DP = [1] * len(array)
prev = [-1] * len(array)

for i in range(len(array)):
	for j in range(len(array)):
		# find the maximum j < i, array[j] < array[i] that maximizes the length
		if array[i] > array[j] and DP[j] + 1 > DP[i]:
			DP[i] = DP[j] + 1
			prev[i] = j

	if DP[i] > max_length:
		best_end = i
		max_length = DP[i]

print DP
print prev
print max_length
print best_end