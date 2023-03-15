str1 = '3 2 1'

n,a,b = map(int,str1.split())

if a > b:
    bigger = a
    smaller = b
else:
    bigger = b
    smaller = a

if n == 0:
    print(0)
elif n == 1:
    print(0)
elif n == 2:
    print(bigger)
else:
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 0
    dp[2] = bigger
    for i in range (3,n+1):
        variants = n*bigger
        for k in range(1, i//2 +1):
            current_variant = (max(dp[k] + bigger, dp[i-k] + smaller))
            if current_variant < variants:
                variants = current_variant
        dp[i] = variants
    print(dp[-1])



