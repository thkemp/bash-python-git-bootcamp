#!/Users/thkemp/anaconda/bin/python

#spits out the input at the commandline, parsing out arguments (good for debugging)
import sys

#define conversion functions that get called
#handle fahrenheit, celcius kelvin
def kelvin_to_celsius(temp):
	return temp-273.15
def celsius_to_kelvin(temp):
	return temp+273.15
def celsius_to_fahrenheit(temp):
	return temp*9.0/5 +32
def fahrenheit_to_celsius(temp):
	return (temp-32)*5.0/9






def main():
	script=sys.argv[0]
	tempinput=float(sys.argv[1])
	tempfrom=sys.argv[2]
	tempto=sys.argv[3]
	
	assert tempinput >= 0, 'temp is negative'
	assert tempfrom in ['-f','-c','-k'], 'flag 1 is not -f or -c or -k'
	assert tempto in ['-f','-c','-k'], 'flag 2 is not -f or -c or -k'
	
	
	if tempfrom == '-k':
		if tempto == '-f':
			print kelvin_to_celsius(celsius_to_fahrenheit(tempinput))
		elif tempto == '-c':
			print kelvin_to_celsius(tempinput)


if __name__ == '__main__':
	main()