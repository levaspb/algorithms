'''
Первая строка содержит количество предметов 1≤n≤103 и вместимость рюкзака 0≤W≤2⋅106. Каждая из следующих n строк задаёт стоимость 0≤ci≤2⋅106 и объём 0<wi≤2⋅106предмета (n, W, ci, wi — целые числа). Выведите максимальную стоимость частей предметов (от каждого предмета можно отделить любую часть, стоимость и объём при этом пропорционально уменьшатся), помещающихся в данный рюкзак, с точностью не менее трёх знаков после запятой.
'''

def price(W, cw, result):
	if W == 0 or len(cw) == 0:
		return(result)
	elif cw[0][1] > W:
		result += (cw[0][0] / cw[0][1]) * W
		return(result)
	else:
		result += cw[0][0]
		W -= cw[0][1]
		del cw[0]
		return(price(W, cw, result))

n, W = map(int, input().split(' '))
cw = [[k, v] for k, v in (map(int, input().split()) for _ in range(n))]
cw.sort(key = lambda x: x[0] / x[1], reverse=True)
result = 0
print('{:f}'.format(price(W, cw, result)))
