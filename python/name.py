num = int(input("Enter any number:"))
if num%2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")


# list 

names = ["jassi","manya","kunwar"]
print(names)
# appending  in the list
names.append("khyati")
# sorting the list
names.sort()
#the no of elements in the list:
print(f"The total elements in the list are: {len(names)}")
print(names)


#sets

#an empty set
set1 = set()
# no element repeats more than once. 
#adding element
set1.add(1)
set1.add(5)
set1.add(2)
set1.add(3)
set1.add(4)
print(set1)
set1.remove(3)
print(set1)
print(f"the total number of the elements are {len(set1)}")