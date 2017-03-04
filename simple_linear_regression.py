from numpy import loadtxt
import matplotlib.pyplot as plt

data = loadtxt('ex1data1.txt', delimiter = ',')


#two empty arrays
x = []
y = []

#iterate through 'data' with a for loop
#.append acts like .push in other languages 
#we will add our first element 'i[0]'' to the x array of x values'
#we will add our second element 'i[1]'' to the y array of y values'
for i in data:
	x.append(i[0])
	y.append(i[1])

plt.scatter(x, y)
plt.xlabel('City Population')
plt.ylabel('Profit in $10,000')
plt.show()