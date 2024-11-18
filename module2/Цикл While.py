list_numb = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

index = 0
count = len(list_numb)

while True:
    if count == 0 or list_numb[index] < 0:
        break
    print(list_numb[index])
    index += 1
    count -= 1


