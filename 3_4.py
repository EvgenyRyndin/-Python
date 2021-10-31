def thesaurus_adv(*names_surnames):
    letters_dict = {}
    for name_surname in names_surnames:
        name, surname = name_surname.split()
        letters_dict.setdefault(surname[0], {})
        letters_dict[surname[0]].setdefault(name[0], [])
        letters_dict[surname[0]][name[0]].append(name_surname)

    sorted_dict = {x: letters_dict[x] for x in sorted(letters_dict)}
    return letters_dict


print(thesaurus_adv('Иван Сергеев', 'Инна Серова', 'Петр Алексее', 'Илья Иванов', 'Анна Савельева'))
