## Project Euler problems 1,2,3
## jacquiunciano, Viridian

## Problem 1: Multiples of 3 or 5
sol1 = sum(x for x in range(1000) if (x%3==0 or x%5==0))
print(sol1)
## sol1 = 233168

## Problem 2: Even Fibonacci Numbers
sol2 = 0
x = 1
y = 2
while x <= 4000000:
    if x%2==0:
        sol2+=x
    x,y=y,x+y
print(sol2)
## sol2 = 4613732

## Large Prime Factor
import numpy as np

def sm_pm(n):
	assert n >= 2
	for i in range(2, int(np.sqrt(n)) + 1):
		if n % i == 0:
			return i
	return n 

def function():
    n = 600851475143
    while True:
        p = sm_pm(n)
        if p<n:
            n//=p
        else:
            return n
print(function())
## sol3 = 6857

## Histograms
## Binomial
import matplotlib.pyplot as plt
import numpy as np
bi = np.random.binomial(10,0.5,10000)
plt.hist(bi)
plt.show()
## Poisson
pois = np.random.poisson(1,10000)
plt.hist(pois)
plt.show()
## Normal
norm = np.random.normal(0,1,10000)
plt.hist(norm)
plt.show()
## Uniform
uni = np.random.uniform(0,1,10000)
plt.hist(uni)
plt.show()
## Chi Square
cs = np.random.chisquare(1,10000)
plt.hist(cs)
plt.show()

## Testing Central N Theorm with Binomial and Normal Dist.
import matplotlib.pyplot as plt
import numpy as np
bi1 = np.random.binomial(10,0.5,10)
plt.subplot(3, 2, 1)
plt.hist(bi1)
bi2 = np.random.binomial(10,0.5,100)
plt.subplot(3, 2, 2)
plt.hist(bi2)
bi3 = np.random.binomial(10,0.5,1000)
plt.subplot(3, 2, 3)
plt.hist(bi3)
bi4 = np.random.binomial(10,0.5,10000)
plt.subplot(3, 2, 4)
plt.hist(bi4)
bi5 = np.random.binomial(10,0.5,100000)
plt.subplot(3, 2, 5)
plt.hist(bi5)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
norm1 = np.random.normal(0,1,10)
plt.subplot(3, 2, 1)
plt.hist(norm1)
norm2 = np.random.normal(0,1,100)
plt.subplot(3, 2, 2)
plt.hist(norm2)
norm3 = np.random.normal(0,1,1000)
plt.subplot(3, 2, 3)
plt.hist(norm3)
norm4 = np.random.normal(0,1,10000)
plt.subplot(3, 2, 4)
plt.hist(norm4)
norm5 = np.random.normal(0,1,100000)
plt.subplot(3, 2, 5)
plt.hist(norm5)
plt.show()