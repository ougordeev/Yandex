str1 = '5 5'
str2 = ['9 9 9 9 9','3 0 0 0 0','9 9 9 9 9','6 6 6 6 8','9 9 9 9 9']

n,m = map(int, str1.split())

data = [[]]
for i in range(n):
    raw = [0]
    values = map(int,str2[i].split())
    raw.extend(values)
    data.append(raw)

ans = []
ans.append([0]*(m+1))
for i in range(n):
    raw = [0]
    for j in range (m):
        raw.append(0)
    ans.append(raw)

for i in range(1, n+1):
    for j in range (1, m+1):
        ans[i][j] = data[i][j] + max(ans[i-1][j],ans[i][j-1])
print(ans[-1][-1])
trace = []
while i !=1 or j!=1:
    if ans[i-1][j] >= ans[i][j-1]:
        trace.append('D')
        i -=1
    else:
        trace.append('R')
        j -=1
trace.reverse()
print(' '.join(trace))

