import json

print("Crazy Fast ISBN Look Up program. For Spring 2019 only. Made by Tan Run En (Eric).")
data = open("DA_ISBN2CLASS.json",'rb')
corpus = json.load(data)

while True:
	isbn = int(input("Enter ISBN or scan it:"))
	try:
		try:
			for classes in corpus[str(isbn)]:
				print(classes)
		except:
			for classes in corpus[str(isbn+1)]
				print(classes)
	except:
		print("Book not found. Try using mbsbooks.")