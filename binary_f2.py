#nlist = [1, 5, 8, 12, 13]
#klist = [8, 1, 23, 1, 11]
nlist = [1, 2, 5, 5, 5, 8]
klist = [2, 5, 8, 8, 8, 7, 1]

def findk(l, k):
	p = 1
	while len(l) > 1:
		#print(l, k, p)
		if l[len(l) // 2] > k:
			l = l[:len(l) // 2]
		elif l[len(l) // 2] < k:
			p += len(l) // 2 + 1
			l = l[len(l) // 2 + 1:]
		else:
			p += len(l) // 2
			l = l[len(l) // 2:len(l) // 2 + 1]
			return p
	if len(l) != 0 and l[0] == k:
		return p
	else:
		return -1

def findk2(l, k, p):
	if len(l) > 1:
		if l[len(l) // 2] > k:
			l = l[:len(l) // 2]
		elif l[len(l) // 2] < k:
			p += len(l) // 2 + 1
			l = l[len(l) // 2 + 1:]
		else:
			p = len(l) // 2 + 1
			l = l[len(l) // 2:len(l) // 2 + 1]
		p = findk(l, k, p)
		return p
	else:
		if len(l) != 0 and l[0] == k:
			return p
		else:
			return -1

def main():
	#n, *nlist = map(int, input().split())
	#k, *klist = map(int, input().split())
	for i in klist:
		print(findk(nlist[:], i), end = ' ')

def test():
	assert findk([], 42) == -1
	assert findk([42], 42) == 1
	assert findk([42], 12) == -1
	
test()
main()
