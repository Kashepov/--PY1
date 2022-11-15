import random
import string


def get_random_password(size) -> str:
    alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits
    n = random.randrange(size, len(alphabet), 1)
    password = "".join(random.sample(alphabet, n))
    return password  # TODO написать функцию генерации случайных паролей


print(get_random_password(8))
