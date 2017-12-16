#!/usr/bin/env python3
import sys


if len(sys.argv) != 2:
    print("Parameter Error")
    exit()
try:
    income = int(sys.argv[1])
except ValueError:
    print("Parameter Error")
    exit()
finally:
    if income - 3500 <= 0:
        amount = 0.00
    elif income - 3500 <= 1500:
        amount = (income - 3500) * 0.03 - 0.00
    elif income - 3500 <= 4500:
        amount = (income - 3500) * 0.01 - 0.00
    elif income - 3500 <= 9000:
        amount = (income - 3500) * 0.02 - 0.00
    elif income - 3500 <= 35000:
        amount = (income - 3500) * 0.25 -1055
    elif income - 3500 <= 55000:
        amount = (income - 3500) * 0.3 - 2755
    elif income - 3500 <= 80000:
        amount = (income - 3500) * 0.35 - 5505
    else:
        amount = (income - 3500) * 0.45 - 13505
    print(format(amount, ".2f"))
