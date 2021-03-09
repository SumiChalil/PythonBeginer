"Program To Print Initials"
firstName = input("Please enter your first name ")
middleName = input("Please enter your middle name ")
lastName = input("Please enter your last name ")
firstInitial = firstName[0]
middleInitial = middleName[0]
lastInitial = lastName[0]
myName = firstName + " " + middleName + " " + lastName
myInitial = firstInitial + middleInitial + lastInitial
print( "Full Name:", myName)
print(" Initials:", myInitial)
