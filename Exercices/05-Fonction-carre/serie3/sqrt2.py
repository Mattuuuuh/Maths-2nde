def f(x):
	return x**2 - 7

precision = 10**-2

def racine(a, b):
	if b-a < precision:
		return a, b
	m = (a+b)/2
	if f(m)> 0:
		return racine(a,m)
	return racine(m,b)
	
a, b = racine(0, 3)
print('a = ', a)
print('b = ', b)
