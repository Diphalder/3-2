n=int(input("fibonacii digit = "))
dp={}
for i in range(n+1):
    dp[i]=-1


def fibo(n):
    global dp
    if(dp[n]!=-1):
        return dp[n]
    if(n==1):
        return 0
    if(n==2):
        return 1
    dp[n]=fibo(n-1)+fibo(n-2)
    return dp[n]


for i in range(n):
    print(fibo(i+1) ,end=",")