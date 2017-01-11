# raisers.py
# raise given value
import database_reader

a = database_reader.value_list()
last_changed = []
def raise_pidpys():
    a[0] += 1
    last_changed.append(0)
    print(a)
    
def raise_copies():
    a[1] += 1
    last_changed.append(1)
    print(a)