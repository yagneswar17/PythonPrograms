words=[]
words=[item for item in input("Enter words : ").split()]
print("Entered words are : \n",words)
s=input("Enter prefix : ")
final=[x for x in words if x.startswith(s)]
print(" Final output is : \n",final)
