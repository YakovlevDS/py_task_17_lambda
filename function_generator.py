# def some():
#     list_text=[]
#     with open('text.txt', encoding = 'utf-8' ) as r:
#        for i in r:
#             list_text.append(i)
#     return list_text        



def some():
    with open('text.txt', encoding = 'utf-8' ) as r:
        for x in r:
            yield x

for i in some():
    print(i.split())