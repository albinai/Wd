a = int(input())
deliteli = []


for i in range(1,a+1):
    if (a % i != 0):
        i+=1
        continue
    else: 
        deliteli.append(i)

print(len(deliteli))        
