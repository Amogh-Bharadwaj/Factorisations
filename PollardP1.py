
from math import gcd,sqrt
import sys

# Pollard p-1 method for factoring a number N
def isPrime(n):
	if n==1:
		return False
	if n==2 or n==3:
		return True
	for i in range(2, int(sqrt(n))+1):
		if(n % i == 0):
			return False
	return True


def factorial(n):
	if n==1 or n==0:
		return 1
	fact = [1,1]
	for i in range(2,n+1):
		fact.append(i*fact[i-1])
	return fact[n]


def pollard_factor(n):
	if(isPrime(n)):
		return n

	k=1
	while True:
		div = pow(2,factorial(k),n)-1
		if(gcd(div,n)!=1):
			return gcd(div,n)
		k=k+1

				
N = int(sys.argv[1])

print("Non-trivial factor of ",N,": ", pollard_factor(N))
