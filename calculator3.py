#!/usr/bin/env python3
import sys


class Config(object):
	def __init__(self, configfile):
		self._config = {}
		with open(configfile) as f:
		for i in f.readlines():
				key1, value1 = (i.strip().split(' = ')[0]), float(i.strip().split(' = ')[1])
				self._config[key1] = value1

	def get_config(self, name):
		return self._config.get(name)


class UserData(object):
	
	def __init__(self, user_data_file):
		self.user_data = {}
		with open(user_data_file) as f:
			for i in f.readlines():
				key2, value2 = (i.strip().split(',')[0], float(i.strip().split(',')[1]))
				self.user_data[key2] = value2
	
	def get_data(self):
		return self.user_data
	
	def calculate(self, config, userdata, outputfile):
		values = []
		jishul = float(config.get_config('JiShuL'))
		jishuh = float(config.get_config('JiShuH'))
		user_dict = userdata.get_data()
		for key, value in user_dict.items():
			if value < jishul:
				ss = jishul * 0.165
			elif jishul < value < jishuh:
				ss = value * 0.165
			else:
				ss = jishuh * 0.165
			tax = value - value * 0.165 - 3500
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
			after_tax = value - ss - tax_amount
			values.append((key, str(int(value)), format(ss, '.2f'), format(tax_amount, '.2f'), format(after_tax, '.2f')))
		userdata.dumptofile(values, outputfile)
		
	def dumptofile(self, values, outputfile):
			with open(outputfile, 'w') as f:
				for t in values:
					f.write(','.join(t)+'\n')

if __name__ == "__main__":
	args = sys.argv[1:]
	try:
		test_cfg = args[args.index('-c') + 1]
		user_csv = args[args.index('-d') + 1]
		wage_csv = args[args.index('-o') + 1]
	except IOError:
		print('No Such a file!')
		sys.exit()
	except ValueError:
		print('Parameter Error')
		sys.exit()
	except NameError:
		print('Please try your name!')
		sys.exit()
	finally:
		config = Config(test_cfg)
		user = UserData(user_csv)
		user.calculate(config, user, wage_csv)

