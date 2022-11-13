def get_unique_list_numbers() -> list[int]:
    from random import randint
    unique = []
    while len(unique) != 15:
        for i in range(15):
            i = randint(-10, 10)
        if i in unique:
            continue
        else:
            unique.append(i)
    return unique  # TODO написать функцию для получения списка уникальных целых чисел


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
