def some():
    list_text=[]
    with open('text.txt', encoding = 'utf-8' ) as r:
       for i in r:
            list_text.append(i)
    return list_text        

for i in some():
    print(i.split())