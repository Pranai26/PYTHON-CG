#To check which is odd and even  among the 3 numbers
"""n1,n2,n3 = map(int,input().split())
if (n1%2) == 0:
    print(f"{n1} is even number")
else:
    if n1%2 == 1:
        print(f"{n1} is odd number")
if (n2%2) == 0:
    print(f"{n2} is even number")
else:
    if n2%2 == 1:
        print(f"{n2} is odd number")
if (n3%2) == 0:
    print(f"{n3} is even number")
else:
    if n3%2 == 1:
        print(f"{n3} is odd number")"""


# FOR LOOP EXAMPLE
# Find which is even or odd from the list of numbers
"""lst = [1,2,3,4,5]
for ind in range(0,5,1):
    if ind%2 == 0:
        print(f"{ind} is even")
    else:
        print(f"{ind} is odd")"""


"""lst = [11,12,13,14,15]
for ind in range(0,5,1):
    if lst[ind]%2 == 0:
        print(lst[ind], "is even")
    else:
        print(lst[ind], "is odd")"""

"""lst = [11,12,13,14,15]
for i in range(0,5,1):
    if lst[i]%2 == 0:
        print(lst[i], "is even")
    else:
        print(lst[i], "is odd")"""


#Print even numbers between 20 to 40
"""#Approch 1
for i in range(20,41):
    if i%2 == 0:
        print(i)
#Approch 2
for i in range(20,41,2):
        print(i)"""

#print 1 - 100 numbers
"""#Approch 1
for i in range(1,101):
        print(i)
#Approch 2
for i in range(1,101):
        print(i, end = " ")"""


#Print the sum of n natural numbers
n = int(input())
total = 0
for i in range(1,n+1):
    total = total + i
print(total)
    
#while loop problems
#print numbers from 1 to 100
i=1
while i<=100:
    print(i)
    i+=1
#print even numbers between 10 to 40
i=10
while i<=40:
    if i%2==0:
        print( i,"even")
    i+=1
#print odd numbers between 1-50
i=1
while i<=50:
    if i%2==1:
        print(i,"odd")
    i+=1
#print which is even and which is odd
lst=[1,2,3,4,5,6,7,8,9]
ind=0
while ind <len(lst):
    if lst[ind]%2==0:
        print(lst[ind],"even")
    else:
        print(lst[ind],"odd")
    ind+=1
