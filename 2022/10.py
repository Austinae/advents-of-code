cycle_waves = 0
cycle_counter = 0
register_x = 1
sum_signal_strengths = 0
grr = []
while True:
	try:
		if cycle_waves == 0:
			if cycle_counter >= 20:
				sum_signal_strengths += (20 * register_x)
				grr.append(sum_signal_strengths)
				cycle_waves = 1
		else:
			if cycle_counter >= (40 * cycle_waves):
				sum_signal_strengths += 40 * cycle_waves * register_x
				grr.append(40 * cycle_waves * register_x)
				cycle_waves += 1
		print(input().strip().split())
		match input().strip().split():
			case ["noop"]:
				cycle_counter += 1
			case ["addx", x]:
				cycle_counter += 2
				register_x += int(x)
	except EOFError:
		print(register_x)
		print(grr)
		print(sum_signal_strengths)
		break