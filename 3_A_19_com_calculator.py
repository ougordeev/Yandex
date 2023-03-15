str1 = '2'
str2 = '1 1'

import heapq
n = int(str1)
numbers = list(map(int, str2.split()))
heapq.heapify(numbers)
ans = 0
while len(numbers) > 1:
    number1 = heapq.heappop(numbers)
    number2 = heapq.heappop(numbers)
    sum = number1 + number2
    ans += sum * 0.05
    heapq.heappush(numbers,sum)
print('{:.2f}'.format(ans))


