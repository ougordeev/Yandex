str1 = 'SALJSDHLAK'
str2 = 'ALJSDHLAK'

n = len(str1)
chars_n = ['0']
chars_n.extend(list(str1))
m = len(str2)
chars_m = ['0']
chars_m.extend(list(str2))

dp = []
inf = max(n,m)
for i in range(n+1):
    if i == 0:
        raw = [0]
        for j in range(1,m+1):
            raw.append(j)
        dp.append(raw)
    else:
        raw = [i]
        for j in range(m):
            raw.append(0)
        dp.append(raw)

for i in range(1,n+1):
    for j in range(1, m+1):
        if chars_n[i] == chars_m[j]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1]) + 1
            

print(dp[-1][-1])