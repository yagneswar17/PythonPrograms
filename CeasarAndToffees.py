t=int(input())
for i in range (t):
    n,m=input().split()
    n=int(n)
    m=int(m)
    if(m%2==0 and n%2==0):
        if(((n%m)-(m//2))<0):
            print((n%m)+(m//2))
        else:
            print((n%m)-(m//2))
    else:
        print(n%m)
