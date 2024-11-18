def count_calls():
    return calls

def string_info(string: str):
    global calls
    calls += 1

    if string .isalpha():
        return len(string ), string .upper(), string .lower()

def is_contains(string , list_to_search):
    global calls
    calls += 1
    for word in list_to_search:
        if string.lower() in word.lower():
            return True
    return False


calls = 0

print(string_info('Capybara'))

print(string_info('Armageddon'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN

print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches

print(calls)
