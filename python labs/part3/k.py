n = int(input())
arr = []
sum = 0

for i in range(0,n):
    x = int(input())
    arr.append(x)
    sum+=arr[i]

print(sum)