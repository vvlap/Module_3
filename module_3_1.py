def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    count_calls()
    for i in range(len(list_to_search)):
        list_to_search[i] = list_to_search[i].upper()
    if string.upper() in list_to_search:
        return True
    return False

calls = 0
print(string_info('Эклектика'))
print(string_info('эЛеватор'))
print(is_contains('Эклер', ['Эклектика', 'эЛеватор', 'экЛер']))
print(is_contains('Булка', ['Эклектика', 'эЛеватор', 'экЛер']))
print(calls)