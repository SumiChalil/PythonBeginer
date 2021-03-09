##Add name at the end of predefined list
studentList =["Jack","Jill","John","Jerry"]
newName = input("Please enter your name ")
length = len(studentList)
#print("length ",length)
studentList.insert(length,newName)
print("New Students list " ,studentList)
