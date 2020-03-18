n = int(input())
arr = input() 
l = list(map(int,arr.split(' ')))

for i in range (0,n):
    if l[i] % 2  == 0:
        print(l[i])
