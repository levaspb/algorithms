def merge2(array1, array2):
	global c
	result = []
	c = i = j = 0
	len_a = len(array1)
	for k in range(len(array1) + len(array2)):
		if array1[i] < array2[j]:
			result.append(array1[i])
			i += 1
			if i + 1 > len(array1): 
				for p in array2[j:]:
					result.append(p)
				break
		else:
			result.append(array2[j])
			j += 1
			c += len_a - i
			if j + 1 > len(array2):
				for p in array1[i:]:
					result.append(p)
				break
	#print(k, i, j, result)
	return result

def mergeCount(arrayInput): # count devided inversions
	q = [i for i in arrayInput]
	print(merge(mergeSort(q[:len(q)//2]), mergeSort(q[len(q)//2:])))
	element, count = merge(mergeSort(q[:len(q)//2]), mergeSort(q[len(q)//2:]))
	#print('el', element, count)
	'''while len(q) > 1:
		print('=======================')
		#print(q)
		print('merge:', q[0:4], q[4:])
		element, count = mergeAndCount(q[0], q[1])
		q.append(element)
		del q[0:2]'''
	return q, count	

def mergeSortAndCount(arrayInput):
	global count
	if len(arrayInput) < 2:
		return arrayInput[:]
	result = []
	m = len(arrayInput) // 2
	a = mergeSortAndCount(arrayInput[:m])
	b = mergeSortAndCount(arrayInput[m:])
	i = j = 0
	len_a = len(a)
	len_b = len(b)
	while i < len_a and j < len_b:
		if a[i] > b[j]:
			result.append(b[j])
			j += 1
			count += len_a - i
		else:
			result.append(a[i])
			i += 1
	result = result + a[i:]
	result = result + b[j:]
	return result

def mergeSort(arrayInput):
	q = [[i] for i in arrayInput]
	while len(q) > 1:
		len_a = len(q)
		for i in range(len_a - 1, 0, -2):
			q[i-1] = merge(q.pop(i), q[i-1])
	return q

def merge(a, b):
	#print('=============', b, a)
	global c
	result = []
	i = j = 0
	len_a = len(a)
	len_b = len(b)
	while i < len_a and j < len_b:
		if a[i] >= b[j]:
			result.append(b[j])
			j += 1
		else: #there is an inversion
			result.append(a[i])
			i += 1
			c += len_b - j
			#len(b[j:]print('FOUND!!!', c, len(b[j:]))
	#for i2 in range(i, len_a): result.append(a[i2])
	#for i2 in range(j, len_b): result.append(b[i2])
	result += a[i:]
	result += b[j:]
	#print('result: ', result)
	return result

def test():
	import numpy as np
	ls = np.random.randint(1, 10 ** 9, 10 ** 3)
	#print(ls)
	return ls

def naive(array):
	result = 0
	len_a = len(array)
	for i in range(len_a):
		for j in range(i+1, len_a):
			if array[i] > array[j]:
				result += 1
	return result

nlist = [2, 1]
#nlist = [1,2,3,4,5,4]
#n = int(input())
#nlist = input().split()
count = c = 0
#nlist = test()
for i in range(10):
	c = 0
	nlist = test()
	p = naive(nlist)
	mergeSort(nlist)
	if p != c:
		print(nlist)
		print(p)
		print(c)
		break
#print(c)
#mergeSortAndCount(nlist)
#print(count)