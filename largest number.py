s,n=input().split()
k=int(n)
lst=list(s)
for i in range (0,k):
    if(lst[i]!='9'):
        lst[i]='9'
    else:
      k+=1
for i in range (0,len(lst)):
    print(int(lst[i]),end="")
