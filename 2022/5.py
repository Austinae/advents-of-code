from math import ceil

#first star
stacks = []
switch_mode = False
while True:
	try:
		inp = input()
		#reverse lists to act like stacks
		if inp == "":
			for x in range(len(stacks)):stacks[x].reverse()
			continue
		#processing moves
		if switch_mode:
			a, amount, c, origin, e, destination = [x for x in inp.split()]
			#first star
			# for x in range(int(amount)):
			# 	stacks[int(destination)-1].append(stacks[int(origin)-1].pop())
			#second star
			stacks[int(destination)-1] += stacks[int(origin)-1][-(int(amount)):]
			del stacks[int(origin)-1][-(int(amount)):]
			continue
		#populate stacks
		if not stacks:
			stacks =[[] for x in range(ceil(len(inp)/4))]
		for x in range(1, len(inp), 4):
			if inp[x] != ' ' and inp[x].isalpha():
				stacks[x//4].append(inp[x])
			elif inp[x].isdigit():
				switch_mode = True
				break
	except EOFError:
		print("".join([x[-1] for x in stacks]).replace(" ", ""))
		break
