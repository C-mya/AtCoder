
N, K = list(map(int, input().split()))

a=[1 for i in range(N+1)]
ans=K
if 0 <= N < K:
    total = 1
else:
    for i in range(K,N+1):
        a[i]=ans
        ans-=a[i-K]
        ans+=a[i]
        ans%=10**9
    
print(a[N])
