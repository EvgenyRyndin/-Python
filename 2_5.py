#A
price_list = [74.61, 25.15, 47.56, 36.24, 96.45, 36.74, 46.85, 62.23, 31.98, 87.25]
for price in price_list:
    rub = int(price)
    kk = (price - int(price)) * 100
    print(f'{rub} руб {kk:02.0f} коп', end=', ')
#B
price_list = [74.61, 25.15, 47.56, 36.24, 96.45, 36.74, 46.85, 62.23, 31.98, 87.25]
print(id(price_list))
price_list.sort()
print(id(price_list))
for price in price_list:
    rub = int(price)
    kk = (price - int(price)) * 100
    print(f'{rub} руб {kk:02.0f} коп', end=', ')
#C
price_list = [74.61, 25.15, 47.56, 36.24, 96.45, 36.74, 46.85, 62.23, 31.98, 87.25]
print(id(price_list))
price_list.sort()
price_list.reverse()
print(id(price_list))
for price in price_list:
    rub = int(price)
    kk = (price - int(price)) * 100
    print(f'{rub} руб {kk:02.0f} коп', end=', ')
#D
price_list = [74.61, 25.15, 47.56, 36.24, 96.45, 36.74, 46.85, 62.23, 31.98, 87.25]
for price in sorted(price_list)[::-1][:5]:
    rub = int(price)
    kk = (price - int(price)) * 100
    print(f'{rub} руб {kk:02.0f} коп', end=', ')
