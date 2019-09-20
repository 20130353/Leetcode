# # case通过率为10.00%
# # 存在的问题：mid不减
#
# # case通过率为40.00%
# # 存在的问题：是int，不是floor
# # 存在的问题：只取前六位
#
# # 存在的问题：左右边界，中间的mid属于右边界
# # 您的代码已保存
# # 答案错误:您提交的程序没有通过所有的测试用例
# # case通过率为70.00%
#
#
# # 为什么这道题不能直接用二分搜索，一定要改成for+low/high=mid
# # 因为如果直接用二分搜索的话，每次low/high=mid，会造成死循环
# # 为什么high不能等于mid-1，这样会造成左区间变小。
# # 答案错误:您提交的程序没有通过所有的测试用例
# # case通过率为90.00%
#
# # 存在的问题：不能用low+(high-low)//2,int(负数/2)-->大的数，负数//2-->小的数
# print(-55 / 2) --》 负数/2
# print(-55 // 2) --》 -28
# print(int(-55 / 2)) --》-27
# AC

class Calculator(object):
    def binary_search(self, target, low=-90, high=90):
        ans = ''
        for i in range(6):
            mid = int((low + high) / 2)
            # print('low {}\t,mid {}\t,high {}'.format(low, mid, high))
            if mid <= target:
                low = mid
                ans += '1'
            else:
                high = mid
                ans += '0'
        return ans


if __name__ == '__main__':
    n = int(input().strip())

    # n = 80
    # n = 0
    # n = 1
    # n = 2
    # n = -7
    # n = 5

    ans = Calculator().binary_search(n)
    print(ans)
