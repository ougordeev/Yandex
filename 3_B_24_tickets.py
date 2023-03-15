str1 = '5'
str2 = ['5 10 15', '2 10 15', '5 5 5', '20 20 1', '20 1 1']

n = int(str1)
a_i = [0]
b_i = [0]
c_i = [0]

dp = [0]*(n+1)
a,b,c = map(int,str2[0].split())
a_i.append(a)
b_i.append(b)
c_i.append(c)
dp[1] = a_i[1]

if n > 1:
    a,b,c = map(int,str2[1].split())
    a_i.append(a)
    b_i.append(b)
    c_i.append(c)
    dp[2] = min(dp[1]+a_i[2],dp[0] + b_i[1])

if n > 2:
    a,b,c = map(int,str2[2].split())
    a_i.append(a)
    b_i.append(b)
    c_i.append(c)
    dp[3] = min(dp[2]+a_i[3],dp[1] + b_i[2],dp[0] + c_i[1])

if n > 3:
    for i in range(4,n+1):
        a,b,c = map(int,str2[i-1].split())
        a_i.append(a)
        b_i.append(b)
        c_i.append(c)
        dp[i] = min(dp[i-1]+a_i[i],dp[i-2] + b_i[i-1],dp[i-3] + c_i[i-2])

print(dp[-1])


