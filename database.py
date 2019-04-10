import json

corpus = {}

for i in range(2,144):
    a = open(f'DA_Bookstore_Corpus{i}.json','rb')
    dip = json.load(a)
    for key,val in dip.items():
        for books in val:
            if books not in corpus:
                corpus[books] = []
            corpus[books].append(key)

b = open('DA_ISBN_TO_CLASS.json','w')
json.dump(corpus,b)