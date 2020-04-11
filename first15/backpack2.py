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
