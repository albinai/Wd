a = int(input())


for i in range(2,a+1):
    if (a % i != 0):
        i+=1
        continue
    else: 
        print(i)
        break
