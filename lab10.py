'''Аня и Боря любят играть в разноцветные кубики, причем у каждого из
них свой набор и в каждом наборе все кубики различны по цвету. Однажды
дети заинтересовались, сколько существуют цветов таких, что кубики каждого
цвета присутствуют в обоих наборах. Для этого они занумеровали все цвета
случайными числами от 0 до 108 На этом их энтузиазм иссяк, поэтому вам
предлагается помочь им в оставшейся части.
В первой строке входных данных записаны числа и – число кубиков
у Ани и Бори. В следующих строках заданы номера цветов кубиков Ани. В
последних строках номера цветов Бори.
Найдите три множества: номера цветов кубиков, которые есть в обоих
наборах; номера цветов кубиков, которые есть только у Ани и номера цветов
кубиков, которые есть только у Бори. Для каждого из множеств выведите
сначала количество элементов в нем, а затем сами элементы, отсортированные
по возрастанию.
Входные данные |4 3|0|1|10|9|1|3|0| ответ |2|0 1| 2 | 9 10|1|3|'''

# Считываем количество кубиков у Ани и Бори
ani_cubes, borya_cubes = map(int, input().strip().split())
# Создаем множества для номеров цветов кубиков Ани и Бори
ani_colors = set()
borya_colors = set()
# Считываем номера цветов кубиков Ани
for _ in range(ani_cubes):
    color = int(input().strip())
    ani_colors.add(color)
# Считываем номера цветов кубиков Бори
for _ in range(borya_cubes):
    color = int(input().strip())
    borya_colors.add(color)
# Находим пересечение множеств
common_colors = ani_colors.intersection(borya_colors)
# Находим разницу множеств
ani_only_colors = ani_colors.difference(common_colors)
borya_only_colors = borya_colors.difference(common_colors)
print(len(common_colors))
print(" ".join(map(str, sorted(common_colors))))
print(len(ani_only_colors))
print(" ".join(map(str, sorted(ani_only_colors))))
print(len(borya_only_colors))
print(" ".join(map(str, sorted(borya_only_colors))))
