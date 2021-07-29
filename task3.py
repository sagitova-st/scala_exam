

str = str(input())
hight = 0
hight_prom = 0
width = len(str)
arr = [[0 for j in range(100)] for i in range(100)]
counter = 0

for char in str:
    if char == "(":
        hight_prom += 1
    if char == ")":
        if hight_prom > hight:
            hight = hight_prom
        hight_prom = 0

for j, char in enumerate(str):
    if char == ")":
        counter -= 1
    for i in range(hight):
        if char == "(":
            if i == counter:
                arr[i][j] = "/"
            else:
                arr[i][j] = "."
        if char == ")":
            if i == counter:
                arr[i][j] = "\\"
            else:
                arr[i][j] = "."
    if char == "(":
        counter += 1

for i in range(hight-1, -1, -1):
    for j in range(width):
        print(arr[i][j], end='')
    print()
