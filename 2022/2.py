#first star
#0 rock, 1 paper, 2 scissors
# sum_total = 0
# while True:
# 	try:
# 		opponent_move, guide_move = [ord(x) for x in input().split()]
# 		opponent_move -= 65
# 		guide_move -= 88
# 		if guide_move == 0: count = 1
# 		elif guide_move == 1: count = 2
# 		else: count = 3
# 		if opponent_move == guide_move: count += 3
# 		elif (opponent_move+1)%3 == guide_move: count += 6
# 		sum_total += count
# 	except EOFError:
# 		print(sum_total)
# 		break

#second star
#x lose, y draw, z win
sum_total = 0
while True:
	try:
		opponent_move, guide_move = [x for x in input().split()]
		opponent_move = ord(opponent_move) - 65
		count = 0
		if guide_move == 'Y':
			guide_move = opponent_move
			count = 3
		elif guide_move == 'Z':
			guide_move = (opponent_move+1)%3
			count = 6
		else: guide_move = (opponent_move-1)%3
		
		if guide_move == 0: count += 1
		elif guide_move == 1: count += 2
		else: count += 3
		sum_total += count
	except EOFError:
		print(sum_total)
		break
