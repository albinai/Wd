n = int(input())
arr = input() 
l = list(map(int,arr.split(' ')))

checker = 0

for i in range (0,n):
    l[i] = l[n-1-i]
    print(l[i])
    
