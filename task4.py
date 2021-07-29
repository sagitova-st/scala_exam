import math

X = int(input())

m_arr = []
n_arr = []
counter = 0

for n in range(1, int(math.sqrt(X))+1):
    for m in range(1, int(math.sqrt(X))+1):
        if m < n:
            if m + X == ((m+1)*n + (n+1)*m):
                m_arr.append(m)
                n_arr.append(n)
                counter += 1
        if m > n:
            if n + 1 + X == ((m+1)*n + (n+1)*m):
                m_arr.append(m)
                n_arr.append(n)
                counter += 1
        if m == n:
            if (m+n) - 1 + X == ((m+1)*n + (n+1)*m):
                m_arr.append(m)
                n_arr.append(n)
                counter += 1
print(counter)
for i in range(len(m_arr)):
    print(n_arr[i], m_arr[i])
