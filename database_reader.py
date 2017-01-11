#database_reader.py

def read():
    with open('fake_database.csv') as file:
        option_value = []
        for item in file.readlines():
            new_item = item.split(';')
            option_value.append(new_item)
    
    return option_value


def value_list():
    opt_val = read()
    res_lst = [int(item[1]) for item in opt_val]
    
    return res_lst

if __name__ == '__main__':
    read()
    print(value_list())