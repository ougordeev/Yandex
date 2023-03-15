str1 = '5 5'
str2 = ['1 1 1 1 1','3 100 100 100 100','1 1 1 1 1','2 2 2 2 1','1 1 1 1 1']

n,m = map(int, str1.split())

data = [[]]
for i in range(n):
    raw = [0]
    values = map(int,str2[i].split())
    raw.extend(values)
    data.append(raw)

ans = []
ans.append([21*100]*(m+1))
for i in range(n):
    if i == 0:
        raw = [0]
    else:
        raw = [21*100]
    for j in range (m):
        raw.append(0)
    ans.append(raw)

for i in range(1, n+1):
    for j in range (1, m+1):
        ans[i][j] = data[i][j] + min(ans[i-1][j],ans[i][j-1])
print(ans[-1][-1])
