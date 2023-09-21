print('what is your name ? ')
name = input()
print(f'what is your gender ? \n(in small letters without any space )')
gender = input()
if gender == ('female'):
    print(f'Are you married ? \n(yes or no)')
    married = input()
    if married == ('yes'):
        print(f'Hello Mrs.{name}, \nHope you are doing well.')
    elif married == ('no'):
        print(f'Hello Ms.{name}, \nHope you are doing well.')
    else:
             print(f'sorry!!,\nUnidnetified marital status !')
elif gender == ('male'):
    print(f'Hello Mr.{name}, \nHope you are doing well.')
elif gender ==('transgender'):
    print(f'Hello Mx.{name}, \nHope you are doing well.')      
else :
    print(f'sorry!!,\nUnidentified gender !')        