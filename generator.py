h=[5,5,6,7,4,2,3,5,66,66]
new_h=[]
for i in h:
    new_h.append(i*3)
print(new_h) 

new_h2=[x*3 for x in h]
print(new_h2) #We generate a list

new_h3={x*3 for x in h}
print(new_h3) #generable multitude

