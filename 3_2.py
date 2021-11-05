words = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять',
}


def num_translate_adv(word):
    if word[0] == word[0].upper():
        word = word.lower()
        return words[word].capitalize()
    else:
        return words[word]


print(num_translate_adv('One'))
print(num_translate_adv('one'))
