str1 = '4 2'

m,n = map(int,str1.split())

dp = []
for i in range(n):
    raw = [1]
    for j in range(m-1):
        if i == 0:
            raw.append(1)
        else:
            raw.append(0)
    dp.append(raw)

for i in range(1,n):
    for j in range(1,m):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] + dp[i-1][j-1]
print(dp[-1][-1])


