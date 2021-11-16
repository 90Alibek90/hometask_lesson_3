en_ru_dict = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}

def num_translate_adv (en_word):
    if en_word[0].isupper():
        en_word = en_word.lower()
        return en_ru_dict[en_word].capitalize()
    else:
        return en_ru_dict[en_word]


print(num_translate_adv('seven'))
print(num_translate_adv('Seven'))