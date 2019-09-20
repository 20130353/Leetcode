# case通过率为75.00%
# 出现的原因是：二分查找的边界存在问题

# AC
class Calculator(object):
    def prime(self, n):
        if n <= 2:
            return 0
        else:
            prime_list = list()
            prime_list.append(2)  # 先将2加入到要遍历的列表中
            for x in range(3, n):
                target = False
                for target in prime_list:
                    if x % target == 0:  # 对小于n的x进行遍历，当某个数整除为0时，不执行添加列表操作
                        target = False
                        break
                    else:
                        target = True
                if target is True:
                    prime_list.append(x)  # 对小于x的质数进行遍历后，没有能整除的质数，则这个数也是质数
            return prime_list

    def binartarget_search(self, arr, n, target):
        low = 0
        high = n - 1
        while (low <= high):
            mid = low + (high - low) // 2
            if arr[mid] == target:
                return mid
            if arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1


if __name__ == '__main__':
    n = int(input().strip())
    arr = Calculator().prime(n)
    num = 0
    res = []
    for each in arr:
        target = n - each
        ans = Calculator().binartarget_search(arr, arr.__len__(), target)
        if ans != -1 and (min(each, target), max(each, target)) not in res:
            num += 1
            res.append((min(each, target), max(each, target)))
    print(num)
