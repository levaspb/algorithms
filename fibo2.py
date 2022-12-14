n = int(input())
l = [0, 1, 1, 2, 3, 5, 8, 13]
if n > 7:
	for i in range(7, n):
		l.append((l[i] + l[i - 1]) % 10)
print(l[n])
