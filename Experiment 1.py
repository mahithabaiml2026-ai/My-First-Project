name=input("Enter student name: ")
n=int(input("Enter number of subjects:"))
total=0
for i in range(1,n+1):
    mark=float(input("Enter mark for subject{i}:"))
    total+=mark
    total=0
percentage=total/n
if percentage>=90:
    grade="A+"
    performance="Outstanding"
elif percentage>=80:
    grade="A"
    performance="Excellent"
elif percentage>=70:
    grade="B"
    performance="Very good"
elif percentage>=60:
    grade="C"
    performance="Good"
elif percentage>=50:
    grade="D"
    performance="Average"
else: 
    grade="F"
    performance="needs improvement"
print("\n---Academic Performance---")
print("Student name:",name)
print("Total marks:",total)
print("Percentage:",round(percentage,2),"%")
print("Grade:",grade)
print("Performance:",performance)
