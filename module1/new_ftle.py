grades: list = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students: set = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sorted_students: list = sorted(students)
new_dict: dict = {}
iter = 0
for student in sorted_students:
    avarage_value = sum(grades[iter]) / len(grades[iter])
    new_dict[student] = avarage_value
    iter += 1
print(new_dict)