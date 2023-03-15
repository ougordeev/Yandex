str1 = '5'
str2 = ['35', '40', '101', '59', '63']
# str1 = '1'
# str2 = ['300']

n = int(str1)
days = [0]
for i in range(n):
    days.append(int(str2[i]))

dp = []
for i in range(n+1):
    raw = []
    for j in range(n+2):
        if i == 0:
            if j == 0:
                raw.append([0,[]])
            else:
                raw.append([601*j,[]])
        else:
            if j!= n+1:
                raw.append([0,[]])
            else:
                raw.append([601*j*(i+1),[]])
    dp.append(raw)

for i in range (1,n+1):
    for j in range (n+1):
        if days[i] <= 100:
            prev_pay = dp[i-1][j][0] + days[i]
            prev_cupon_sell = dp[i-1][j+1][0]
            if prev_pay <= prev_cupon_sell:
                dp[i][j] = ([prev_pay,dp[i-1][j][1]])
            else:
                new_days = dp[i-1][j+1][1].copy()
                new_days.append(i)
                dp[i][j] = ([prev_cupon_sell,new_days])
        else:
            prev_cupon_sell = dp[i-1][j+1][0]
            if j != 0:
                prev_pay = dp[i-1][j-1][0] + days[i]
            else:
                prev_pay = 2 * prev_cupon_sell
            if prev_pay <= prev_cupon_sell:
                dp[i][j] = ([prev_pay,dp[i-1][j-1][1]])
            else:
                new_days = dp[i-1][j+1][1].copy()
                new_days.append(i)
                dp[i][j] = ([prev_cupon_sell,new_days])
min_value = dp[n][0]
j = 0
ans_j = 0
for element in dp[n]:
    if element[0] <= min_value[0]:
        min_value = element
        ans_j = j
    j+= 1
print(min_value[0])
print(ans_j,len(min_value[1]))
for day in min_value[1]:
    print(day)

