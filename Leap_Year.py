
i1=int(input("Enter a integer"))
if (i1%4 == 0):
    if (i1>= 100 and i1%100 == 0 and i1%400 == 0):
        print(f'{i1} is leap year')
    else :
        print(f'{i1} is not leap year')
else :
    print(f'{i1} is not leap year')