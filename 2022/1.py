#first star
# max_sum = 0
# current_sum = 0

# while True:
# 	try:
# 		line = input()
# 		if line:
# 			current_sum += int(line)
# 		else:
# 			max_sum = max(max_sum, current_sum)
# 			current_sum = 0
# 	except EOFError:
# 		print(max(max_sum, current_sum))
# 		break

#force EOF w/ctrl+d

#second star
sums=[]
current_sum = 0

while True:
	try:
		line = input()
		if line:
			current_sum += int(line)
		else:
			sums.append(current_sum)
			current_sum = 0
	except EOFError:
		sums.append(current_sum)
		print(sums)
		sums.sort()
		break
#force EOF w/ctrl+d