'''
No duplicates
Given a knapsack of capacity C, and n different items, each with its own value and weight

Find the maximum value
and then reconstruct the solution
'''

val = [60, 100, 120]
weight = [10, 20, 30]
n = len(val)
C = 50

'''
V[i][j] # Item i at capacity j

not using the i-th item, and using it
V[i][j] = max{ V[i-1][j], V[i-1][j - Wi] + Vi }		
'''
V = [[0 for j in range(C + 1)] for i in range(n + 1)]
steps = [[0 for j in range(C + 1)] for i in range(n + 1)]

# Traverse through items, instead of capcity
# At each item, we choose to take it or leave it
for i in range(n + 1):		# IMPORTANT: we are counting 0..n 
	for j in range(C + 1):
		if i == 0 or j == 0:
			continue

		if j >= weight[i-1]:
			# whether to include it, or not
			exclude_i = V[i-1][j]
			include_i = V[i-1][j-weight[i-1]] + val[i-1]

			V[i][j] = max(exclude_i, include_i)
			if include_i > exclude_i:
				steps[i][j] = [i-1, j-weight[i-1]]
			else: 
				steps[i][j] = [i-1,j]
		else:
			V[i][j] = V[i-1][j]

full_solution = []
j = C
i = n
while j > 0 and i > 0:
	step = steps[i][j]
	next = V[step[0]][step[1]]

	# if item i was included
	if V[i][j] != next:
		val_diff = V[i][j] - next
		item = val.index(val_diff)
		full_solution.append(item)

	i = step[0]
	j = step[1]

print full_solution