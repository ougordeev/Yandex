str1 = '8 7'
str2 = ['1 4 2 2 2 4 6', '6 2 4 4 2 4 6', '2 1 2 4 2 4 6', '2 1 1 2 4 6 6', '6 2 1 2 6 1 6', '5 5 5 5 5 5 5', '2 1 2 1 2 1 2', '5 5 5 5 1 5 5']

# str1 = '4 4'
# str2 = ['1 2 4 1', '2 4 4 4', '1 4 3 2', '1 2 3 2']

# str1 = '5 5'
# str2 = ['1 1 1 1 1', '1 2 2 2 1', '1 2 3 2 1', '1 2 2 2 1', '1 1 1 1 1']

n,m = map(int,str1.split())
field = []
for i in range(n):
    raw = []
    raw.extend(list(map(int,str2[i].split())))
    field.append(raw)

di = [0,-1,0,1]
dj = [-1,0,1,0]

vertex_vays = [0] * (m*n)
hi_array = [0] * (m*n)
for i in range(n):
    for j in range(m):
        vays = []
        hi_array[(i)*m +(j)] = field[i][j]
        for k in range(4):
            if (0 <= (i + di[k]) < n) and (0 <= (j + dj[k]) < m):
                if field[i][j] > field[i + di[k]][j + dj[k]]:
                    vays.append((i + di[k]) * m + (j + dj[k]))
        if not vays:
            for k in range(4):
                if (0 <= (i + di[k]) < n) and (0 <= (j + dj[k]) < m):
                    if field[i][j] == field[i + di[k]][j + dj[k]]:
                        vays.append((i + di[k]) * m + (j + dj[k]))
        vertex_vays[(i)*m +(j)] = vays

def dfs(vertex_vays, hi_array, visited, now, hi, hi_circle_flag, no_exit_vertex, searched):
    visited[now] = True
    if vertex_vays[now]:
        for vay in vertex_vays[now]:
            if searched[vay]:
                hi_circle_flag[0] = False
                return
            if hi_array[vay] < hi:
                hi_circle_flag[0] = False
                return
            if not visited[vay]:
                dfs(vertex_vays, hi_array, visited, vay, hi, hi_circle_flag, no_exit_vertex, searched)
            if hi_circle_flag[0] == False:
                break
        if hi_circle_flag[0] == False:
            return
    else:
        hi_circle_flag[0] = False
        no_exit_vertex.append(now)
        return


searched = [False]*(n*m)
no_exit_vertex = []

for i in range(n*m):
    if searched[i] == False:
        visited = [False]*(n*m)
        hi_circle_flag = [True]
        dfs(vertex_vays, hi_array, visited, i, hi_array[i], hi_circle_flag, no_exit_vertex, searched)
        searched[i] = True
        if hi_circle_flag[0]:
            for j in range(n*m):
                if visited[j]:
                    searched[j] = True
            no_exit_vertex.append(-1)


print(len(no_exit_vertex))


