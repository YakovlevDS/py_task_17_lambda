# from dis import dis
# def some(x):
#     return x/5

# var = lambda z: z/5 

# print (some(4))
# print (dis(some))
# print (dis(var))
# print (var(4))

list_of=[["Jon",23],["acj",20],["Tom",2]]
# r= sorted(list_of,key=lambda x:x[1])
# print (r)


x = list(filter(lambda x:x[1]>19, list_of))
print (x)
