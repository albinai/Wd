if __name__ == '__main__':
    n = int(input())

    marksheet = []
    for i in range(0, n):       
        marksheet.append([input(), float(input())])

    second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]

    print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))