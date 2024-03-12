from constant_time_item_in_list_check import special_list

ls = special_list()

ls.append(3)
ls.append(31)
ls.append(27)
test = 27

print()
print(ls.internal_list)
print(f'{test} in ls = {test in ls}')
print()

