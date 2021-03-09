##Program to Loop through names
import random
names_list = []
for x in range(0,8):
    name = input("Enter a name : ")
    print("x:", x)
    names_list.append(name)
print(names_list)
n = random.randint(0,7)
print("n:" ,n)
print("Name: ",names_list[n])
