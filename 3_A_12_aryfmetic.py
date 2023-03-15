str1 = '1+2-3*4+5-6*7+8-9*10'

operations = {'-', '+', '*', '(', ')'}
first = True
first_minus = False
postfix_stack = []
postfix_ans = []
digits = ''
false_flag = False
breackets_stack = []
last_char = 'operator'
space = False
for char in str1:
    if first and char == '-':
        postfix_ans.append(0)
        last_char = 'operator'
        first_minus = True
        continue
    if char == ' ':
        if (last_char == 'open_breaked' or last_char == 'operator') and (digits):
            postfix_ans.append(int(digits))
            digits = ''
            last_char = 'operand'
            if first_minus:
                postfix_ans.append('-')
                first = False
                first_minus = False
            first = False
        continue
    if char not in operations:
        if char.isdigit():
            digits += char
            first = False
            # if not first_minus:
            #     first = False
        else:
            false_flag = True
            break
    else:
        if digits:
            if last_char == 'open_breaked' or last_char == 'operator':
                postfix_ans.append(int(digits))
                digits = ''
                last_char = 'operand'
            else:
                false_flag = True
                break
            if first_minus:
                postfix_ans.append('-')
                first = False
                first_minus = False
            first = False
        if char == '+' or char == '-':
            if last_char == 'close_breaked' or last_char == 'operand':
                if len(postfix_stack) > 0:
                    exit_postfix_stack = False
                    while not exit_postfix_stack:
                        if len(postfix_stack) > 0:
                            if postfix_stack[-1] == '+' or postfix_stack[-1] == '-'or postfix_stack[-1] == '*':
                                postfix_ans.append(postfix_stack.pop())
                            else: exit_postfix_stack = True
                        else: exit_postfix_stack = True
                postfix_stack.append(char)
                last_char = 'operator'
            else:
                false_flag = True
                break

        elif char == '*':
            if last_char == 'close_breaked' or last_char == 'operand':
                if len(postfix_stack) > 0:
                    exit_postfix_stack = False
                    while not exit_postfix_stack:
                        if len(postfix_stack) > 0:
                            if postfix_stack[-1] == '*':
                                postfix_ans.append(postfix_stack.pop())
                            else: exit_postfix_stack = True
                        else: exit_postfix_stack = True
                postfix_stack.append(char)
                last_char = 'operator'
            else:
                false_flag = True
                break

        elif char == '(':
            if last_char == 'open_breaked' or last_char == 'operator':
                postfix_stack.append(char)
                breackets_stack.append(char)
                last_char == 'open_breaked'
                first = True
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
if digits:
    if last_char == 'open_breaked' or last_char == 'operator':
        postfix_ans.append(int(digits))
        last_char = 'operand'
        if first_minus:
            postfix_ans.append('-')
    else:
        false_flag = True

if last_char == 'operator':
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
        if element in {'+','-','*'}:
            op1 = stek.pop()
            op2 = stek.pop()
            if element == '-':
                result = op2 - op1
            elif element == '+':
                result = op2 + op1
            else:
                result = op2 * op1
            stek.append(result)
        else:
            stek.append(int(element))
    print(stek.pop())    
        

    



