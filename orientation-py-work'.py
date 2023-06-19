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