import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
symbols = "-!@#"

upper, lower, num, syms = True, True, True, True

all = ""

if upper:
    all += uppercase_letters

if lower:
    all += lowercase_letters

if num:
    all += digits

if syms:
    all += symbols

length = 16
amount = 1

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)
