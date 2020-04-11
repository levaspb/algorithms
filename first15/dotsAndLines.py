def dots(lines, array):
	if len(lines) == 0:
		return array
	else:
		array.append(lines[0][1])
		del lines[0]
		while len(lines) != 0 and lines[0][0] <= array[-1]:
			del lines[0]
		return(dots(lines, array))

n = int(input())
lines = [[k, v] for k, v in (map(int, input().split()) for _ in range(n))]
lines.sort(key = lambda x: x[1])
array = []
result = dots(lines, array)
print(len(result))
for i in result:
	print(i, end = ' ')
