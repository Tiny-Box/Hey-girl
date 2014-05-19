import argparse

_default = dict(
	logfile = 'spider.log',
	loglevel = 3,
	threadNum = 10,
	keyword = ''
	)
	
def positiveInt(rawValue):
	errorInfo = "Must be a positive integer."
	try:
		value = int(rawValue)
	except ValueError:
		raise argparse.ArgumentTypeError(errorInfo)
	if value < 1:
		raise argparse.ArgumentTypeError(errorInfo)
	else:
		return value
		
def url(rawValue):
	if not rawValue.startswith('http'):
		value = 'http://' + rawValue
	return value
	
parser = argparse.ArgumentParser(description='A Web crawler for Knownsec')

parser.add_argument('-n', type=positiveInt, required=True, metavar='NUMBER', dest='number', help='Specify the number of picture you want')

parser.add_argument('--logfile', type=str, metavar='FILE', default=_default['logfile'], dest='logFile',
					help='The log file path, Default: %s' %_default['logfile'])
parser.add_argument('--loglevel', type=int, choices=[1, 2, 3, 4, 5], default=_default['loglevel'], dest='loglevel',
					help='The level of logging details. Larger number record more details. Default:%d' %_default['loglevel'])
parser.add_argument('--thread', type=positiveInt, metavar='NUM', default=_default['threadNum'], dest='threadNum',
					help='The amount of threads. Default:%d' %_default['threadNum'])

def main():
	args = parser.parse_args()
	print args
	
if __name__ == '__main__':
	main()