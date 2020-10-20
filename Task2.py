# Задание начальных условий задачи
a = [
    {'x': 1, 'y': 1},
    {'x': 1, 'y': -1},
    {'x': -1, 'y': -2}
]


def count_of_circles(array_points):
    """
    Функция нахождения количества окружностей с центром в точке O(0, 0) на которых лежат все заданные точки.

    Основная формула нахождения точки на окружности с центром в точке О(0, 0):
    x^2 + y^2 <= R^2

    :param array_points: массив с координатами точек
    :return: количество окружностей
    """
    # Задаем словарь для расчета количества окружностей, с ключем - R (радиус окружности) и значением - (x, y)
    circles = {}

    for coordinate in array_points:
        x = coordinate["x"]
        y = coordinate["y"]

        # Функция pow в python - предназначена для возведения в степень x^y, pow(x, y)
        r = pow(x, 2) + pow(y, 2)
        # Создаем пару ключ - радиус, значение - координаты точки (x, y) и в случае если ключ уже существует, добавляем в массив к существующим координатам
        circles.setdefault(r, []).append(coordinate)

    return len(circles)


# Выводим количество возможных окружностей с радиусами R
result = count_of_circles(a)
print(result)
