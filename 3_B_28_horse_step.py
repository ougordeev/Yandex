str1 = '31 34'

n,m = map(int,str1.split())
di = [2,1]
dj = [1,2]
ans = []
for i in range(n+2):
    raw = [0,0]
    for j in range(m):
        raw.append(0)
    ans.append(raw)
ans[2][2] = 1
for i in range(2,n+2):
    for j in range(2,m+2):
        if i == 2 and j == 2:
            pass
        else:
            sum = 0
            for a in range(2):
                sum += ans[i-di[a]][j - dj[a]]
            ans[i][j] = sum
print(ans[-1][-1])
