n = int(input())
arr = input() 
l = list(map(int,arr.split(' ')))

checker = 0

for i in range (1,n-1):
    if l[i-1] < l[i] and l[i+1] < l[i]:
       
        checker += 1
    
print(checker)