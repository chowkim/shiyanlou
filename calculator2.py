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

SOCIAL_SECURITY_FEES = {
	'old-age_insurance': 0.08,
	'medical_insurance': 0.02,
	'unemployment_insurance': 0.005,
	'work-related_injury_insurance': 0.00,
	'maternity_insurance': 0.00,
	'provident_fund': 0.06
}


def cal_taxable_amount(incomes):
	five_risks_one_gold = incomes * sum(SOCIAL_SECURITY_FEES.values())
	real_income = incomes - five_risks_one_gold
	income_taxable = real_income - INCOME_TAX_START_POINT
	if income_taxable <= 0:
		return '0.00', '{:.2f}'.format(real_income)
	for item in INCOME_TAX_QUICK_LOOKUP_TABLE:
		if income_taxable > item.taxable_amount:
			tax = income_taxable * item.tax_rate - item.calculating_deduction
			return '{:.2f}'.format(tax), '{:.2f}'.format(real_income - tax)


if __name__ == '__main__':
	for avg in sys.argv[1:]:
		employee_id, income_string = avg.split(':')
		try:
			income = int(income_string)
		except ValueError:
			print('Parameter Error')
		finally:
			_, after_tax_salary = cal_taxable_amount(income)
			print('{}:{}'.format(employee_id, after_tax_salary))
