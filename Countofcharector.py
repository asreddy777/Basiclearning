str1=str(input("Enter a string"))
str2=str(input("Enter a character to serach in a string"))
count=0
j=0
for i in list(str1):
    if (i==str2):
       count=count+1
       print(f"{str2} found at position {j} in {str1}")
    j=j+1
print(f"{str2} found in {str1} {count} times" )
k=str1.find(str2[2:9])
print(str1.index(str2[::-1]))
print(k)

#7892297837 Aqua care OKI432740964