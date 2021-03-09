##Program to determine grade of students
grade1 = float(input("Enter the grade of student in first class "))
grade2 = float(input("Enter the grade of student in second class "))
abscence = int(input("Enter the no. of abscent classes "))
no_of_classes = int(input("Enter the total no. of classes "))
avgMarks = (grade1 + grade2)/2
attendance = (no_of_classes - abscence)/no_of_classes

print("Average Marks =", round(avgMarks,2))
print("Attendence Percentage =", str(round((attendance*100),2))+"%")
if (avgMarks >= 6 and attendance >= 0.8):
    print("The student has been approved")
elif(avgMarks < 6 and attendance < 0.8):
    print("The student failed due to average marks less than 6 and an attendence rate lower than 80%")
elif(attendance >= 0.8):
    print("The student failed due to average marks less than 6")
else:
    print("The student failed due to an attendence rate lower than 80%")

