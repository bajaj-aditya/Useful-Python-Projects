import random

print("I will generate a password for you!")

characters = 'abcdefghijklmnopqrstuvwxyz'
numbers = "0123456789"
capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "!@#$%^&*()_+=-"

#The Below code asks you as to how long you want your password to be
char_length = int(input("How many small letters do you want? "))
cap_length = int(input("How many Capital Letters you want? "))
num_length = int(input("How many numbers you want? "))
sym_length = int(input("How many symbols do you want? "))
#this defines password in a particular key
pass_char = ''
sym_pass = ''
num_pass = ''
pass_cap = ''

for i in range(char_length):
    pass_char += random.choice(characters)

for j in range(cap_length):
    pass_cap += random.choice(capital_letters)

for k in range(num_length):
    num_pass += random.choice(numbers)

for l in range(sym_length):
    sym_pass += random.choice(symbols)

unmixed_pass = pass_char + pass_cap + num_pass + sym_pass

#we will now create a list of the strings.

pass_list = list(unmixed_pass)
#After shuffling i joined it.
password = random.shuffle(pass_list)
final = ''.join(pass_list)

print("Your Password randomized is:", final)

