#first + second star
lines = []
marker_length = 14
with open('input.txt', 'r') as file:
  lines = file.readlines()
for line in lines:
	queue = []
	start_queue_pointer = 0
	for idx, char in enumerate(line):
		if len(queue) != marker_length: queue.append(char)
		else:
			queue[start_queue_pointer] = char
			start_queue_pointer = (start_queue_pointer + 1) % marker_length
			if len(set(queue)) == marker_length:
				print(set(queue), len(set(queue)), idx+1)
				break
