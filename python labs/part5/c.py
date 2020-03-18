n = int(input())
arr = input() 
l = list(map(int,arr.split(' ')))

cnt = 0

for i in range (0,n):
    if l[i] > 0:
       cnt+=1
       
print(cnt) 