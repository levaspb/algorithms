def pli(n, array, pos):
	while n != pos:
		if pos * 2 + 1 <= n:
			array.append(pos)
			n -= pos
			pos += 1
		else:
			pos += 1
	array.append(pos)
	return array
	
def pli2(n):
	return n 

n = int(input())
array = []
pos = 1

for i in range(1, 101):
	array.clear()
	pos = 1
	print(i, len(pli(i, array, pos)))

d = pli(n, array, pos)
print(len(d))
for i in d:
	print(i, end = ' ')
print()
