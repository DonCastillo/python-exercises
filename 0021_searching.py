shopping_list = ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice']

item_to_find = 'spam'
found_at = None     # like null, does have a value


for index in range(len(shopping_list)):  # len is the size of the array
    if shopping_list[index] == item_to_find:
        found_at = index
        break

print('Item found at position {}'.format(found_at))



print('----')


item_to_find = 'albatross'
found_at = None



# for index in range(len(shopping_list)):  # len is the size of the array
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break

if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

if found_at is not None:
    print('Item found at position {}'.format(found_at))
else:
    print('{} not found'.format(item_to_find))