# list_1 = []
# list_2 = []
# var = 'None'
# while(var !='end'):
#    var = input("Enter a value for list 1 or enter end to  finish")
#    if var != 'end':
#       list_1.append(var)
# var = 'None'
# while(var !='end'):
#    var = input("Enter a value for list 2 or enter end to  finish")
#    if var != 'end':
#       list_2.append(var)
#
# jj=[]
# minlen= len(list_1) if len(list_1) <= len(list_2) else len(list_2)
# Match = 0
# for i in range(0,minlen):
#     jj = list(list_2[i])
#     if(len(list_1[i]) == len(list_2[i])):
#          count = 0
#          Match = 0
#          for h in list(list_1[i]):
#              count = 0
#              for k in list(list_2[i]):
#                 if (h==k):
#                    count = 1
#                    for y in jj:
#                        if (h==y):
#                            jj.remove(y)
#                    break
#              if count != 1 and len(jj) == 1:
#                 Match = Match + 1
#          if Match == 1:
#             print(f'{list_1[i]} , {list_2[i]} elements has only one difference')

# list_1 = []
# list_2 = []
# var = 'None'
# while(var !='end'):
#    var = input("Enter a value for list 1 or enter end to  finish")
#    if var != 'end':
#       list_1.append(var)
# var = 'None'
# while(var !='end'):
#    var = input("Enter a value for list 2 or enter end to  finish")
#    if var != 'end':
#       list_2.append(var)
# minlen= len(list_1) if len(list_1) <= len(list_2) else len(list_2)
# Match = 0
# for i in range(0,minlen):
#     jj = list(list_2[i])
#     kk = list(list_1[i])
#     mm = list(list_1[i])
#     if(len(list_1[i]) == len(list_2[i])):
#          for h in mm:
#              for k in jj:
#                 if (h==k):
#                    jj.remove(k)
#                    kk.remove(h)
#                    break
#          if len(jj) == 1 and len(kk)== 1:
#             print(f'{kk} , {jj} are the only differnt elements in the LIST1 {list(list_1[i])} AND LIST2 {list(list_2[i])}')



list_1 = ['aabbc', 'aabcddef', 'aabcddef', 'abdddccc','abdddcccf']
list_2 = ['bbaad', 'abbcddef', 'abbcdeef', 'abdddcce','abdddcceg']

count=0
j=0
def returndictionay(list_1):
    dict1 = {}
    for i in list(list_1):
        count=0
        for j in list(list_1):
            if(i==j):
                count=count+1
            dict1.update({i:count})
    return(dict1)

def compareelemets(dict2,dict3):
    count=0
    if (len(dict2)) == (len(dict3)) :
        for key,value in dict2.items():
           if key not in dict3.keys() or value not in dict3.values():
               count = count + 1
        if count == 0:
           key_count = 0
           for key1,value1 in dict2.items():
                for key2, value2 in dict3.items():
                    if(key1 == key2 and value1 != value2 ):
                        key_count=key_count + 1
                        val= value1-value2 if value1 > value2 else value2-value1
                        count = 1
                        if val > 1 or key_count > 2:
                            count = 0
                            return count
    elif ((len(dict2)) - (len(dict3)) == 1 or (len(dict2)) - (len(dict3)) == -1 ) :
         if len(dict2) < len(dict3):
             temp=dict2
             dict2=dict3
             dict3=temp
         key_count=0
         for key1, value1 in dict2.items():
             if key1 not in dict3.keys():
                key_count = key_count + 1
                if value1 > 1 or key_count > 1:
                    return count + 1
             for key2, value2 in dict3.items():
                if (key1 == key2 and value1 != value2):
                    count = count + 1
    return(count)

minlen= len(list_1) if len(list_1) <= len(list_2) else len(list_2)
Match = 0
for i in range(0,minlen):
    if(len(list_1[i]) == len(list_2[i])):
        dict2 = returndictionay(list_1[i])
        dict3 = returndictionay(list_2[i])
        count=compareelemets(dict2,dict3)
        if(count==1):
            print(f'Only one differnce found b/w {list_1[i]} and {list_2[i]} ')