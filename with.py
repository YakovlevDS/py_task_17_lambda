# r=open('file.txt','a')
# r.write('hello my dear \n')
# 2/0
# r.write('friend!')
# r.close()
# print('Good!')



# with open('file.txt','a') as r: #To save data in case of error in the middle of the block
#     r.write('hello my dear \n')
#     2/0   # Write all that was before mistake
#     r.write('friend!')
# print('Good!')


r=open('file.txt','a')
try:
    r.write('hello my dear \n')
    2/0
    r.write('friend!')
finally: # the same effect that an example above
    r.close()
print('Good!')

 






