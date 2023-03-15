str1 = '3'
str2 = '3 2 1'

stack = []
train = list(map(int,str2.split()))
train.reverse()
key = 1
exit_flag = False
while not exit_flag:
    try: 
        car = train.pop()
        if car != key:
            stack.append(car)
        else:
            stack_exit = False
            while not stack_exit:
                key += 1
                try:
                    if stack[-1] == key:
                        stack.pop()
                    else:
                        stack_exit = True
                except:
                    stack_exit = True
    except:
        exit_flag = True
if len(stack) == 0:
    print('YES')
else:
    print('NO')

