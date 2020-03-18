n = int(input())
arr = input() 
l = list(map(int,arr.split(' ')))

cnt = 0

for i in range (0,n-1):
    if l[i+1] > l[i]:
       cnt+=1
       
print(cnt) 