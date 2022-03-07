# def decor(f):
#     def wrapper():

#         print('Code decor')
#         f()         # The body function(def make) is started here. 
#         print('Code 2 decor')
#     return wrapper


# @decor #make=decor(make)
# def make():
#     enter=input('Enter somesing...')
#     print(enter)

# print('start')
# make()
# decor This poundation is wrapping the necessary function. To simplify the code of each function.



def decor(f):
    def wrapper():
        try:
            h=f() 
        except Exception: 
            print('Repeat input...')
            h=f()         
        return h
    return wrapper


@decor #make=decor(make)
def make():
    enter=float(input('Enter number: '))
    return enter
@decor #make2=decor(make2)
def make2():
    enter=float(input('Enter number next: '))
    return enter

make2()
make()