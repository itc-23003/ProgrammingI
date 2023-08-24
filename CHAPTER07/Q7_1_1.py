name_age = {'Tanaka': 35, 'Satou': 25, 'Suzuki': 27}


def dict_info(dict_tbl, key):
    try:
        return dict_tbl[key]
    except:
        return 'key is not found'


print(dict_info(name_age, 'Satou'))
print(dict_info(name_age, 'Yamada'))
