# 您的代码已保存
# 答案正确:恭喜！您提交的程序通过了所有的测试用例

from collections import Counter


def solution(arr, k):
    ans = 0
    counter = Counter(arr).most_common()
    for i in range(counter.__len__()):
        ans += (min(counter[i][1], k) ** 2)
        k -= min(k, counter[i][1])
        if k <= 0:
            return ans
    return ans


if __name__ == '__main__':
    try:
        while True:
            string = input().strip()
            if string == '':
                break
            arr = list(input().strip())
            n, k = map(int, string.split(' '))
            ans = solution(arr, k)
            print(ans)
    except Exception as e:
        pass
