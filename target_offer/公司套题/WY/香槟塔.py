# AC
if __name__ == '__main__':
    n, m = map(int, input().strip().split(' '))
    size = list(map(int, input().strip().split(' ')))
    contain = [0] * n
    for _ in range(m):
        data = list(map(int, input().strip().split(' ')))
        if data.__len__() == 2:
            print(contain[data[1] - 1])
        else:
            i = data[1] - 1
            leave = data[2]
            while leave > 0 and i < n:
                if size[i] - contain[i] >= leave:
                    contain[i] += leave
                    leave = 0
                else:
                    leave -= size[i] - contain[i]
                    contain[i] = size[i]
                    i += 1
