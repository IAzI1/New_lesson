import os


def custom_write(file_name, strings):
    strings_positions = {}

    # with open(file_name, 'w', encoding='utf-8') as file:
    #     for string in strings:
    #         file.write(f'{string}\n')

    with open(file_name, 'r+', encoding='utf-8') as file:
        count_line = 0
        for string in strings:
            count_line += 1
            strings_positions[(count_line, file.tell())] = string
            file.write(f'{string}\n')

    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
