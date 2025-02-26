print(id(1))
id = 1
print(id(1))

a, b = 1, 2

c = a
b = a
a = c

a,b = b,a
