calls = 0


def count_calls():
    global calls
    calls = 1


def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())


print(string_info('Copybara'))
print(string_info('Armageddon'))
print(calls)
