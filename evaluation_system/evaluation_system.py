print("Introduce the requested data to calculate your average grade: ")

#Request the student's name
name = input("Name: ")
upper_name = name.upper()
total_sum = 0

#Request the 3 grades
for i in range(3):
    grade = float(input("Introduce your grade: "))
    total_sum += grade

#Calculate the average grade
def calculate_average(total_sum):
    average_grade = total_sum / 3
    return average_grade
average_grade = calculate_average(total_sum)

#Print message
print("Name: ", upper_name)
print("Your average grade is: ", average_grade)