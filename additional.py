grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
class_dict = dict({})
students=list(students)
students.sort()                              #множество приводим к списку и сортируем в алфавитном порядке
print(students)
grades_median=[]
for i in grades:                             #используем цикл и проходимся по каждому элементу и считаем среднюю оценку
    medium_grade = sum(i)/len(i)
    grades_median.append(medium_grade)
class_dict = dict(zip(students,grades_median)) #используем zip чтобы соединить два списка
print((class_dict.items()))
