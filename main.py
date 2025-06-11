def main ():
        print(get_book_text("books/frankenstein.txt"))
        pass

def get_book_text(fp):
	with open(fp) as f:
		file_contents = f.read()
	return file_contents

main()
