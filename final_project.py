#!/Users/thkemp/anaconda/bin/python

import sys
#so that we can read command line argument at sys.argv[1]
import math
import random
#so that we can generate random numbers (temperature fluctuations)
import csv
#so that we can write to and read from csv file
import matplotlib.pyplot as plt
#so that we can plot numbers


def f2c(temp):
	return (temp-32)*5.0/9

def main():
#	read in argument (number of lines to read out of file)
	numlines=int(sys.argv[1])
	print 'Number of lines to read: ', numlines

# go ahead and make a file of random temperatures
	with open('temperature_data.csv','wb') as filename:
		for i in range(1000):
			csv.writer(filename,delimiter=',').writerow([int(50+30*math.sin(i*0.02)+random.randint(-5,5))])

#read numlines rows from csv file I just made
	inputdata=[]
	with open('temperature_data.csv','rb') as filename:
		for row in range(numlines):
			inputdata.append(int(csv.reader(filename,delimiter=',').next()[0]))
#assuming integer input

#convert to celsius (assuming numbers are in fahrenheit)
	for value in range(len(inputdata)):
		inputdata[value]=f2c(inputdata[value])
#	print inputdata
#store those numbers

#plot the numbers
	plt.plot(inputdata)
	plt.show()



#required (apparently) to make main run when this is called from bash command line
if __name__ == '__main__':
	main()