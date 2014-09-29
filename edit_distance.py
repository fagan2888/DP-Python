'''
Base case: 

Given two text strings A of length m and B of length n, you want to transform A into B with a minimum number of operations of the following types: delete a character from A, insert a character into A, or change some character in A into a new character. The minimal number of such operations required to transform A into B is called the edit distance between A and B.

'''

A = "hello"
B = "world"
m = len(A)
n = len(B)

penalty_d = 1 	# delete
penalty_i = 1 	# insert
penalty_c = 1 	# change

# Table - minimum edit distance for words with i, j marking the end of string A and B
dist = [[-1 for j in range(n)] for i in range(m)]
steps = [[(0, 0) for i in range(n)] for j in range(m)]

# Initialize base case - where one of the strings has gone past its start
# dist[i][0]
for i in range(m):
	dist[i][0] = i
for j in range(n):
	dist[0][j] = j

# Starting from the end of the array, counting back
i = m
j = n
for i in range(1, m):
	for j in range(1, n):
		# Case if equal
		if A[i] == B[j]:
			dist[i][j] = 0
			steps[i][j] = (i, j)	# we will distinguish in the solution reconstruction

		# Case if not equal
		# delete last char of A or
 		# delete last char of B or
		# change both, move on
		else:
			del_A = dist[i-1][j] + penalty_d
			del_B = dist[i][j-1] + penalty_d
			change_both = dist[i-1][j-1] + penalty_c

			dist[i][j] = min(del_A, del_B, change_both)

			if del_A == dist[i][j]:
				steps[i][j] = ((i-1, j))
			elif del_B == dist[i][j]:
				steps[i][j] = ((i, j-1))
			elif change_both == dist[i][j]:
				steps[i][j] = ((i-1, j-1))


full_solution = []
# Reconstruct the solution
i = m-1
j = n-1 
while i > 0 and j > 0:
	step = steps[i][j]
	print step, (i, j)

	if step[0] == i and step[1] == j:
		full_solution.append("no change")
	else:
		if step[0] == i and step[1] == j-1:
			full_solution.append("delete last char in B")
		if step[0] == i-1 and step[1] == j:
			full_solution.append("delete last char in A/Insert in B")
		if step[0] == i-1 and step[1] == j-1:
			full_solution.append("Change character")
			
		i = step[0]
		j = step[1]

# IMPORTANT: SOLUTION MISSING ONE!!!
print steps
print full_solution