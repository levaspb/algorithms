import numpy as np
import math
import matplotlib.pyplot as plt

y1 = lambda n: math.log(2, np.math.factorial(n))
y2 = lambda n: 2 ** (3 * n)
y3 = lambda n: n ** (n ** 0.5)
y4 = lambda n: 2 ** (2 ** n)
y5 = lambda n: np.log2(n) ** np.log2(n)
y6 = lambda n: n ** 0.5
y7 = lambda n: np.log2(n) ** 2
y8 = lambda n: (math.log(n, 4)) ** 0.5
y9 = lambda n: math.factorial(n)
ya = lambda n: 3 ** (np.log2(n))
yb = lambda n: n ** (np.log2(n))
yc = lambda n: 2 ** n
yd = lambda n: np.log2(np.log2(n))
ye = lambda n: 4 ** n
yf = lambda n: math.log(n, 3)
yg = lambda n: 7 ** (np.log2(n))
yh = lambda n: n / math.log(n, 5)
fig = plt.subplots()
x = np.linspace(0, 10, 100)

n = 10
result = []
result.append(y1(n))
result.append(y2(n))
result.append(y3(n))
result.append(y4(n))
result.append(y5(n))
result.append(y6(n))
result.append(y7(n))
result.append(y8(n))
result.append(y9(n))
result.append(ya(n))
result.append(yb(n))
result.append(yc(n))
result.append(yd(n))
result.append(ye(n))
result.append(yf(n))
result.append(yg(n))
result.append(yh(n))

for i in range(17):
	print(i+1, result[i])

#plt.plot(x,y1(x), 'g')
#plt.plot(x,y2(x), 'b')
#plt.plot(x,y3(x), 'r')
#plt.plot(x,y4(x), 'r--')
#plt.plot(x,y5(x), 'b--')
#plt.plot(x,y6(x), 'g--')
#plt.plot(x,y7(x), '-.')
#plt.show()
