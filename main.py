import json

print("Crazy Fast ISBN Look up. Made by Tan Run En (Eric).")
data = open("DA_ISBN_TO_CLASS.json",'rb')
corpus = json.load(data)

while True:
	isbn = input("Enter ISBN or scan it:")
	try:
		for classes in corpus[isbn]:
			print(classes)
	except:
		print("Book not found. Try using mbsbooks.")