str1 = '6 6'

n,m = map(int,str1.split())
di = [2,2,-1,1]
dj = [-1,1,2,2]
ans = []
for i in range(n):
    raw = []
    for j in range(m):
        raw.append(0)
    ans.append(raw)
ans[0][0] = 1
for k in range(0,max(n,m)*2):
    f = k
    for l in range(0,k//2+1):
        if l!= f:
            i = l
            j = f
            if (0 <= i <= n-1) and (0 <= j <= m-1):
                val = ans[i][j]
                for a in range(4):
                    if (0 <= i+di[a] <= n-1) and (0 <= j+dj[a] <= m-1):
                            ans[i+di[a]][j+dj[a]] += val
            i = f
            j = l
            if (0 <= i <= n-1) and (0 <= j <= m-1):
                val = ans[i][j]
                for a in range(4):
                    if (0 <= i+di[a] <= n-1) and (0 <= j+dj[a] <= m-1):
                            ans[i+di[a]][j+dj[a]] += val
        else:
            i = f
            j = f
            if (0 <= i <= n-1) and (0 <= j <= m-1):
                val = ans[i][j]
                for a in range(4):
                    if (0 <= i+di[a] <= n-1) and (0 <= j+dj[a] <= m-1):
                            ans[i+di[a]][j+dj[a]] += val
        f -=1
        
print(ans[-1][-1])
