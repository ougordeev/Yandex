str1 = '!1|!(!0&!0^1)'

operations = {'!', '&', '|', '^', '(', ')'}
postfix_stack = []
postfix_ans = []
false_flag = False
breackets_stack = []
last_char = 'operator'
for char in str1:
    if char not in operations:
        if char.isdigit():
            postfix_ans.append(int(char))
            last_char = 'operand'
    else:
        if char == '^' or char == '|':
            if last_char == 'close_breaked' or last_char == 'operand':
                if len(postfix_stack) > 0:
                    exit_postfix_stack = False
                    while not exit_postfix_stack:
                        if len(postfix_stack) > 0:
                            if postfix_stack[-1] in {'!', '&', '|', '^'}:
                                postfix_ans.append(postfix_stack.pop())
                            else: exit_postfix_stack = True
                        else: exit_postfix_stack = True
                postfix_stack.append(char)
                last_char = 'operator'
            else:
                false_flag = True
                break

        elif char == '&':
            if last_char == 'close_breaked' or last_char == 'operand':
                if len(postfix_stack) > 0:
                    exit_postfix_stack = False
                    while not exit_postfix_stack:
                        if len(postfix_stack) > 0:
                            if postfix_stack[-1] == '*' or postfix_stack[-1] == '!':
                                postfix_ans.append(postfix_stack.pop())
                            else: exit_postfix_stack = True
                        else: exit_postfix_stack = True
                postfix_stack.append(char)
                last_char = 'operator'
            else:
                false_flag = True
                break
        
        elif char == '!':
            postfix_stack.append(char)
            last_char = 'not_operator'

        elif char == '(':
            if last_char == 'open_breaked' or last_char == 'operator' or last_char == 'not_operator':
                postfix_stack.append(char)
                breackets_stack.append(char)
                last_char == 'open_breaked'
            else:
                false_flag = True
                break
        else:
            if last_char == 'operator':
                false_flag = True
                break
            if len(breackets_stack) != 0:
                breackets_stack.pop()
                exit_postfix_stack = False
                while not exit_postfix_stack:
                    if len(postfix_stack) > 0:
                        if postfix_stack[-1] != '(':
                            postfix_ans.append(postfix_stack.pop())
                        else:
                            postfix_stack.pop()
                            exit_postfix_stack = True
                    else: exit_postfix_stack = True
                last_char == 'close_breaked'
            else:
                false_flag = True
                break

if last_char == 'operator' or last_char == 'not_operator':
    false_flag = True

if breackets_stack:
    false_flag = True

if len(postfix_stack) > 0:
    postfix_stack.reverse()
    for value in postfix_stack:
        postfix_ans.append(value)


        
if false_flag:
    print('WRONG')
else:
    list = postfix_ans
    stek = []
    for element in list:
        if element in {'&', '|', '^'}:
            op1 = stek.pop()
            op2 = stek.pop()
            if element == '&':
                result = op2 and op1
            elif element == '|':
                result = op2 or op1
            else:
                result = (not(op2) and op1) or (not(op1) and op2)
            stek.append(result)
        elif element == '!':
            op1 = stek.pop()
            result = not op1
            stek.append(result)
        else:
            stek.append(bool(element))
    print(int(stek.pop()))