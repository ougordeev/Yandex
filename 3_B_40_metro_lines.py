str1 = '5'
str2 = '2'
str3 = ['4 1 2 3 4', '2 5 3']
str4 = '3 1'

from collections import deque

station_count = int(str1)
lines_count = int(str2)

staitions_dict = {}
staitions_variants_dict = {}
for i in range(lines_count):
    line = str3[i].split()
    line_len = int(line[0])
    for j in range(1,line_len+1):
        station = (int(line[j]),i)
        if station[0] not in staitions_variants_dict:
            staitions_variants_dict[station[0]] = []
        staitions_variants_dict[station[0]].append(station)
        if station not in staitions_dict:
            staitions_dict[station] = []
        if j-1 >= 1:
            left_station = (int(line[j-1]),i)
            staitions_dict[station].append(left_station)
        if j+1 < line_len+1:
            right_station = (int(line[j+1]),i)
            staitions_dict[station].append(right_station)
        for same_station in staitions_variants_dict[station[0]]:
            if same_station != station:
                staitions_dict[station].append(same_station)
                staitions_dict[same_station].append(station)

        
start, finish = map(int,str4.split())


def bfs(staitions_dict, change_dict, now, que):
    now_changes_count = change_dict[now]
    for vay in staitions_dict[now]:
        changes_count = now_changes_count
        if vay[0] == now[0]:
            changes_count += 1
        if (vay not in change_dict) or (changes_count < change_dict[vay]):
            change_dict[vay] = changes_count
            que.append(vay)

que = deque()
change_dict = {}
for variant in staitions_variants_dict[start]:
    change_dict[variant] = 0
    que.append(variant)


while que:
    station = que.popleft()
    bfs(staitions_dict, change_dict, station, que)

min_changes = lines_count
for variant in staitions_variants_dict[finish]:
    if variant in change_dict:
        if change_dict[variant] < min_changes:
            min_changes = change_dict[variant]

if min_changes == lines_count:
    print(-1)
else:
    print(min_changes)





