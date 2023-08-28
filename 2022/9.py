from math import copysign
tail_visits = [(0, 0)]
length_rope = 10 #2 for part one
rope = [[0, 0] for _ in range(length_rope)]

def propagate_movement(head): #head index value is local, head isn't the first knot which leads movement
	if head >= length_rope - 1: return #stop propagation once tail is reached
	else:
		diff_x = rope[head][0] - rope[head+1][0]
		diff_y = rope[head][1] - rope[head+1][1]
		if abs(diff_x) > 1 or abs(diff_y) > 1:
			diff_x, diff_y = [int(copysign(1, x)) if abs(x) > 1 else x  for x in [diff_x, diff_y]]
			rope[head+1] = [rope[head+1][0] + diff_x, rope[head+1][1] + diff_y]
			if head == length_rope - 2: tail_visits.append(tuple(rope[-1]))
		propagate_movement(head + 1)

def move_head_and_propagate_movement(x, y):
	rope[0]=[rope[0][0]+x, rope[0][1]+y]#move head
	propagate_movement(0)

while True:
	try:
		direction, step = input().strip().split(" ")
		for x in range(int(step)):
			match direction:
				case "U": move_head_and_propagate_movement(0, 1)
				case "R": move_head_and_propagate_movement(1, 0)
				case "D": move_head_and_propagate_movement(0, -1)
				case "L": move_head_and_propagate_movement(-1, 0)
	except EOFError as e:
		print(len(set(tail_visits)))
		break
