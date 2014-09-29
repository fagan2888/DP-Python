# Given a binary matrix, find out the maximum size square sub-matrix with all 1s.
def max_matrix(M):
	row_count = len(M)
	col_count = len(M[0])

	S = []
	for i in range(row_count):
		S.append([0] * col_count)

	# Initialize the first column
	for i in range(row_count):
		S[i][0] = M[i][0]

	# Initialize the first row 
	for j in range(len(M[0])):
		S[0][j] = M[0][j]

	# Construct other entries of the auxilliary matrix S
	for i in range(row_count):
		for j in range(col_count):
			if M[i][j] == 1:
				S[i][j] = min(S[i][j-1], S[i-1][j], S[i-1][j-1]) + 1
			else:
				S[i][j] == 0

	# Find the maximum entry, and the indexes of maximum subentry
	max_of_s = S[0][0]
	max_i = 0
	max_j = 0
	for i in range(row_count):
		for j in range(col_count):
			if max_of_s < S[i][j]:
				max_of_s = S[i][j]
				max_i = i
				max_j = j

	print max_i
	print max_j 
	print max_of_s

	# Since S[i][j] denotes the bottom right corner 
	for i in range(max_i - max_of_s + 1, max_i + 1):
		for j in range(max_j - max_of_s + 1, max_j + 1):
			print (i, j), M[i][j]

M = [
	[0, 1, 1, 0, 1],
	[1, 1, 0, 1, 0],
	[0, 1, 1, 1, 0],
	[1, 1, 1, 1, 0],
	[1, 1, 1, 1, 1],
	[0, 0, 0, 0, 0]
]

print max_matrix(M)