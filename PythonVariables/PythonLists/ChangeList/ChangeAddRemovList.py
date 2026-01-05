#  list Cheanges  
Thelist2 = [ ' ami ' , 'tumi', 'mylove','yourlove',"Dipto",'Bakshi', "mita","sumaya"] 

cheangesList = Thelist2[2]='mother'
print(Thelist2)

# Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)



#          Append Items

# Append Items use  append() method 


thislist = [ ' ami ' , 'tumi', 'mylove','yourlove',"Dipto",'Bakshi', "mita","sumaya"] 
thislist.append("mother")
print(thislist)

# Insert Items 
thislist4 = [ ' ami ' , 'tumi', 'mylove','yourlove',"Dipto",'Bakshi', "mita","sumaya"] 
thislist4.insert(4,"Mother")

print(thislist4)

# Extend List

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)



#            Remove List Items

thislist = [ ' ami ' , 'tumi', 'mylove','yourlove',"Dipto",'Bakshi', "mita","sumaya"] 
thislist.remove("tumi")
print(thislist)

#  Remove Specified Index
thislist = [ ' ami ' , 'tumi', 'mylove','yourlove',"Dipto",'Bakshi', "mita","sumaya"]  
thislist.pop(4)
print(thislist)

# If you do not specify the index, the pop() method removes the last item.
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# he del keyword also removes the specified index:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
# The del keyword can also delete the list completely.
thislist = ["apple", "banana", "cherry"]
del thislist

# Clear the List
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)