def get_matrix(n=2, m=2, value=10):
    matrix = []

    # В случае передачи аргумента со значением 0 или меньше,
    # будет возвращаться пустой список.
    if n <= 0 or m <= 0 or value <= 0:
        return matrix

    for x in range(n):
        matrix.append([]) # добавляем пустые списки
        for j in range(m):
            matrix[x].append(value) # Добавляем значения по индексу x

    return matrix


result1 = get_matrix(2, 2, 10)

result2 = get_matrix(3, 5, 42)

result3 = get_matrix(4, 2, 13)

result4 = get_matrix(2, 0, 1)

print(result1)
print(result2)
print(result3)
print(result4)
