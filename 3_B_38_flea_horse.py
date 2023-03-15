str1 = '4 4 1 1 16'
str2 = ['1 1','1 2','1 3','1 4','2 1','2 2','2 3','2 4','3 1','3 2','3 3','3 4','4 1','4 2','4 3','4 4']

from collections import deque

n,m,s,t,q = map(int,str1.split())

flea_dict = {}
for i in range(q):
    split_cord = str2[i].split()
    flea_dict[(int(split_cord[0]),int(split_cord[1]))] = -1

di = [1, 1, -1, -1, 2, -2, 2, -2]
dj = [2, -2, 2, -2, 1, 1, -1, -1]

def bfs(n,m,find_flea,flea_dict,ranges_dict,now, que):
    current_range = ranges_dict[now]
    for k in range(8):
        new_i = now[0] + di[k]
        new_j = now[1] + dj[k]
        if 1 <= new_i <= n and 1 <= new_j <= m:
            if (new_i,new_j) not in ranges_dict:
                ranges_dict[new_i,new_j] = current_range + 1
                que.append((new_i,new_j))
            if (new_i,new_j) in flea_dict:
                if flea_dict[(new_i,new_j)] == -1:
                    flea_dict[(new_i,new_j)] = current_range + 1
                    find_flea[0] += 1



ranges_dict = {}
ranges_dict[(s,t)] = 0
find_flea = [0]
if (s,t) in flea_dict:
    find_flea = [1]
    flea_dict[(s,t)] = 0
que = deque()
que.append((s,t))

while que:
    cord = que.popleft()
    bfs(n,m,find_flea,flea_dict,ranges_dict,cord,que)
    if find_flea[0] == q:
        break

if find_flea[0] == q:
    print(sum(flea_dict.values()))
else:
    print(-1)
