a=1
b=1
c=1
d=1
ans=1
i=200
j=99
k=1
l=1
while l<102:
    c=c*l
    l=l+1
while k<100:
    d=d*k
    k=k+1
while i>101:
    a=a*i
    i=i-1
while j>0:
    b=j*b
    j=j-1
ans=(a//b)*c*d
print(ans)
