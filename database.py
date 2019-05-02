import json

corpus = {}

# 9781337109680
# 2901337109689

for i in range(1,257):
    a = open(f'Backup+Title/DA_Bookstore_Corpus{i}.json','rb')
    dip = json.load(a)
    for classe,booksandtitle in dip.items():
        for books in booksandtitle:
            book = books[0][3:-1]
            title = books[1]

            isbn_and_title = book+ " " + title
            # print(isbn_and_title)
            if isbn_and_title not in corpus:
                corpus[isbn_and_title] = []
            if classe[-1] == 'n':
            	classe = classe[:-2]
            corpus[isbn_and_title].append(classe)

for booktitle, classes in corpus.items():
    corpus[booktitle] =list(dict.fromkeys(corpus[booktitle]))
# print(list(dict.fromclasses(corpus['9781337694933'])))

c = open('DA_ISBN2CLASS4.json','w')
json.dump(corpus,c)
