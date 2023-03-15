str1 = '10 3'
str2 = '2 4 7'

l,n = map(int,str1.split())
saw_list = list(map(int,str2.split()))
list_saw = [0]
list_saw.extend(saw_list)
list_saw.append(l)

dp=[]

for l in range(n+2):
    raw = []
    for r in range(n+2):
        raw.append(0)
    dp.append(raw)

for l in range(n+2):
    for r in range(n+2):
        if r == l+2:
            dp[l][r] = list_saw[r] - list_saw[l]

for i in range(3,len(list_saw)):
    for l in range(n+2):
        for r in range(n+2):
            if r == l+i:
                variants = []
                for k in range(1,i):
                    midle = l+k
                    variants.append(dp[l][midle] + dp[midle][r])
                dp[l][r] = list_saw[r] - list_saw[l] + min(variants)

print(dp[0][len(list_saw)-1])