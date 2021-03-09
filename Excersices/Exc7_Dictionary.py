##Dictionary
##Programm to Get value based on the Key Passed
personDict = {"Name":"Ronald Weasley","Gender":"Male","Age":31,"Address":"Park Avenue,3rd Street,London","PhoneNo":"+219987567"}
key = input("Please enter key input ")
value = personDict.get(key,"Invalid Input")
print(key, "of the person is" , value)
