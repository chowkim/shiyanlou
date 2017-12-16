#!/usr/bin/env python3
import sys

def get_config(file):
    dic = dict()
    with open(file) as f:
        for i in f.readlines():
            key, value = (i.strip().split(' = ')[0]), (i.strip().split(' = ')[1])
            dic[key] = value
        return dic


def user_data(file):
    dit = dict()
    with open(file) as fi:
        for j in fi.readlines():
            print(j)
            key, value = (j.strip().split(',')[0]), (j.strip().split(',')[1])
            dit[key] = value
        return dit


def social(i):
    args = sys.argv[1:]
    index = args.index('-c')
    cfg_file = args[index + 1]
    test_cfg = get_config(cfg_file)
    jishul = float(test_cfg['JiShuL'])
    jishuh = float(test_cfg['JiShuH'])
    if i < jishul:
		#print('i1:', i)
        sc_money = jishul * 0.165
    elif jishul < i < jishuh:
        sc_money = i * 0.165
    else:
        sc_money = jishuh * 0.165
    return sc_money


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


def dump_to_file(content):
    args = sys.argv[1:]
    index = args.index('-o')
    write_file = args[index + 1]
    with open(write_file, "w") as f:
        for t in content:
            f.write(','.join(t)+'\n')
			

if __name__ == '__main__':
    args = sys.argv[1:]
    index1 = args.index('-d')
    user_file = args[index1 + 1]
    userData = user_data(user_file)
    values = []
    for key, value in userData.items():
        i = int(value)
        sc = social(i)
        tax = amount(i)
        after_tax = i - sc - tax
        values.append((key, value, format(sc, '.2f'), format(tax, '.2f'), format(after_tax, '.2f')))
        dump_to_file(values)
