students={'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades=[[5,3,3,5,4], [2,2,2,3], [4,5,5,2], [4,4,3], [5,5,5,4,5]]

students_list=list(students)
students_list.sort()
avg_grades={}
for student, grade in zip(students_list, grades):
   avg_grades[student]=sum(grade)/len(grade)
print(avg_grades)




