
str1=str(input("Enter a string"))
str2=str(input("Enter a character to serach in a string"))
str_updated=list(str1)
for i in list(str1):
    if (i==str2):
        str_updated.remove(i)
print(str(str_updated))

