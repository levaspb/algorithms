s = input()

tree = list()
letters = {char: s.count(char) for char in s}
for i, j in letters.items():
	tree.append([i, j])
tree.sort(key = lambda x: x[1], reverse = True)

table = dict()
if len(tree) == 1:
	table[tree[0][0]] = '0'
while len(tree) > 1:
	new_node = [tree[-1][0] + tree[-2][0], tree[-1][1] + tree[-2][1]]
	tree.insert(0, new_node)
	for i in tree[-2][0]:
		table[i] = '1' + table.get(i, '')
	for i in tree[-1][0]:
		table[i] = '0' + table.get(i, '')
	del tree[-1]; del tree[-1]
	tree.sort(key = lambda x: x[1], reverse = True)

coded = str()
for i in s:
	coded	+= table[i]

print(len(table), len (coded))
for i, j in table.items():
	print(i, ': ', j, sep = '')
print(coded)
