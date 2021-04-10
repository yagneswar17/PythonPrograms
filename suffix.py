words=[]
words=[item for item in input("Enter words : ").split()]
print("Entered words are : \n",words)
s=input("Enter suffix : ")
final=[x for x in words if x.endswith(s)]
print(" Final output is : \n",final)
