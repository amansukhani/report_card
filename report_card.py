#creates a file report_card.txt that has the grades of all the students

import csv

with open('students.csv', mode='r') as students_file:
	student_reader = csv.DictReader(students_file)
	students = []  #dictionary to store contents of students.csv
	for row in student_reader:
		individual_student = []
		individual_student.append(int(row["id"]))
		individual_student.append(row["name"])
		students.append(individual_student)
	

with open('marks.csv', mode = 'r') as marks_file:
	marks_reader = csv.DictReader(marks_file)
	marks = []
	for row in marks_reader:
		individual_marks = []
		individual_marks.append(int(row["student_id"]))
		individual_marks.append(int(row["test_id"]))
		individual_marks.append(int(row["mark"]))
		marks.append(individual_marks)

with open('tests.csv', mode = 'r') as tests_file:
	tests_reader = csv.DictReader(tests_file)
	tests = []
	for row in tests_reader:
		individual_tests = []
		individual_tests.append(int(row["course_id"]))
		individual_tests.append(int(row["id"])) #actually test_id
		individual_tests.append(int(row["weight"]))
		tests.append(individual_tests)
	

with open('courses.csv', mode = 'r') as courses_file:
	courses_reader = csv.DictReader(courses_file)
	courses = []
	for row in courses_reader:
		individual_courses = []
		individual_courses.append(int(row["id"])) #actually course id
		individual_courses.append(row["name"]) #name of course
		individual_courses.append(row["teacher"]) #name of teacher
		courses.append(individual_courses)
	

final = []

for i in range(len(students)):
	final_row = []
	final_row.append(students[i][0])
	final_row.append(students[i][1])
	avg_grade = 0
	for j in range(len(courses)):
		total_wt = 0
		total_grade = 0
		#weight_individual = []
		final_row.append(courses[j][1])
		final_row.append(courses[j][2])

		for k in range(len(tests)):
			if(courses[j][0] == tests[k][0]):
				total_wt = total_wt + tests[k][2]
				for l in range (len(marks)):
					if(students[i][0] == marks[l][0] and marks[l][1] == tests[k][1]): #if the student id matches
						total_grade = (tests[k][2]/100) * marks[l][2] + total_grade
	
		final_row.append(total_grade)
		avg_grade += total_grade/(len(courses))
	final_row.append(avg_grade)
	final.append(final_row)
print(final)
	

report_file = open('report_card.txt', mode = 'w')
for i in range(len(students)):
	l = len(final[i])
	report_file.write("Student Id: {}, name: {} \n".format(final[i][0], final[i][1]))
	report_file.write("Total Average:      {:.2f}%\n\n".format(final[i][l-1]))
	for j in range(0,len(courses)*3, 3):
		report_file.write("     Course: {}, Teacher: {}\n".format(final[i][j+2],final[i][j+3]))
		report_file.write("     Final Grade:   {:.2f}%\n\n".format(final[i][j+4]))


report_file.close()


	



