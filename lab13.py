class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = None

    def square(self):
        pass

    def perimeter(self):
        pass

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def fill(self, color):
        self.color = color

    def compare(self, other):
        return self.square() - other.square()

    def is_intersect(self, other):
        pass

    def is_include(self, other):
        pass

class C1(Shape):
    def __init__(self, x, y, side1, side2, side3, side4):
        super().__init__(x, y)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.side4 = side4

    def square(self):
        return self.side1 * self.side2

    def perimeter(self):
        return 2 * (self.side1 + self.side2)

    def is_intersect(self, other):
        # Проверяем пересечение с другой фигурой other
        if isinstance(other, C1):
            x1, y1 = self.x, self.y
            x2, y2 = other.x, other.y

            if (
                (x1 < x2 + other.side1) and
                (x1 + self.side1 > x2) and
                (y1 < y2 + other.side2) and
                (y1 + self.side2 > y2)
            ):
                return True
        elif isinstance(other, Shape):
            # Если other - объект другого класса Shape
            # Для простоты считаем, что пересечения нет
            return False

    def is_include(self, other):
        pass

class C2(Shape):
    def __init__(self, x, y, side):
        super().__init__(x, y)
        self.side = side

    def square(self):
        return (self.side ** 2) * 0.5

    def perimeter(self):
        return 4 * self.side

    def is_intersect(self, other):
        distance = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        return distance < (self.side / 2 + other.side / 2)

    def is_include(self, other):
        pass

class C3(Shape):
    def __init__(self, x, y, side):
        super().__init__(x, y)
        self.side = side

    def square(self):
        return (self.side ** 2) * (5 * (5 + 2 * 5 ** 0.5)) ** 0.5 / 4

    def perimeter(self):
        return 5 * self.side

    def is_intersect(self, other):
        distance = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        return distance < (self.side / 2 + other.side / 2)

    def is_include(self, other):
        pass

# Создаем объекты C2 (ромб) и C3 (правильный пятиугольник) с координатами и размерами, чтобы они пересекались
c2 = C2(0, 0, 4)  # Ромб C2 с центром в (0, 0) и стороной 4
c3 = C3(2, 2, 4)  # Правильный пятиугольник C3 с центром в (2, 2) и стороной 4

# Создаем объект C1 (четырехугольник)
c1 = C1(1, 1, 3, 3, 3, 3)  # Четырехугольник C1 с центром в (1, 1) и сторонами 3, 3, 3, 3

# Создаем список объектов фигур
shapes = [c1, c2, c3]

# Проверяем сравнение фигур по площади
for i in range(len(shapes)):
    for j in range(i + 1, len(shapes)):
        area_diff = shapes[i].compare(shapes[j])
        if area_diff > 0:
            print(f"{shapes[i].__class__.__name__} больше по площади, чем {shapes[j].__class__.__name__}")
        elif area_diff < 0:
            print(f"{shapes[i].__class__.__name__} меньше по площади, чем {shapes[j].__class__.__name__}")
        else:
            print(f"{shapes[i].__class__.__name__} имеет равную площадь с {shapes[j].__class__.__name__}")

# Проверяем факт пересечения фигур
for i in range(len(shapes)):
    for j in range(i + 1, len(shapes)):
        if shapes[i].is_intersect(shapes[j]):
            print(f"{shapes[i].__class__.__name__} пересекается с {shapes[j].__class__.__name__}")
        else:
            print(f"{shapes[i].__class__.__name__} не пересекается с {shapes[j].__class__.__name__}")

