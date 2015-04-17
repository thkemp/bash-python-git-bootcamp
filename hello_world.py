#!/usr/bin/python


import random
import matplotlib.pyplot as plt #matlab-style plotting module
import csv

def main():
	print "hello world!"
		
	with open('output.csv','wb') as fp:
		a=csv.writer(fp,delimiter=',')
		for i in range(1000):
			mylist=[]
			mylist.append(random.randint(1,10))
			a.writerow(mylist)
				
	randnums=[]
	with open('output.csv','rb') as fp:
		a=csv.reader(fp,delimiter=',')
		for row in a:
			randnums.append(int(row[0]))

#    plt.plot(randnums)
	plt.hist(randnums)
	plt.show()

if __name__ == '__main__':
	main()