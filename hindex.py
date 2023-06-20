articles = [0,1,3,5,6,4,4]
count = [0 for i in range(len(articles))]
for e in articles:
    if e != 0:
        if e < len(articles):
            count[e-1] += 1
        else:
            count[-1] += 1
    result = list()
    for i in range(len(count)):
        for j in range(count[i]):
            result.append(i+1)
h = 0
for i in range(-1, -len(articles), -1):
    if articles[i] > h:
        h += 1
    else:
        break
print(h)