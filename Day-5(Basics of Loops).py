#Find whether the number is +ve even or -ve even or +ve odd or -ve odd
num = int(input("Enter a number: "))
if num >= 0 and num %2 == 0:
    print("number is positive even")
elif num <= 0 and num %2 == 0:
    print("number is negative even")
elif num >= 0 and num %2 == 1:
    print("number is negative odd")
elif num <= 0 and num %2 == 1:
    print("number is negative odd")
else:
    print("enter a valid number")


#Find which among the three numbers is the bigest number
num1,num2,num3 = map(int,input().split())
if num1>num2 and num1>num3:
    print(f"{num1} is the bigest number")
elif num2>num1 and num2>num3:
    print(f"{num2} is the bigest number")
else:
    print(f"{num3} is the bigest number")

n1,n2,n3 = map(int,input().split())
if n1>n2 and n1>n3:
    print("n1 is big")
elif n2>n3:
    print("n2 is big")
else:
    print("n3 is big")

#to find given num is +ve even,+ve odd, -ve even, -ve odd
num=int(input("enter the number:"))
if num>0:
    if num%2==0:
        print("+ve even")
    else:
          print("+ve odd")
else:
    if num%2==0:
        if num<0:
          print("-ve even")
    else:
          print("-ve odd")
          
#which number is greater 
a,b,c=map(int,input().split())
if a>=b:
    if a>=c:
        print("a is greater")
    else:
        print("c is greater")
else:
    if b>=c:
        print("b is greater")
    else:
        print("c ic greatest")
