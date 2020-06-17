r = int(input("enter no of rows"))
for i in range(65, 65+r):
    r = r - 1
    for j in range(r, 1, -1):
        print(" ", end="")
    for k in range(65, i+1):
        print(chr(k), end="")
    for j in range(i-1, 64, -1):
        print(chr(j), end="")
    print()



