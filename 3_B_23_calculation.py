str1 = '9'

n = int(str1)

dp = [-1] * (n+5)
dp[0] = (0,0)
dp[1] = (0,0)
dp[2] = (1,1)
dp[3] = (1,1)

for i in range(4,n+1):
    min_dict = {}
    min_dict[dp[i-1]] = i-1
    
    if i%2 == 0:
        two_index = i//2
        min_dict[dp[two_index]] = two_index
    
    if i%3 == 0:
        three_index = i//3
        min_dict[dp[three_index]] = three_index

    
    min_value = min(min_dict)
    min_index = min_dict[min_value]
    dp[i] = (min_value[0]+1,min_index)

print(dp[n][0])
ans = []
i = n
while dp[i][1] > 0:
    ans.append(str(i))
    i = dp[i][1]
ans.append('1')
ans.reverse()
print(' '.join(ans))


