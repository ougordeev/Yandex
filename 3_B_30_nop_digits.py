str1 = '5'
str2 = '1 2 3 4 5'
str3 = '5'
str4 = '2 3 1 5 4'

# str1 = '1'
# str2 = '1'
# str3 = '100'
# str4 = '1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10'

n = int(str1)
digits_n = [0]
digits_n.extend(list(map(int,str2.split())))
m = int(str3)
digits_m = [0]
digits_m.extend(list(map(int,str4.split())))

dp = []
for i in range(n+1):
    raw = []
    for j in range(m+1):
        raw.append(0)
    dp.append(raw)

for i in range(1,n+1):
    for j in range(1, m+1):
        if digits_n[i] == digits_m[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1],dp[i-1][j])

ans = []
while i !=0 or j!=0:
    if dp[i][j] == 0:
        break
    if dp[i][j] == dp[i-1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j-1]:
        j-= 1
    else:
        ans.append(str(digits_n[i]))
        i -= 1
        j-= 1
ans.reverse()
print(' '.join(ans))




