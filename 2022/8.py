import numpy as np

with open("input.txt", "r") as file:
	trees = np.array([[int(y) for y in x] for x in [line.strip() for line in file.readlines()]])
height=len(trees)
width=len(trees[0])

# str - start range, er - end range, s - step, flipped - order in which we traverse grid
def calculate_tree_visibility(visible_trees, str_x, er_x, s_x, str_y, er_y, s_y, flipped=False):
	for x in range(str_x, er_x, s_x):
		max_height = -1
		for y in range(str_y, er_y, s_y):
			tree_height = trees[x, y] if not flipped else trees[y, x]
			if tree_height > max_height:
				max_height = tree_height
				if flipped:visible_trees[y, x] = 1
				else: visible_trees[x][y] = 1

def part_one():
	visible_trees = np.zeros((width, height), dtype=int) #faster than [[0 for _ in range(width)] for _ in range(height)]
	calculate_tree_visibility(visible_trees, 0, height, 1, 0, width, 1) #west
	calculate_tree_visibility(visible_trees, 0, height, 1, width-1, -1, -1) #east
	calculate_tree_visibility(visible_trees, 0, width, 1, 0, height, 1, 1) #north
	calculate_tree_visibility(visible_trees, 0, width, 1, height-1, -1, -1, 1) #south
	return sum([sum(x) for x in visible_trees])


def compute_scenic_score(route):
	big_trees_array = list(route >= 0)
	if True in big_trees_array:
		return big_trees_array.index(True) + 1
	else:
		return len(big_trees_array)

def part_two():
	scenic_scores = np.zeros((width, height), dtype=int)

	for i in range(1, trees.shape[0]-1):
		for j in range(1, trees.shape[1]-1):
			tree_column = trees[:, j] - trees[i, j]
			tree_row = trees[i, :] - trees[i, j]
			routes = [tree_row[j-1::-1], tree_row[j+1:], tree_column[i-1::-1], tree_column[i+1:]] # west, east, north, south
			scenic_scores[i,j] = np.prod(list(map(compute_scenic_score, routes)))
		
	return np.max(scenic_scores)

print(part_one())
print(part_two())

