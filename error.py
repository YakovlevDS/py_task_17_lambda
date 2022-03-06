import sys
url=['text.txt','text2.txt','text3.txt','text4.txt']
list_defect =[]
list_info =[]
# for path in url:
#     try:
#         r=open(path)
#         list_info.append(r.read())
#         print('try',list_info)
#     except Exception:
#         list_defect.append(path)
#         print('error',list_defect)
      #   sys.exit# If you do not count the error leave the system
#         continue

try:
    for path in url:
        try:
            r=open(path)
            list_info.append(r.read())
            print('try',list_info)
        except Exception:
            list_defect.append(path)
            print('error',list_defect)
            continue
finally:
    save=open('save.txt','a')
    for i in list_info:
        save.write(f'{i}\n')
    save.write(str(f'With Errors {list_defect}\n')) 
    save.close() 
    print('All data saved', save)  






