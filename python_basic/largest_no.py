#largest of three numbes
a=int(input("enter a first number:"))
b=int(input("enter a secound number:"))
c=int(input("enter a third number:"))
if a>=b and a>=c:
    print("larest:",a)
elif b>=a and b>=c:
    print("largest:",b)
else:
    print("largest:",c) 