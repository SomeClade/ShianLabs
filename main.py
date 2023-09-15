degrees = float(input("Введите градусы часов (не более 360): "))
hours = int(degrees // 30)
degrees %= 30
minutes = int(degrees * 2)
degrees %= (1 / 30) * 60 * 60
print(f"Часы: {hours}")
print(f"Минуты: {minutes}")
print(f"Секунды: {degrees:.2f}")
