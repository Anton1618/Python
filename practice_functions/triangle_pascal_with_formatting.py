def pascal(N):
    P = []
    for i in range(N):
        row = [1] * (i + 1)
        for j in range(i +1):
            if j != 0 and j != i:
                row[j] = P[i-1][j-1]+P[i-1][j]
        P.append(row)
    len_width = len(repr(P[-1]))
    for i in P:
        elements = ' '.join([str(el) for el in i])
        print(f'{elements:^{len_width}}')

pascal(10)