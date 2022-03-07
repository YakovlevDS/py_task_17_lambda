def decor(f):
    print('Code decor')
    f()
    print('Code 2 decor')



@decor #make=decor(make)
def make():
    enter=input('Enter somesing...')
    print(enter)


# make()
