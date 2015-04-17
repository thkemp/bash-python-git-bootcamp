#!/Users/thkemp/anaconda/bin/python
#location of executable


def k2f(ktemp=273):
	ftemp=k2c(ktemp)*9.0/5+32
	return ftemp

def k2c(ktemp=273):
	ctemp=ktemp-273
	return ctemp

def main():
	print "kelvin to celsius:"
	print k2c(300)
	print "kelvin to F:"
	print k2f(300)




if __name__ == '__main__':
	main()