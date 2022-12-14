# put your python code here
def pli(n, array, pos):
	if n == pos:
		array.append(pos)
		return(array)
	elif n == 0:
		print('n=0')
		return array
	elif n >= pos * 2 + 1:
		array.append(pos)
		n -= pos
		pos += 1
		#print(n, pos)
		return(pli(n, array, pos))
	else:
		pos += 1
		return(pli(n, array, pos))

n = int(input())
array = []
pos = 1
d = pli(n, array, pos)
print(len(d))
for i in d:
	print(i, end = ' ')
print()
