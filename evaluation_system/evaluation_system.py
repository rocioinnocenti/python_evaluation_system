#Determine the student's status based on their average grade
def status(average_grade):
    if 1 <= average_grade < 5:
        message = "FAILED"
    elif 5 <= average_grade < 7:
        message = "PASSED"
    elif 7 <= average_grade < 9: 
        message = "GOOD"
    elif 9 <= average_grade <= 10:
        message = "EXCELLENT"
    else:
        message = "Something went wrong. You must enter grades between 1 and 10."
    return message

#Add loop to ask 5 students
for i in range(5):

#Request data
    print("Please, introduce the requested data to calculate your average grade: ")

#Request the student's name
    name = input(f"Name {i + 1}: ")
    upper_name = name.upper()
    total_sum = 0

#Request the 3 grades
    for j in range(3):
        grade = float(input(f"Grade {j + 1}: "))
        total_sum += grade

#Calculate the average grade
    def calculate_average(total_sum):
        average_grade = total_sum / 3
        return average_grade
    average_grade = calculate_average(total_sum)
    student_status = status(average_grade) 

#Print message
    print("Name: ", upper_name)
    print("Your average grade is: ", average_grade)
    print("Your status is: ", student_status)