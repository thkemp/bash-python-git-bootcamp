#python code to calculate BMI

w= raw_input("Enter Weight (in pounds): ")
h=raw_input("Enter Height (in inches): ")
#using pounds and inches
bmi=(float(w)/float(h)**2)*703
print 'BMI is: ',round(bmi,1)

