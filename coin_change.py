'''
You are given n types of coin denominations of values v(1) < v(2) < ... < v(n) (all integers). Assume v(1) = 1, so you can always make change for any amount of money C. Give an algorithm which makes change for an amount of money C with as few coins as possible.

	map to integer knapsack problem, with each item having a value of -1
	and denomination of coin maps to size of item

*** Variation: 
http://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/
Given a value N, if we want to make change for N cents, and we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins, how many ways can we make the change? The order of coins doesn’t matter.

- divide all set solutions in two sets.
1. solutions that do not contain m-th coin (or Sm)
2. solutions that contain at least one Sm.

'''

n = 50
table = [[0 for i in range(m)] for i in range(n + 1)]

# Fill the entries for 0 value case (n = 0)
for i in range(m):
	table[0][i] = 1

for i in range(n + 1):
	for j in range(m):
		# Count solutions including and excluding S[j]
		# table[n+1][m]
		x = (i-S[j] >= 0) ? table[i - S[j]][j] : 