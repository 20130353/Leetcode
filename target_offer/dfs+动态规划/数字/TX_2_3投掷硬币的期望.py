# 出现的两点问题：
# 1. 不应该直接用dp
# 2. 取模也不应该是自己算
# 两个点都应该直接模拟

def solution(n, p, q):
    if n == 0 or p == 0:
        return 0
    leng = n - q + 1
    dp = [[0] * (leng) for _ in range(n)]  # 到第i个硬币时j个正面向上的方案可能性
    for i in range(n):
        for j in range(leng):
            if i == 0 and (j <= 1):
                dp[i][j] = 1
                continue
            elif i > 0:
                dp[i][j] = dp[i - 1][j]
                if j >= 1:
                    dp[i][j] += dp[i - 1][j - 1]
    # for each in dp:
    #     print(each)

    ans = 0
    sum_case = 0
    for i in range(p, leng):
        sum_case += dp[n - 1][i]
        ans += dp[n - 1][i] * i
    qiwang = (1 / sum_case) * ans
    # print(qiwang)
    mod = 1000000007
    if int(qiwang) != qiwang:
        return int((mod + ans) / 3)
    else:
        return qiwang


# #include <iostream>
# #include <vector>
# #include <string>
# #include <algorithm>
# using namespace std;
# int C(int n,int p){
#     int tmp=1;
#     for (int i=0;i<p;i++){
#         tmp=tmp*(n-i)/(p-i); # 排列数求c(n,i)
#         tmp=tmp%1000000007;
#     }
#     return tmp;
# }
# int main(){
#     int n,p,q;
#     cin>>n>>p>>q;
#     int x=0,y=0;
#     for (int i=p;i<=n-q;i++){
#         x=x+C(n,i)*i;
#         x=x%1000000007;
#         y=y+C(n,i);
#         y=y%1000000007;
#     }
#     int res=0;
#     while (1){
#         if (res*y%1000000007==x) {cout<<res;return 0;}
#         res++;
#     }
# }


if __name__ == '__main__':
    try:
        while True:
            n, p, q = map(int, input().strip().split(' '))
            ans = solution(n, p, q)
            print(ans)
            break
    except Exception as e:
        print(e)
