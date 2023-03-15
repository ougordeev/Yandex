str1 = '1 7 3 9 4'
str2 = '5 8 0 2 6'

from collections import deque
deq1 = deque()
for card in str1.split():
    deq1.append(int(card))
card_len1 = 5

deq2 = deque()
for card in str2.split():
    deq2.append(int(card))
card_len2 = 5


turns = 0
exit_flag = False
while not exit_flag:
    turns += 1
    card1 = deq1.popleft()
    card2 = deq2.popleft()
    if card1 == 0:
        if card2 == 9:
            deq1.append(card1)
            deq1.append(card2)
            card_len1 += 1
            card_len2 -= 1
        else:
            deq2.append(card1)
            deq2.append(card2)
            card_len2 += 1
            card_len1 -= 1
    elif card2 == 0:
        if card1 == 9:
            deq2.append(card1)
            deq2.append(card2)
            card_len2 += 1
            card_len1 -= 1
        else:
            deq1.append(card1)
            deq1.append(card2)
            card_len1 += 1
            card_len2 -= 1
    else:
        if card1 > card2:
            deq1.append(card1)
            deq1.append(card2)
            card_len1 += 1
            card_len2 -= 1
        else:
            deq2.append(card1)
            deq2.append(card2)
            card_len2 += 1
            card_len1 -= 1
    if card_len1 == 10:
        print('first', turns)
        exit_flag = True
    if card_len2 == 10:
        print('second', turns)
        exit_flag = True
    if turns == 1000000:
        print('botva')
        exit_flag = True
    





