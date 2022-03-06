while True:
    try:
        enter= float(input('Enter number'))
        print(140/enter)
        break
    except ValueError:
        print('You have entered no number ')  
    except ZeroDivisionError:
        print('It is impossible to share on zero')  
    # else:
    #     print('Fine! From first  attempt')
    finally:
        print('This block Code run allways')
        
print('The End')
        
