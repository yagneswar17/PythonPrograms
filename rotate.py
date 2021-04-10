'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
t=int(input())
for i in range(t):
    n=int(input())
    s=bin(n).replace("0b","")
    print(s)
    num=s
    l=0
    r=0
    while (num!=0):
        rem=num%10
        if(rem==1):
            l=l+1
        else:
            r=r+1
        num=num/10;
    s=list(s[l:])
    a=int(s,2)
    if(a%2==0):
        print('Even')
    else:
        s=lis(s[:r])
        a=int(s,2)
        print(a)
