#finding the length of number
n=int(input())
count=0
while n>0:
    n//=10
    count+=1
print(count)
    
#finding the sum of number
n=int(input())
sum=0
while n>0:
    rem=n%10
    sum+=rem
    n//=10
print(sum)
#reverse of numbers
n=int(input())
rev=0
while n>0:
    rem =n%10
    rev=rev*10+rem
    n//=10
print(rev)
#palindrome number or not
n=int(input())
rev=0
pal=n
while n>0:
    rem=n%10
    rev=rev*10+rem
    n//=10
if (pal==rev):
    print("it is palindrome")
else:
    print("not a palindrome")
