def main ():
	book_path = "books/frankenstein.txt"
	text = get_book_text(book_path)
	print(word_count(text), "words found in the document")
	#print(character_count(text))
	print(character_sort(character_count(text)))
	
pass

def get_book_text(fp):        #this function returns the contents of a file as a string from a file path provided as a string
	with open(fp) as f:
		file_contents = f.read()
	return file_contents

from stats import word_count

from stats import character_count

from stats import character_sort

main()
