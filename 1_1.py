duration = int(input('Введите секунды: '))
if duration < 60:
    print(duration, 'сек')
elif duration >= 60 and duration < 3600:
    duration_min = duration // 60
    duration_sec = duration % 60
    print(duration_min, 'мин', duration_sec, 'сек')
elif duration >= 3600 and duration < 86400:
    duration_hour = duration // 3600
    duration_min = duration % 3600 // 60
    duration_sec = duration % 60
    print(duration_hour, 'час', duration_min, 'мин', duration_sec, 'сек')
elif duration >= 86400:
    duration_days = duration // 86400
    duration_hour = duration // 3600 % 24
    duration_min = duration % 3600 // 60
    duration_sec = duration % 60
    print(duration_days, 'дней', duration_hour, 'час', duration_min, 'мин', duration_sec, 'сек')