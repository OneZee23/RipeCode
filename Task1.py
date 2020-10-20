# Задание начальных условий задачи
a = [1, -2, 5, 6, 10, 5, 1]
n = 7
m = 2

a_2 = [5, 1, 3, 6, 8, -2, 8, -1, 1, 18]
n_2 = 10
m_2 = 3


def largest_sum_of_a_subsequence(sequence, length, length_sub):
    """
    Функция нахождения наибольшей суммы подпоследовательности

    :param sequence: начальная последовательность
    :param length: длина последовательности
    :param length_sub: длина подпоследовательности
    :return: наибольшая сумма подпоследовательности
    """
    # Задаем начальную максимальную сумму равную нулю
    max_amount = 0

    # Проходимся по каждому элементу массива и находим максимальную сумму подпоследовательности длины m в массиве a
    for i in range(length - length_sub + 1):
        cur_amount = 0

        # Суммируем все впередистоящие значения подпоследовательности с текущей суммой
        for j in range(length_sub):
            cur_amount = cur_amount + sequence[i + j]

        # Проверяем текующую сумму подпоследовательности длины m с максимальной суммой
        if cur_amount > max_amount:
            max_amount = cur_amount

    return max_amount


# Выводим результат
result = largest_sum_of_a_subsequence(a, n, m)
print(result)
result_2 = largest_sum_of_a_subsequence(a_2, n_2, m_2)
print(result_2)
