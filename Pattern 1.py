k=int(input())
s=0;p=0
n=k
for i in range (1,k+1):
    s=s+i
for i in range (1,k-1):
    p=p+s[i]
p=p[::-1]
i=0;k=""
while(i<n*n):
    if(i+len(s)-k==n*n):
        k=k+s
        i=i+len(s)
    else:
        e=i+len(s)-(n*n)
        k=k+s[::e]
        break
    if (i+len(p)-k==n*n):
        k=k+p
        i=i+p
    else:
        e=i+len(p)-(n*n)
        k=k+p[::e]
        break
print(k)
