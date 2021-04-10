N=int(input("Enter N :"))
i=0
while i<N:
    A=int(input("Enter A:"))
    B=int(input("Enter B:"))
    m=0
    n=0
    if A%B == 0:
        print("A \n")
    elif B%A == 0:
        print("B \n")
    elif A==B:
        print("Tie \n")
    else:
        j=1
        while j<=B:
            if A%j==0:
                m=m+1
            if B%j==0:
                n=n+1
        if m>n:
            print("A \n")
        elif m<n:
            print("B \n")
        else:
            print("Tie \n")
