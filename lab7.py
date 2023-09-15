'''
Дан список. Выведите те его элементы, которые встречаются в списке
только один раз. Элементы нужно выводить в том порядке, в котором они
встречаются в списке.
'''
# Входной список
my_list = [1, 2, 2, 3, 4, 4, 5]
element_count = {}
for item in my_list:
    if item in element_count:
        element_count[item] += 1
    else:
        element_count[item] = 1
result = [item for item, count in element_count.items() if count == 1]
for item in my_list:
    if item in result:
        print(item, end=' ')
