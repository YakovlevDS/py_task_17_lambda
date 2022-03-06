import sys
url=['text.txt','text2.txt','text3.txt','text4.txt']
list_defect =[]
list_info =[]
for path in url:
    try:
        r=open(path)
        list_info.append(r.read())
        print('try',list_info)
    except Exception:
        list_defect.append(path)
        print('error',list_defect)
        continue
    



