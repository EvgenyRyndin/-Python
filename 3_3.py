def thesaurus(*names):
    letter_dict = dict()
    for name in names:
        letter_dict.setdefault(name[0], [])
        letter_dict[name[0]].append(name)
    return letter_dict


print(thesaurus('Иван', 'Мария', 'Петр', 'Илья'))
