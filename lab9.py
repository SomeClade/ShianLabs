'''Задание 3 Шахматная доска.
Даны два числа n и m Создайте двумерный массив размером n×m и
заполните его символами «.» и «*» в шахматном порядке. В левом верхнем
углу должна стоять точка.'''

n = int(input("Введите количество строк (n): "))
m = int(input("Введите количество столбцов (m): "))
chessboard = []
for i in range(n):
    row = []  # Создаем пустую строку
    for j in range(m): # заполнение
        if (i + j) % 2 == 0:
            row.append('.')
        else:
            row.append('*')
    chessboard.append(row)
for row in chessboard:
    print(' '.join(row))
