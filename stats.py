def word_count(text):		# this counts the number of words a string given to text.
        return len(text.split())

def character_count(text):	# trying to count individual characters after setting them all to lowercase
	characters = {}
	text_lower = text.lower()
	for char in text_lower:
		if char not in text_lower:
			characters[char] = 0
		if char in characters
			characters[char] += 1
	return
