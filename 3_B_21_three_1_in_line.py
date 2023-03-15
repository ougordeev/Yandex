str1 = '4'

n = int(str1)

answers_list = [0]*(n+1)
answers_list[0] = {0:0, 1:0, 2:0, 3:0}
if n > 0:
    answers_list[1] = {0:1, 1:1, 2:0, 3:0}

for i in range(2, n+1):
    new_dict = {}
    new_dict[0] = answers_list[i-1][0] + answers_list[i-1][1] + answers_list[i-1][2]
    new_dict[1] = answers_list[i-1][0]
    new_dict[2] = answers_list[i-1][1]
    new_dict[3] = answers_list[i-1][2]
    answers_list[i] = new_dict
print (answers_list[-1][0]+answers_list[-1][1]+answers_list[-1][2])
