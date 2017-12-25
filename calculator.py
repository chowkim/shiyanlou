#!/usr/bin/env python3
import sys
from collections import namedtuple

IncomeTaxQuickLookupItem = namedtuple(
	'IncomeTaxQuickLookupItem',
	['taxable_amount', 'tax_rate', 'calculating_deduction']
)

INCOME_TAX_START_POINT = 3500
INCOME_TAX_QUICK_LOOKUP_TABLE = [
	IncomeTaxQuickLookupItem(80000, 0.45, 13505),
	IncomeTaxQuickLookupItem(55000, 0.35, 5505),
	IncomeTaxQuickLookupItem(35000, 0.30, 2755),
	IncomeTaxQuickLookupItem(9000, 0.25, 1005),
	IncomeTaxQuickLookupItem(4500, 0.20, 555),
	IncomeTaxQuickLookupItem(1500, 0.10, 105),
	IncomeTaxQuickLookupItem(0, 0.03, 0)
]


def cal_taxable_amount(incomes):
	taxable_income = incomes - INCOME_TAX_START_POINT
	if taxable_income <= 0.00:
		return 0.00
	for item in INCOME_TAX_QUICK_LOOKUP_TABLE:
		if taxable_income > item.taxable_amount:
			tax = taxable_income * item.taxable_amount - item.calculating_deduction
			return '{:.2f}'.format(tax)

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print("Parameter Error")
	try:
		income = int(sys.argv[1])
	except ValueError:
		print("Parameter Error")
		exit()
	finally:
		print(cal_taxable_amount(income))
