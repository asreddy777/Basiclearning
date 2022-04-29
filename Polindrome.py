# x=int(input("Enter an integer"))
# temp=x
# y=0
# while(x>0):
#     if(x>10):
#        y=(x%10+y)*10
#     else:
#         y = (x % 10 + y)
#     x=int(x/10)
# if(y==temp):
#     print(f"{temp} is Polindrome")
# else:a
#     print(f"{temp} is Not Polindrome")

x=input("Enter an integer")
if(str(x)==str(x)[::-1]):
    print(f"{x} is polindrome")
else:
    print(f"{x} is not polindrome")
