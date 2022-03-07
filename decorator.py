def decor(f):
    def wrapper():

        print('Code decor')
        f()         # The body function(def make) is started here. 
        print('Code 2 decor')
    return wrapper


@decor #make=decor(make)
def make():
    enter=input('Enter somesing...')
    print(enter)

print('start')
make()
# decor This poundation is wrapping the necessary function. To simplify the code of each function.