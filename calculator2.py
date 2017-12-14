#!/usr/bin/env python3
import sys


def socialSecurity(income):
    social_security = income * 0.165
    return social_security


def amount(income):
    tax = income - income * 0.165 - 3500
    if tax <= 0:
        tax_amount = 0
    elif tax <= 1500:
        tax_amount = tax * 0.03 - 0
    elif 1500 < tax <= 4500:
        tax_amount = tax * 0.1 - 105
    elif 4500 < tax <= 9000:
        tax_amount = tax * 0.2 - 555
    elif 9000 < tax <= 35000:
        tax_amount = tax * 0.25 - 1005
    elif 35000 < tax <= 55000:
        tax_amount = tax * 0.3 - 2755
    elif 55000 < tax <= 80000:
        tax_amount = tax * 0.35 - 5505
    else:
        tax_amount = tax * 0.45 - 13505
    return tax_amount


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Parameter Error')
        exit()
    for avg in sys.argv[1:]:
        try:
            month_income = float(avg.split(':')[1])
        except ValueError:
            print('Parameter Error')
            exit()
        social_Security = social(month_income)
        print(social_Security)
        taxable_amount = amount(month_income)
        print(taxable_amount)
        money = month_income - social_Security - taxable_amount
        print(avg.split(':')[0] + ":" + format(money, '.2f'))
