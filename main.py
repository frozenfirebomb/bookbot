def main ():
	book_path = "books/frankenstein.txt"
	text = get_book_text(book_path)
	print(word_count(text), "words found in the document")
	pass

def get_book_text(fp):        #this function returns the contents of a file as a string from a file path provided as a string
	with open(fp) as f:
		file_contents = f.read()
	return file_contents

from stats import word_count

main()
