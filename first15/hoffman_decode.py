count, lenght = map(int, input().split())
table = dict()
for i in range(count):
	s, k = map(str, input().split(': '))
	table[k] = s
encoded = input()
decoded = ''

while len(encoded) >= 1:
	finished = False
	howmany = 0
	while not finished:
		howmany += 1
		if encoded[:howmany] in table:
			finished = True
	decoded += table[encoded[:howmany]]
	encoded = encoded[howmany:]

print(decoded)
