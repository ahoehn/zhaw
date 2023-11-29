import copy

# list
x = [*range(5)]  # unpack * operator to unpack range to list
z = x[0:5]
print(type(z))
print(x)
y = x[0:5]
print(y)
z[0] = -1
x.remove(0)
y.append(11)
print("Influence on x", x)
print("Influence on y", y)
print("Influence on z", z)

for item in x:
    print(item)
    print("me too")
print("me not")

# set
a = {1, 1, 2, 3}  # unique => 1,2,3
a.add(4)
a.remove(2)
print(a)

b = set(y)
print(b)

# tuple
c = 1, 2
print(c)
d = 1, 2, 3
print(d)

# dictionary
e = {"me": "too", "you": "not", 5: "test"}
print(e)
e["they"] = {"maybe": "too"}
print(e)
print(e.get("you"))
print(e.pop(5))
print(e)
print("test" in e)
print(e.get("test", "does not exists"))
f = e.copy()
print(f)
f = copy.deepcopy(e)
print(f)

# 2d init
g = []
for row in range(4):
    g += [*range(4)]
print(g)
