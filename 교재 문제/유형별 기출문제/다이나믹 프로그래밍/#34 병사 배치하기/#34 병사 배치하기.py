n = int(input())

data = list(map(int,input().split()))

count = [1] * (n)

for i in range(1,len(data)):
    for j in range(0,i):
        if data[i]<data[j]:
            count[i] = max(count[j]+1,count[i])


print(int(n-count[-1]))