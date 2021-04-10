def func(N, t):       
    if (t > 20): 
        return
    print(N,"*",t,"=",N * t) 
    return func(N, t + 1) 
for i in range (10,20+1):
    func(i, 10)
    print("\n ")
