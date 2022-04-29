x=int(input("Enter an integer"))
count=0
for i in range(2,10):
    if((x != i) and (x%i == 0 or x==1 or x== 0)):
        count=1
        print(f"{x} is not prime number")
        break
if (count==0):
    print(f"{x} is prime number")