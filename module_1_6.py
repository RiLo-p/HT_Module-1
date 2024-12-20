my_dict={'owl':1, 'cat':2, 'toad':3}
print(my_dict)
print(my_dict['owl'])
my_dict['rat']=4
print(my_dict['rat'])
my_dict.update({'hippogriff':5, 'phoenix':6})
del my_dict['rat']
print(my_dict)

my_set={1, 2, 'cat', 2, False, 'cat'}
print(my_set)
my_set.update({5, 'owl'})
my_set.remove(1)
print(my_set)

