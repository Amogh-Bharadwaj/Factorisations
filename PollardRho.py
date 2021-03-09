from math import gcd
import sys

#Pollard Rho factorisation
def f(x):
	return pow(x,2)+1

def fill_x():
	for i in range(1,k):
		xk.append(f(xk[i-1])%n)

def pollard_rho(n):
	for i in xk:
		for j in xk:
			if(gcd(abs(i-j),n)!=1 and j!=i):
				print("Non-trivial factor: ", gcd(abs(i-j),n))
				return 1

n= int(sys.argv[1])
k = 100 #increase this value to increase chances for factoring
xk = [f(1)]
fill_x()
pollard_rho(n)
