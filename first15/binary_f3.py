n, *nlist = map(int, input().split())
k, *klist = map(int, input().split())
#nlist = [1, 5, 8, 12, 13]
#klist = [8, 1, 23, 1, 11]

rlist = {nlist[x]: x + 1 for x in range(len(nlist))}

for i in klist:
	if i in rlist: 
		print(rlist[i], end = ' ')
	else:
		print(-1, end = ' ')
