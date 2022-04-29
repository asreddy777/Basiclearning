d1={1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',0:'Zero'}
i1=int(input("Enter a integer"))
k=''
for i in str(i1):
    k=k+(d1.get(int(i)))
    k=k + " "
print(k)