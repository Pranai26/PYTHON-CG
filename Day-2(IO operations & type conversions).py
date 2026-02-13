"""# read input numbers from user
num = input()
print(type(num)) # checking the type of the number
print(num)"""


"""# implecit Type Conversion

num1 = int(input())
val = float(input())
print(type(num1), type(val)) #checking the type of number
res = num1 + val
print(res)"""


"""num1= input() #read string type of number
print(type(num1))#checking the type of number
res = num1 + 10
print(res)"""


"""#To overcome the above problem using Explict Type Conversion
num1= input() #read string type of number
print(type(num1))#checking the type of number
res = int(num1) + 10 #TypeError: can only concatinate str (not "int") to str
print(res)"""


"""#Converting integer to float, string & boolean
num = 123
print(float(num))
print(str(num))
print(bool(num))"""


n = "hi"
print(bool(n))


