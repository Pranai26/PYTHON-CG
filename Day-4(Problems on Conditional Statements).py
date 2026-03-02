#print the even numbers
"""num = (int(input("enter the even number:")))
for i in range(0,num):
    if i % 2 == 0:
        print(i)"""


num = int(input("Enter a number: "))

# 1. Even or Odd
if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")

# 2. Divisible by 5 or not
if num % 5 == 0:
    print("The number is divisible by 5")
else:
    print("The number is not divisible by 5")

# 3. Divisible by both 3 and 5
if num % 3 == 0 and num % 5 == 0:
    print("The number is divisible by both 3 and 5")
else:
    print("The number is not divisible by both 3 and 5")
    
# 4. Divisible by any one of 4 or 6
if num % 4 == 0 or num % 6 == 0:
    print("The number is divisible by 4 or 6")
else:
    print("The number is not divisible by 4 or 6")
