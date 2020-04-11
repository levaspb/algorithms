def fib_mod(n, m):
    s = [0, 1]
    period = 0
    r = 0
    for i in range(2, n + 1):
        s.append((s[i - 1] + s[i - 2]) % m)
        period += 1
        if s[i] == 1 and s[i - 1] == 0:
          return s[n % period]
          break
    #print(period, n, n % period, s)
    return s[n]
    
def fib(n):
    # put your code here
    l = [0, 1]
    if n != 1:
        for i in range(2, n + 1):
		        l.append(l[i - 1] + l[i - 2])
    return l[n]

def main():
    #n, m = map(int, input().split())
    m = 77
    for n in range(200000, 500000):
      if (fib(n) % m) != fib_mod(n, m):
         print('ERROR: ', fib(n) % m, ' ', fib_mod(n, m))
    print('SUCCESS')


if __name__ == "__main__":
    main()
