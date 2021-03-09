##To print month of birth after accepting DOB in DD-MM-YYYY format
dOB = input("Please enter your DOB in DD-MM-YYYY format")
month = int (dOB[3:5])-1
monthsInYear = ("January","February","March","April","May","June","July","August","September","October","November","December")
monthOfBirth = monthsInYear[month]
print("You were born in ", monthOfBirth)
