def Plot(n):
    for i in range(n):
        flag = i % 2
        if flag == 0:
            for j in range(1, i + 2):
                print(j, end='')
                if j < i + 1:
                    print('#', end='')
        else:
            for j in range(i + 1, 0, -1):
                print(j, end='')
                if j > 1:
                    print('#', end='')
        print('\n')


n = int(input())
Plot(n)