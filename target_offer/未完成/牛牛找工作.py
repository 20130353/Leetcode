from collections import OrderedDict

if __name__ == '__main__':
    n, m = map(int, input().strip().split(' '))
    arr = OrderedDict()
    for i in range(n):
        a, b = map(int, input().strip().split(' '))
        arr[a] = b
    people = list(map(int, input().strip().split(' ')))
    for i in range(m):
        if people[i] in arr.keys():
            print(str(arr[people[i]]))
        else:
            for key in arr.keys():
                if key > people[i]:
                    print(str(pre_value))
                    break
                else:
                    pre_value = arr[key]
