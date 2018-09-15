import re
from unidecode import unidecode


def sanitise(word):
    word = word.lower()
    word = unidecode(word)
    word = re.sub(r'[^a-z0-9\-]+', '', word)
    return word
