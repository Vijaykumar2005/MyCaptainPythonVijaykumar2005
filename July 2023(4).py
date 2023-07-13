list1=[12,-7,5,64,-14]
for i in list1:
  if i<0:
    list1.remove(i)
separator=","
print(separator.join(map(str,list1)))

list2=[12,14,-95,3]
for j in list2:
  if j<0:
    list2.remove(j)
print(list2)
