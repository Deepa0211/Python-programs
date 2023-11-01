# Input -> [1, 1, 2, 2, 3, 3, 4, 4]
# Outpiut -> [1, 2, 3, 4]

list_1 = [1, 1, 2, 2, 3, 3, 4, 4]
list_2 = [1, 2, 3, 4]

list= []

for i in list_1:
    if i not in list:
       list.append(i)
print(list)