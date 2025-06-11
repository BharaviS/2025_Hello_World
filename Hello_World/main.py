print("Hello World!")

#(input("Enter a value: "))

"""for i in range (1, 5):
    for j in range (1, 5):
        print(i, end=" ")
    print()"""

"""for i in range (1, 6):
    for j in range (i):
        print(i, end=" ")
    print()

for i in range (4, 0, -1):
    for j in range (1, i + 1):
        print(i, end=" ")
    print()"""

"""while True:
    i = int(input("Enter a value: "))

    if i==1:
        print(i)
    elif i<1:
        print("The value is smaller than 1.")
        break
    elif i>1:
        print("The value is bigger than 1.")
        break
    else:
        print("Enter correct value")"""

#print(help('if'))
#print(12<<2)

# Tuple is store sequence of immutable data.
my_tuple = (11, 55, 26, 25)
print(my_tuple)
print(type(my_tuple))
print(my_tuple[1:7])

# List is a store sequence of mutable data.
my_list = ['a', 'b', 2 , 2.5]
print(my_list)
print(type(my_list))
my_list[1] = 'c'
print(my_list)

#Set To store unorder and unindexed values.
my_set = {1, 3, 5, 7}
print(my_set)
print(type(my_set))
my_set.add(300)
print(my_set)
my_set.remove(3)
print(my_set)

#my code
list1 = [3, 4,8,9, 25]

for i in list1:
    print(i, end=" ")
print()

#bytearray
list1 = [3, 4,8,9, 25]
b_array = bytearray(list1)
print(b_array)
print(type(b_array))

#For loop
summ = 1
for i in range (1, 22, 1):
    summ = i * i
    print(summ)

#dictonery
dicts = {'js': 'atom', 'cs': 'vs code', 'python': ['pycharm', 'sublime'], 'java': {'jse': 'netbeans', 'jee': 'eclipse'}}

print(dicts)
print(dicts['python'])
print(dicts['python'][0])
print(dicts['java'])
print(dicts['java']['jee'])