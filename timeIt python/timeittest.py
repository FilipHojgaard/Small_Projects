from timeit import default_timer as timer
import matplotlib.pyplot as plt
import sys

fib_min = int(sys.argv[1])
fib_max = int(sys.argv[2])



def fib(n):
    if (n == 0 or n == 1):
        return n
    else:
        return fib(n-1)+fib(n-2)

time_data = []

for i in range(fib_min, fib_max):
    startTime = timer()
    print(fib(i))
    endTime = timer()
    time_data.append(endTime-startTime)

print(time_data)
plt.plot(time_data)
plt.title("Fibbonacci time data")
plt.show()
