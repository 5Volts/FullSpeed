import json

# corpus = {}
#
# for i in range(2,144):
#     a = open(f'DA_Bookstore_Corpus{i}.json','rb')
#     dip = json.load(a)
#     for key,val in dip.items():
#         for books in val:
#             if books not in corpus:
#                 corpus[books] = []
#             corpus[books].append(key)

b = open('DA_ISBN_TO_CLASS.json','rb')
corpus = json.load(b)
for keys, value in corpus.items():
    corpus[keys] =list(dict.fromkeys(corpus[keys]))
# print(list(dict.fromkeys(corpus['9781337694933'])))

c = open('DA_ISBN2CLASS.json','w')
json.dump(corpus,c)