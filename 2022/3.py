#first star
# characters_sum = 0
# while True:
# 	try:
# 		rucksacks_content = input()
# 		swivel_index = int(len(rucksacks_content)/2)
# 		seen_characters = set(rucksacks_content[:swivel_index])

# 		for character in rucksacks_content[swivel_index:]:
# 			if character in seen_characters:
# 				characters_sum += ord(character)-96 if character.islower() else ord(character)-38
# 				break
# 	except EOFError:
# 		print(characters_sum)
# 		break

#second star

the_sum = 0
rucksacks_count = 0
a = set()
while True:
	try:
		if rucksacks_count % 3 == 0:
			a = set(input())
		else:
			a = set(a).intersection(set(input()))
			if (rucksacks_count + 1) % 3 == 0:
				the_char = list(a)[0]
				the_sum += ord(the_char)-96 if the_char.islower() else ord(the_char)-38
		rucksacks_count += 1
	except EOFError:
		print(the_sum)
		break

