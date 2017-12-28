#!/usr/bin/env python3
import sys
from multiprocessing import Process, Queue
import getopt
import configparser
from datetime import datetime

queue1 = Queue()
queue2 = Queue()


class UserData(object):
	
	def __init__(self, user_data_file):
		self.user_data = []
		with open(user_data_file) as f:
			for i in f.readlines():
				self.user_data.append((i.strip().split(',')[0], i.strip().split(',')[1]))
	
	def get_data(self):
		queue1.put(self.user_data)
		return self.user_data
	
	@staticmethod
	def calculate(tax_config, cityname):
		Config = configparser.ConfigParser()
		Config.read(tax_config)
		values = []
		if cityname is None:
			tax_config = dict(Config['DEFAULT'])
		elif cityname.upper() in Config:
			tax_config = dict(Config[cityname.upper()])
		else:
			raise KeyError
		jishul = float(tax_config.get('jishul'))
		jishuh = float(tax_config.get('jishuh'))
		rate = float(tax_config.get('yanglao')) + float(tax_config.get('yiliao')) + float(tax_config.get('shiye')) + float(tax_config.get('gongshang')) + float(tax_config.get('shengyu')) + float(tax_config.get('gongjijin'))
		user_list = queue1.get()
		for i in user_list:
			ic = int(i[1])
			if ic < jishul:
				ss = jishul * rate
			elif jishul < ic < jishuh:
				ss = ic * rate
			else:
				ss = jishuh * rate

			tax = ic - ss - 3500
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
			after_tax = ic - ss - tax_amount
			t = datetime.now()
			t1 = datetime.strftime(t, '%Y-%m-%d %H:%M:%S')
			values.append((i[0], str(i[1]), format(ss, '.2f'), format(tax_amount, '.2f'), format(after_tax, '.2f'), t1))
		queue2.put(values)

	def get_value(self):
		return self.values
	
	@staticmethod
	def dump_to_file(output_file):
		values = queue2.get()
		with open(output_file, 'w') as f:
			for t in values:
				f.write(','.join(t)+'\n')
	
		
if __name__ == "__main__":
	try:
		opts, args = getopt.getopt(sys.argv[1:], 'C:c:d:o:h', 'help')
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
		for o1, a1 in opts:
			if o1 in ('-h', '--help'):
				print('Usage: calculator.py -C cityname -c configfile -d userdata -o resultdata')
			elif o1 == '-C':
				cityname = a1
			elif o1 == '-c':
				configfile = a1
			elif o1 == '-d':
				userdata = a1
			elif o1 == '-o':
				resultdata = a1
			else:
				raise ValueError
		user = UserData(userdata)
		Process(target=user.get_data).start()
		Process(target=user.calculate, args=(configfile, cityname,)).start()
		Process(target=user.dump_to_file, args=(resultdata,)).start()
