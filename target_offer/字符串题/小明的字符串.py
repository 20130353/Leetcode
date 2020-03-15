if __name__ == '__main__':
    n, times = map(int, input().strip().split(' '))
    string = input().strip()
    for _ in range(times):
        type, pos = map(int, input().strip().split(' '))
        if type == 1:
            num = string.__len__() - pos
            string = string[num:] + string[:num]
        else:
            print(string[pos])
