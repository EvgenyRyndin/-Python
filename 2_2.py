random_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_list = []
for content in random_list:
    if content.isdigit():
        new_list.extend(['"', f'{int(content):02}', '"'])
    elif (content.startswith('+') or content.startswith('-')) and content[1:].isdigit():
        new_list.extend(['"', f'{content[0]}{int(content[1:]):02}', '"'])
    else:
        new_list.append(content)
final_list = ' '.join(new_list)
print(final_list)
