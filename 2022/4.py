#first star
# sum_fully_contained = 0
# while True:
# 	try:
# 		a, b = input().split(',')
# 		aMin, aMax = [int(x) for x in a.split('-')]
# 		bMin, bMax = [int(x) for x in b.split('-')]
# 		if aMin >= bMin and aMax <= bMax:
# 			sum_fully_contained += 1
# 		elif bMin >= aMin and bMax <= aMax:
# 			sum_fully_contained += 1
# 	except EOFError:
# 		print(sum_fully_contained)
# 		break

#second star
sum_fully_contained = 0
while True:
	try:
		a, b = input().split(',')
		aMin, aMax = [int(x) for x in a.split('-')]
		bMin, bMax = [int(x) for x in b.split('-')]
		if aMin >= bMin and aMin <= bMax:
			sum_fully_contained += 1
		elif aMax >= bMin and aMax <= bMax:
			sum_fully_contained += 1
		elif bMin >= aMin and bMin <= aMax:
			sum_fully_contained += 1
		elif bMax >= aMin and bMax <= aMax:
			sum_fully_contained += 1
	except EOFError:
		print(sum_fully_contained)
		break