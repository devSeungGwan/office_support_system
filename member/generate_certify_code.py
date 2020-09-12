import random
import string

def generate_code():
    length = 10
    str_set = string.ascii_lowercase

    result = ''

    for i in range(0, length):
        result += random.choice(str_set)

    return result
