### Lists ###

myLists = list()
myotherList = []

my_list = [1, 2, 3, 4, 5, 6, 7]
print(len(my_list))


my_other_list = [18, 1.80, "Carlos", "Abea"]
print(type(my_other_list))


print(my_other_list[2])
print(my_other_list[3])
print(my_other_list[-1])

print(my_other_list.count("carlos".capitalize()))

age, height, name, surname = my_other_list

print(age)

print(my_list + my_other_list)


my_other_list.append("Martinez")
print(my_other_list)

my_other_list.insert(1, "Negro")
print(my_other_list)

my_other_list.remove("Negro")
print(my_other_list)

my_list.pop()
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2]
print(my_list)



myNewList = my_list.copy()
my_list.clear()
print(my_list)
print(myNewList)


myNewList.reverse()
print(myNewList)

myNewList.sort()
print(myNewList)

print(myNewList[1:2])



