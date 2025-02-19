import random
import string


def text_generator(limitation: int) -> str:
    return ''.join(random.choices(string.ascii_letters, k=limitation)).lower()


def email_generator(limitation: int = 12) -> str:
    domains = ['.ru', '.com', '.ya']

    text = text_generator(limitation=limitation)
    domain = random.choice(domains)

    return f'{text}@test{domain}'
