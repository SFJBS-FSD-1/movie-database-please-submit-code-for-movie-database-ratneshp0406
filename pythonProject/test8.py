# print('hello')
# lst = [20,30,40,50,60,60]
# print(lst)
# lst.append(60)
# print(lst)
# list1=[]
# for i in lst:
#     if i != 60:
#         list1.append(i)
#
# print(list1)

dict = {'india':'delhi','bangladesh':'dhaka', 'srilanka':'colombo'}
print(dict)
dict['india']='new delhi'
print(dict)

dict1={}
for k,v in dict.items():
    dict1[v]=k
print(dict1)