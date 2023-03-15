# str1 = '10'
# str2 = '4 8 2 6 2 10 6 29 58 9'

str1 = '6'
str2 = '3 29 5 5 28 6'

n = int(str1)
numbers =[0]
numbers.extend(list(map(int, str2.split())))
dp = [(0,None,0)]

max_l = 0
for i in range(1,n+1):
    number = numbers[i]
    max = (1,number,0)
    l = 1
    for j in range(0, i):
        element = dp[j]
        if dp[j][1] is None or number > dp[j][1]:
            if dp[j][0] >= l:
                l = dp[j][0]
                max = (dp[j][0]+1,number,j)
                if dp[j][0]+1 > max_l:
                    max_l = dp[j][0]+1
    dp.append(max)
while dp[i][0] < max_l:
    i -=1
ans = []
while i > 0:
    ans.append(str(dp[i][1]))
    i = dp[i][2]
ans.reverse()
print (' '.join(ans))
        

