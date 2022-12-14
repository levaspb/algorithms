import numpy as np
import math

def func(f, n):
    if f == 1:
        return math.log(np.math.factorial(n), 2)
    elif f == 2:
        return 2 ** (3 * n)
    elif f == 3:
        return n ** (n ** 0.5)
    elif f == 4:
        return 2 ** (2 ** n)
    elif f == 5:
        return np.log2(n) ** np.log2(n)
    elif f == 6:
        return n ** 0.5
    elif f == 7:
        return np.log2(n) ** 2
    elif f == 8:
        return (math.log(n, 4)) ** 0.5
    elif f == 9:
        return math.factorial(n)
    elif f == 10:
        return 3 ** (np.log2(n))
    elif f == 11:
        return n ** (np.log2(n))
    elif f == 12:
        return 2 ** n
    elif f == 13:
        return np.log2(np.log2(n))
    elif f == 14:
        return 4 ** n
    elif f == 15:
        return math.log(n, 3)
    elif f == 16:
        return 7 ** (np.log2(n))
    elif f == 17:
        return n / math.log(n, 5)
    elif f == 18:
        return n ** 2  
    print('Error!')

y1 = lambda n: math.log(np.math.factorial(n), 2)
y2 = lambda n: 2 ** (3 * n)
y3 = lambda n: n ** (n ** 0.5)
y4 = lambda n: 2 ** (2 ** n)
y5 = lambda n: np.log2(n) ** np.log2(n)
y6 = lambda n: n ** 0.5
y7 = lambda n: np.log2(n) ** 2
y8 = lambda n: (math.log(n, 4)) ** 0.5
y9 = lambda n: math.factorial(n)
y10 = lambda n: 3 ** (np.log2(n))
y11 = lambda n: n ** (np.log2(n))
y12 = lambda n: 2 ** n
y13 = lambda n: np.log2(np.log2(n))
y14 = lambda n: 4 ** n
y15 = lambda n: math.log(n, 3)
y16 = lambda n: 7 ** (np.log2(n))
y17 = lambda n: n / math.log(n, 5)
y18 = lambda n: n ** 2

n = 23
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
result.append(y10(n))
result.append(y11(n))
result.append(y12(n))
result.append(y13(n))
result.append(y14(n))
result.append(y15(n))
result.append(y16(n))
result.append(y17(n))
result.append(y18(n))

array = []
for i in range(len(result)):
	array.append([i + 1, result[i]])

rating = sorted(array, key = lambda array: array[1])
for i in rating: 
	print(i[0], end = ' ')

n = 370
rating2 = []
for i in range(len(rating)-5):
    print('Проверяем: ', rating[i][0])
    print(func(rating[i][0], n) < func(rating[i+1][0], n))
    #rating2.append(func(rating[i][0], n))
#rating2 = sorted(array, key = lambda rating2: rating2[1])
print(rating2)