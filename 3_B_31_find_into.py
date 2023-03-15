from threading import stack_size
from sys import setrecursionlimit

setrecursionlimit (1000000)
stack_size(134217728)

str1 = '10 10'
str2 = ['2 5','6 5','2 4','8 8','3 6','7 9','5 6','6 2','1 3','1 6']

v,e  = map(int,str1.split())

vertex_vays = []
for i in range(v+1):
    vertex_vays.append([])

for i in range(e):
    edge = list(map(int,str2[i].split()))
    vertex_vays[edge[0]].append(edge[1])
    vertex_vays[edge[1]].append(edge[0])

visited = [False] * (v+1)

ans = []
    
def dfs(vertex_vays, visited, ans, now):
    visited[now] = True
    ans.append(now)
    for vay in  vertex_vays[now]:
        if not visited[vay]:
            dfs(vertex_vays, visited, ans, vay)

dfs(vertex_vays,visited, ans, 1)

print(len(ans))
print(' '.join(map(str,sorted(ans))))