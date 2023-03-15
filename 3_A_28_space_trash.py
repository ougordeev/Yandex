str1 = ['N', 'NUSDDUSE', 'UEWWD', '', 'U', 'WED']
str2 = 'S 3'

rules_list = []
for i in range(6):
    rules_list.append(str1[i])
input_command = str2.split()

direction_list = ['N', 'S', 'W', 'E', 'U', 'D']
rules = {name:rule for name,rule in zip(direction_list,map(list,rules_list))}
direction_dict = {name:number for name,number in zip(direction_list,range(len(direction_list)))}


n = int(input_command[1])
dp = []
for i in range(len(direction_list)):
    raw = [0,1]
    for j in range(n-1):
        raw.append(-1)
    dp.append(raw)

def execute_command(direction, index, dp):
    if index == 0:
        return 0
    if index == 1:
        return 1
    number = direction_dict[direction]
    move = dp[number][1]
    for part in rules[direction]:
        if dp[direction_dict[part]][index-1] == -1:
            dp[direction_dict[part]][index-1] = execute_command(part, index-1,dp)
        move += dp[direction_dict[part]][index-1]
    return move

ans = execute_command(input_command[0], n, dp)
print(ans)
