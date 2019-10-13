def solution(string):
    i = 0
    leng = len(string)
    while i <= (leng // 2) and string[i] == string[leng - i - 1]:
        i += 1
    if i > (leng // 2):
        return 'Yes!'
    else:
        return 'No!'


if __name__ == '__main__':
    try:
        while True:
            string = input().strip()
            if string == '':
                break
            print(solution(string))
    except Exception:
        pass
