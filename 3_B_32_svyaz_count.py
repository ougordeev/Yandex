from threading import stack_size
from sys import setrecursionlimit

setrecursionlimit (1000000)
stack_size(134217728)

str1 = '6 4'
str2 = ['3 1','1 2','5 4','2 3']

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

for i in range(1,v+1):
    if not visited[i]:
        temp_ans = []
        dfs(vertex_vays, visited, temp_ans, i)
        ans.append(temp_ans)


print(len(ans))
for line in ans:
    print(len(line))
    print(' '.join(map(str,line)))