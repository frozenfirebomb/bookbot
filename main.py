def main ():
	book_path = "books/frankenstein.txt"
	text = get_book_text(book_path)

	print("============ BOOKBOT ============")
	print("Analyzing book found at", book_path +"...")
	print("----------- Word Count ----------")
	print("Found", word_count(text), "total words")
	print("--------- Character Count -------")
	for character in character_sort(character_count(text)):
		if character["char"].isalpha():
			print(character["char"]+":",character["num"])
	print("============= END ===============")

def get_book_text(fp):        #this function returns the contents of a file as a string from a file path provided as a string
	with open(fp) as f:
		file_contents = f.read()
	return file_contents

from stats import word_count

from stats import character_count

from stats import character_sort

main()
