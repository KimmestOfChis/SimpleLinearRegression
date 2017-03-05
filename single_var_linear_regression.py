from numpy import *

def cost_function(a_zero, a_one, data):
    totalError = 0
    for i in range(0, len(data)):
        x = data[i,0]
        y = data[i, 1]
        totalError += (y - (a_one * x + a_zero)) ** 2
    return totalError/ len(data * 2)

def step_gradient(a_zero_current, a_one_current, data, learningRate):
    a_zero_gradient = 0
    a_one_gradient = 0
    N = float(len(data))
    for i in range(0, len(data)):
        x = data[i, 0]
        y = data[i, 1]
        a_zero_gradient += -(2/N) * (y - ((a_one_current * x) + a_zero_current))
        a_one_gradient += -(2/N) * x * (y - ((a_one_current * x) + a_zero_current))
    new_a_zero = a_zero_current - (learningRate * a_zero_gradient)
    new_a_one = a_one_current - (learningRate * a_one_gradient)
    return [new_a_zero, new_a_one]

def gradient_descent_runner(data, starting_a_zero, starting_a_one, learning_rate, num_iterations):
    a_zero = starting_a_zero
    a_one = starting_a_one
    for i in range(num_iterations):
        a_zero, a_one = step_gradient(a_zero, a_one, array(data), learning_rate)
    return [a_zero, a_one]

def main():
    data = loadtxt('ex1data1.txt', delimiter = ',')

    initial_a_one = 0 # we will guess zero and let the computer do the heavy lifting
    initial_a_zero = 0 #same

    num_iterations = 1000 #how much do we want to train this model?
                      #We only have 97 data points, so not too extensively

    learning_rate = 0.0001 #the steps we're taking towards the optimum
  
    print "When we started our value were as follows: a(0) = {0}, a(1) = {1}, error = {2}".format(initial_a_zero, initial_a_one, cost_function(initial_a_zero, initial_a_one, data))
    [a_zero, a_one] = gradient_descent_runner(data, initial_a_zero, initial_a_one, learning_rate, num_iterations)
    print "After {0} iterations, we found got a(0) = {1}, a(1) = {2}, error = {3}".format(num_iterations, a_zero, a_one, cost_function(a_zero, a_one, data))


if __name__ == '__main__':
    main()