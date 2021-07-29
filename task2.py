L = int(input())
N = int(input())
cells = []
for i in range(N):
    cells.append(int(input()))
a = 0
i = 0
while i < N:
    if cells[i] == 0:
        i = i + 1
    else:
        i = i + L
        a = a + 1
print(a)

