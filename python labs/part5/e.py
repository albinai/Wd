n = int(input())
arr = input() 
l = list(map(int,arr.split(' ')))

checker = False

for i in range (0,n-1):
    if (l[i+1] > 0 and l[i] > 0) or (l[i+1] < 0 and l[i] < 0):
       checker = True
       
if checker == False:
    print("NO")

if checker == True:
    print("YES") 