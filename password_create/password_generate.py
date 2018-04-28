import random

def generate_password():
    return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)


def generate_password2():
    return str().join(random.sample(word_list,3))