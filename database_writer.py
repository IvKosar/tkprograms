# database_writer.py
# writes data to fake database

import database_reader

def writer(result_values):
    opt_val = database_reader.read()
    options = [item[0] for item in opt_val]
            
    result = ''
    with open('fake_database.csv', 'w') as file:
        for item in zip(options, result_values):
            result += item[0] + ';' + str(item[1]) + '\n'
        result = result[:-1]
            
        file.write(result)
        
if __name__ == '__main__': writer([1,0])
   