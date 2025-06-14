import sys

from stats import(
	word_count,
	character_count,
	character_sort,
)

if len(sys.argv) !=2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

def main ():
	book_path = sys.argv[1]
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

main()
