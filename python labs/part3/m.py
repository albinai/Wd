n = int(input())
arr = []
sum = 0

for i in range(0,n):
    x = int(input())
    arr.append(x)
    if x == 0:
        sum+=1

print(sum)