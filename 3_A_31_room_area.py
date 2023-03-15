str1 = '3'
str2 = ['***', '*..', '***']
str3 = '2 2'

n = int(str1)
field = []
for i in range(n+2):
    raw = []
    for j in range(n+2):
        raw.append(0)
    field.append(raw)

for i in range(1,n+1):
    raw = list(str2[i-1])
    for j in range(n):
        if raw[j] == '.':
            field[i][j+1] = 1

find_key = ''.join(str3.split())

vertex_dict = {}


move_i = [0,0,-1,+1]
move_j = [-1,+1,0,0]

for i in range(1,n+1):
    for j in range(1,n+1):
        if field[i][j] == 1:
            key = str(i) + str(j)
            vertex_dict[key] = []
            for k in range(4):
                if field[i+move_i[k]][j+move_j[k]] == 1:
                    new_key = str(i+move_i[k]) + str(j+move_j[k])
                    vertex_dict[key].append(new_key)

colours = {key:False for key in vertex_dict.keys()}


ans = []
    
def dfs(vertex_dict, colours, ans, now):
    colours[now] = True
    ans.append(1)
    for vay in vertex_dict[now]:
        if not colours[vay]:
            dfs(vertex_dict, colours, ans, vay)

dfs(vertex_dict, colours, ans, find_key)


print(len(ans))


