TASK-3

import random
print("welcome to the password generation!!!")
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']

UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','(',')','*','!']
no_upperletters=int(input("enter the no of uppercase letters do you want"))
no_lowerletters=int(input("enter the no of lower letters do you want"))
no_digits=int(input("enter the no of digits do you want"))
no_symbols=int(input("enter the no of symbols do you want"))
password_list=[]
for i in range(0,no_upperletters):
    upper_case_letters=random.choice(UPCASE_CHARACTERS)
    password_list+=upper_case_letters
for i in range(0,no_lowerletters):
    lower_case_letters=random.choice(LOCASE_CHARACTERS)
    password_list+=lower_case_letters
for i in range(0,no_digits):
    digits=random.choice(DIGITS)
    password_list+=digits
for i in range(0,no_symbols):
     symbols=random.choice(SYMBOLS)
     password_list+=symbols
print(password_list)
random.shuffle(password_list)
print(password_list)
password=" "
for i in password_list:
    password+=i
print ( "This is your password:",password)
