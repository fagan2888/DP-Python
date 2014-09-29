'''
Given a knapsack of capacity C, and n different items, each with its own value and weight

Find the maximum value
and then reconstruct the solution
'''

# weights and values are parallel arrays of size n=5
weights = [5, 7, 3, 4, 6]
values = [9, 12, 8, 4, 5]
n = len(weights)
C = 50

# Subproblem: given backpack of capacity j, maximize its value
# j-th slot can either be filled, or not
# V(j) = max{ V(j-1), max(V(j - Wi) + Vi) }

# Overlapping substructure
# Build from bottom up
# let V[j] be the maximum value at each capacity j
steps = [-1] * C 	# boolean representing whether the j-th slot is used
items = [-1] * C 	# item storing which item is put into the knapsack
V = [0] * C
for j in range(1, 50):
	# Find item i that maximizes the value, if j-th slot of backpack is used
	max_from_item = 0
	max_item = 0
	for i in range(n):
		# If capacity is enough
		if weights[i] < j:
			# Fill with item i
			curr_val = V[j - weights[i]] + values[i]

			if curr_val > max_from_item:
				max_from_item = curr_val
				max_item = i

	# Compare with not filling j-th slot
	j_not_used = V[j-1]
	j_used = max_from_item

	if (j_not_used > j_used):
		steps[j] = 0
	else:
		steps[j] = 1
		items[j] = max_item

	# Store the max_item used here.
	V[j] = max(j_used, j_not_used)

# Reconstructing the items in knapsack, starting at j = C-1
full_solution = []
j = C-1
while j > 0:
	# If not used
	if steps[j] == 0:
		j -= 1
	else:
		item = items[j]
		full_solution.append(item)
		j -= weights[item]

# TODO - full solution here uses the slots that exceed the capacity!
print V
print full_solution
print sum(map(lambda x: values[x], full_solution))
print sum(map(lambda x: weights[x], full_solution))