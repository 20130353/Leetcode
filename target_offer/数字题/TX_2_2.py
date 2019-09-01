# # import sys
# # all_ans = [1]
# # result = []

# # t, k = list(map(int, sys.stdin.readline().strip().split()))
# # for i in range(t):
# #     low, high = list(map(int, sys.stdin.readline().strip().split()))
# #     if high > len(all_ans)-1:
# #         for i in range(len(all_ans), high+1):
# #             if i - k >= 0:
# #                 all_ans.append(all_ans[-1] + all_ans[i-k])
# #             else:
# #                 all_ans.append(all_ans[-1])
# #     result.append(sum(all_ans[low:high+1]))
# # for i in result:
# #     print(i)

# # import sys
# # all_ans = [1]
# # result = []

# t, k = list(map(int, sys.stdin.readline().strip().split()))
# lows = []
# highs = []
# for i in range(t):
#     low, high = list(map(int, sys.stdin.readline().strip().split()))
#     lows.append(low)
#     highs.append(high)
# highest = max(highs)
# for i in range(1,highest+1):
#     if i-k>=0:
#         all_ans.append(all_ans[i-1]+all_ans[i-k])
#     else:
#         all_ans.append(all_ans[i-1])
# for i in range(len(lows)):
#     low = lows[i]
#     high = highs[i]
#     print(sum(all_ans[low:high+1]))

# import sys
# all_ans = [1]
# result = []

# t, k = list(map(int, sys.stdin.readline().strip().split()))
# lows = []
# highs = []
# for i in range(t):
#     low, high = list(map(int, sys.stdin.readline().strip().split()))
#     lows.append(low)
#     highs.append(high)
# highest = max(highs)
# for i in range(1,highest+1):
#     if i-k>=0:
#         all_ans.append(all_ans[i-1]*2+all_ans[i-k])
#     else:
#         all_ans.append(all_ans[i-1]*2)
# for i in range(len(lows)):
#     low = lows[i]
#     high = highs[i]
#     ans = all_ans[high]-all_ans[low-1]
#     #ans = ans % (1e9+7)
#     print(ans)
import sys
all_ans = [1]
sum_ans = [1]
result = []

t, k = list(map(int, sys.stdin.readline().strip().split()))
lows = []
highs = []
for i in range(t):
    low, high = list(map(int, sys.stdin.readline().strip().split()))
    lows.append(low)
    highs.append(high)
highest = max(highs)
for i in range(1,highest+1):
    if i-k>=0:
        all_ans.append(all_ans[i-1]+all_ans[i-k])
    else:
        all_ans.append(all_ans[i-1])
    sum_ans.append(all_ans[-1]+sum_ans[-1])
for i in range(len(lows)):
    low = lows[i]
    high = highs[i]
    print(sum_ans[high]-sum_ans[low-1])
    #print(sum(all_ans[low:high+1]))