import json

print("Crazy Fast ISBN Look Up program.For Spring 2019 only.Made by Tan Run En (Eric).")
data = open("DA_ISBN2CLASS3.json",'rb')
corpus = json.load(data)

while True:
	isbn = int(input("Enter ISBN or scan it:")[3:-1])

	if str(isbn) in corpus:
		for classes in corpus[str(isbn)]:
			print(classes)
	elif str(isbn-1) in corpus:
		for classes in corpus[str(isbn-1)]:
			print(classes)
	elif str(isbn+1) in corpus:
		for classes in corpus[str(isbn-1)]:
			print(classes)
	else:
		print("Book not found. Try using mbsbooks ARC5")