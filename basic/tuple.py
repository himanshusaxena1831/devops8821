# tuple = ('apple', 'banana', 'kiwi')
# print(tuple[1])
# # I want to change the value of tuple firstly i want to change the tuple into list and change the value and change it back in tuple 

# x = list(tuple)
# x[1] = "Pinapple"
# tuple = tuple(x)
# print(y)
X = ('apple', 'banana', 'kiwi')
y = list(X)
print(X)
# y[1] = 'Pinapple'
# X = tuple(y)
# print(X)
y.append('papaya')
X = tuple(y)
print(X)