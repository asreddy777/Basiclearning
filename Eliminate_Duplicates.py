#m=list(input("Enter a values to store in list"))
m=[]
var = 'None'
while(var !='end'):
   var = input("Enter a value for list 1 or enter end to  finish")
   if var != 'end':
      m.append(var)
x=[]
for i in m:
    x.append(i.upper())
k=1
New_List=x[k:]
for i in x:
    for j in New_List:
        if( i==j ):
            x.remove(j)
    k=k+1
    New_List=x[k:]
print(f"list after eleminating duplicates {x}")

