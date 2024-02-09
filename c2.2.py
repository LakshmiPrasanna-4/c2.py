# Write a program to print given number is a palindrome number or not.

n=int(input())
t=n
res=0
while n!=0:
    r=n%10
    n=n//10
    res=res*10+r
print(res)
if(res==t):
    print('Palindrome')
else:
    print('Not a Palindrome')

