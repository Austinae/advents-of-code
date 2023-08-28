from collections import defaultdict

directory_stack = []
files = defaultdict(int)
while True:
	try:
		match input().split():
			case ['$', 'cd', '..']:
				directory_stack.pop()
			case ['$', 'cd', p]:
				directory_stack.append(p)
			case ['$', 'ls']:
				pass
			case ['dir', p]:
				pass
			case [s, f]:
				files[tuple(directory_stack)] += int(s)
				curr_path = directory_stack[:-1]
				while curr_path:
					files[tuple(curr_path)] += int(s)
					curr_path.pop()
	except EOFError:
		#first star
		#print(sum([size for size in files.values() if size <= 100000]))
		#second star
		print(min([size for size in files.values() if size >= files.get(('/',))-40000000]))
		break
