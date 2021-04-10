t=int(input())
i=0
while i<t:
    a=1
    b=1
    n,r=[int(r) for r in input().split()]
    if n-r<r:
        j=n
        while j>n-r:
            a=a*j
            j=j-1
        j=r
        while j>1:
            b=b*j
            j=j-1
        print(a//b,"\n")
    else:
        j=n
        while j>r:
            a=a*j
            j=j-1
        j=n-r
        while j>1:
            b=b*j
            j=j-1
        print(a//b,"\n")
    i=i+1
