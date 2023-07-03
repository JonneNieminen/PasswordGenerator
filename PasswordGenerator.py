import random


uppcase_letters = 'ABCDEFGHIJLMNOPQRSTUVXYZÅÄÖW'
lowcase_letters = uppcase_letters.lower()
dig = '0123456789'
sym = '()[],;:._-*¨^´+!"#¤£$&/{}'

upper, lower, nums, syms = True, True, True, True

all = ""

if upper:
    all += uppcase_letters
if lower:
    all += lowcase_letters
if nums:
    all += dig
if syms:
    all += sym

def password_generator(length=20, amount=1):
    for i in range(amount):
        password = "".join(random.sample(all, length))
        print(password)


password_generator()    