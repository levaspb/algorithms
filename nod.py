def fib(n):
    l = [0, 1]
    if n != 1:
        for i in range(2, n + 1):
		        l.append(l[i - 1] + l[i - 2])
    return l[n]

def nod(a, b):
	if a == 0 or b == 0:
		return(max(a, b))
	else:
		return nod(b % a, a)

for i in range(2, 50, 2):
	print(nod(fib(i), fib(i + 1)))
	
#a, b = map(int, input().split(' '))
