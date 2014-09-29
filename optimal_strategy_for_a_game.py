'''
Optimal Strategy for a Game: Consider a row of n coins of values v(1) ... v(n), where n is even. We play a game against an opponent by alternating turns. In each turn, a player selects either the first or last coin from the row, removes it from the row permanently, and receives the value of the coin. Determine the maximum possible amount of money we can definitely win if we move first.

Base case: 
points(i, j) = Vi  if i == j
points(i, j) = max(Vi, Vj) if j == i + 1
'''

# row of n coins
values = [1,2,3,4,5]
n = len(values)

# each time it is our turn, take the max of the two available moves (but the minimum of the opponent's two potential moves)
points = []
for i in range(n):
	points.append([0] * n)

for i in range(n):
	for j in range(n):
		if i == j:
			points[i][j] = values[i]
		elif j == i + 1:
			points[i][j] = max(values[i], values[j])
		
		# only valid if i < j
		take_start = ((i + 2) <= j)? points[i + 2][j] : 0
		take_end = ((i + 1) <= (j - 1))? points[i + 1][j - 1] : 0

            # // Here x is value of F(i+2, j), y is F(i+1, j-1) and
            # // z is F(i, j-2) in above recursive formula
            # x = ((i+2) <= j) ? table[i+2][j] : 0;
            # y = ((i+1) <= (j-1)) ? table[i+1][j-1] : 0;
            # z = (i <= (j-2))? table[i][j-2]: 0;
 
            # table[i][j] = max(arr[i] + min(x, y), arr[j] + min(y, z));