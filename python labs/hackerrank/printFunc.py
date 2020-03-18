if __name__ == '__main__':
    n = int(input())



def printString(n):

    arr = []
    for i in range(1, n+1):
        arr.append(i)

    print(*arr, sep='', end='\n')


printString(n)