# # collection are used to store multiple items in a single variable. 
# # 1) list: ordered, mutable(changeable) collection of items
# # 2) it contain items different data type
# # 3) defined using the squire brackets [].

# set= [apple, banana, graps, ]
# print(set[2])

# list.append(399)
# print(list)
# list.insert(2, 195)
# print(list)
# list2 = [85, 86, 958, 9124]
# list.extend(list2)
# print(list)

# tuple = (84, 79, 89, 192, 185, 189)
# list.extend(tuple)
# print(list)
# list.remove(35)
# print(list)

# # list.remove()
# # print(list)
# # list.pop(4)
# # print(list)
# # del list[2] 
# # print(list)
# list.clear()
# print(list)
###############################################
###############################################

# list = [34, 35,59, 83, 19, 38, 35]

# # for i in list:
#     # print(i)
# # using while loop 
# i = 0
# while i < len(list):
#     print(list[i])
#     i = i + 1 
# fruits = ["Apple", 'banana', "kiwi", "Cherry"]
# newlist = []

# for X in fruits:
#     if "a" in X:
#         newlist.append(X)
# print(newlist)
#### comprehension #############
# newlist = [x for x in fruits if 'a' in x]
# newlist = [x if x != "banana" else "kiwi" for x in fruits]

# print(newlist)
# fruits.sort()
# print(fruits)
# fruits.sort(key=str.upper)
# print(fruits)
# fruits.reverse()
# print(fruits)
fruits = ["Apple", 'banana', "kiwi", "Cherry"]
print(fruits)
# mylist = fruits.copy()
# print(mylist)
# mylist = list(fruits) # list method 
# print(mylist)
mylist = fruits[ : ]  # slice operetor 
print(mylist)
