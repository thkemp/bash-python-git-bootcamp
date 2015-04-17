#!/Users/thkemp/anaconda/bin/python

#spits out the input at the commandline, parsing out arguments (good for debugging)
import sys

def main():
	i=0
	for var in sys.argv:
		print 'sys.argv[',i,'] = ',var
		i+=1

if __name__ == '__main__':
	main()