
thistupule = ('Dipto', "subro",'mita', )

print(thistupule)


thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# Tuple Length
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(len(thistuple))

# Access Tuple Items


thistuple = ("apple", "banana", "cherry", "apple", "cherry")

print(thistuple[1])
thistuple = ("apple", "banana", "cherry", "apple", "cherry")

print(thistuple[4])

# Update Tuples 1
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# Update Tuples 2

x= ("apple", "banana", "cherry", "apple", "cherry")
y=list(x)
y.append("Chagol")
x=tuple(y)
print(x)

# Update Tuples 2 

x=("apple", "banana", "cherry", "apple", "cherry")
y=("pagol",)
x += y
print(x)

# Remove Items 1 
 
x= ("apple", "banana", "cherry", "apple", "cherry")

y= list(x)
y.remove('apple')
x=tuple(y)

print(x)

x=("apple", "banana", "cherry", "apple", "cherry")
del x
print(x)

# Unpacking  
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# Join Two
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
 
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)