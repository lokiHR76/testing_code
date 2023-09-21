print(f'\t\t\t\t\t\t\t\t\t\tBasic calculator\n symbols for operation that is valid \n 1. Addition : " + "\t\t\t\t\t 2. Substraction : " - "\n 3. Multiplication : " * "\t\t\t\t\t 4. Divison : " / " \n 5. Double multiplication : " ** "\t\t\t\t\t 6. Double divison : " // " ')



first_digit = input('enter first digit : ')
second_digit = input('enter second digit : ')
opr = input('enter opreation symbol : ')
if opr == ('+'):
    print(int(first_digit) + int(second_digit))
elif opr == ('-'):
     print(int(first_digit) - int(second_digit))
elif opr == ('*'):
     print(int(first_digit) * int(second_digit))
elif opr == ('/'):
     print(int(first_digit) / int(second_digit))
elif opr == ('**'):
     print(int(first_digit) ** int(second_digit))
elif opr == ('//'):
     print(int(first_digit) // int(second_digit))
else:
    print('operation invalid ! ')