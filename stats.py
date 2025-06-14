def word_count(text):		# this counts the number of words a string given to the value text.
        return len(text.split())

def character_count(text):	# counts individual characters after setting them all to lowercase
	characters = {}
	text_lower = text.lower()
	for char in text_lower:
		if char not in characters:
			characters[char] = 0
		if char in characters:
			characters[char] += 1
	return characters

def character_sort(character_count):
	list_of_character_dicts = []
	for char in character_count:
		character_dict = {}
		character_dict["char"] = char
		character_dict["num"] = character_count[char]
		list_of_character_dicts.append(character_dict)
	return list_of_character_dicts

