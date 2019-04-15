import json

corpus = {}

# 9781337109680
# 2901337109689

for i in range(1,252):
    a = open(f'FullSpeed/DA_Bookstore_Corpus{i}.json','rb')
    dip = json.load(a)
    for key,val in dip.items():
        for books in val:
            books = books[3:-1]
            if books not in corpus:
                corpus[books] = []
            if key[-1] == 'n':
            	key = key[:-2]
            corpus[books].append(key)

for keys, value in corpus.items():
    corpus[keys] =list(dict.fromkeys(corpus[keys]))
# print(list(dict.fromkeys(corpus['9781337694933'])))

c = open('DA_ISBN2CLASS2.json','w')
json.dump(corpus,c)
