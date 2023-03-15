str1 = '2'
str2 = ['2 2.9 2.1', '3 5.6 9.0 2.0']

n = int(str1)
requests = str2
for i in range(n):
    request = requests[i].split()
    containers_count = int(request[0])
    if containers_count <= 2:
        print('1')
        continue
    containers = []
    first_element = True
    for container in request:
        if first_element:
            first_element = False
            continue
        else:
            f_container = float(container)
            containers.append(f_container)
    
    stack = []
    containers.reverse()
    keys = sorted(containers)
    keys_iterator = iter(keys)
    key = next(keys_iterator)

    exit_flag = False
    while not exit_flag:
        try:
            cont = containers.pop()
            if cont != key:
                stack.append(cont)
            else:
                stack_exit = False
                while not stack_exit:
                    try:
                        key = next(keys_iterator)
                        if stack[-1] == key:
                            stack.pop()
                        else:
                            stack_exit = True
                    except:
                        stack_exit = True
        except:
            exit_flag = True
    if len(stack) == 0:
        print('1')
    else:
        print('0')

