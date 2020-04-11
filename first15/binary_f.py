n, *nlist = map(int, input().split())
k, *klist = map(int, input().split())
#nlist = [1, 5, 8, 12, 13, 23, 56]
#klist = [8, 1, 23, 1, 11, 12, 77]

for i in klist:
	cursor_x = 0
	cursor_y = len(nlist)
	while len(nlist[cursor_x:cursor_y]) > 0:
		#print('spec:', i, cursor_x, cursor_y, pos)
		
		#print(nlist[cursor_x:cursor_y], len(nlist[cursor_x:cursor_y]) // 2)
		
		if i == nlist[cursor_x:cursor_y][len(nlist[cursor_x:cursor_y]) // 2]:
			print(cursor_y - len(nlist[cursor_x:cursor_y]) // 2, end = ' ')
			break
		elif i > nlist[cursor_x:cursor_y][len(nlist[cursor_x:cursor_y]) // 2]:
			cursor_x += len(nlist) // 2 - 1
		else:
			cursor_y //= 2
	else:
		print(-1, end = ' ')

