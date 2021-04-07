# normal
def fib(n):
	if n<=1:
		return n
	else:
		return fib(n-1)+fib(n-2)
def fib1(n,a):
	
	if a[n]!=-1:
		return a[n]
	if n<=1:
		a[n]=n
	else:
		a[n]=fib1(n-1,a)+fib1(n-2,a)
	return a[n]
k=int(input())
print(fib(k))
a=[-1]*(k+1)
#print(a)
print(fib1(k,a))