from heapq import *

n = int(input())
l = list()
h = []

for i in range(n):
	l.append(input())

for s in l:
	if s[:6] == 'Insert':
		heappush(h, int(s[7:]) * -1)
		#print(h)
	if s == 'ExtractMax':
		print(heappop(h) * -1)

