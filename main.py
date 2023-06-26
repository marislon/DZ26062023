# 4.137 Даны целое число k (1 k 180) и последовательность цифр 10111213...9899,
# в которой выписаны подряд все двузначные числа. Определить k-ю цифру.

# def find_kth_digit(k):
#     s = ''.join(str(i) for i in range(10, 100))
#     return int(s[k-1])
#
# k = int(input())
# print(find_kth_digit(k))

# 5.62 Известны оценки по физике каждого ученика двух классов. Определить
# среднюю оценку в каждом классе. Количество учащихся в каждом классе одинаковое

# import random
# # оценки учеников первого класса
# class1_grades = [random.randint(1, 5) for _ in range(30)]
# print(class1_grades)
# # оценки учеников второго класса
# class2_grades = [random.randint(1, 5) for _ in range(30)]
# print(class2_grades)
# import statistics
# # средняя оценка в первом классе
# class1_average = statistics.mean(class1_grades)
# print(f'Средняя оценка в первом классе: {class1_average}')
#
# # средняя оценка во втором классе
# class2_average = statistics.mean(class2_grades)
# print(f'Средняя оценка во втором классе: {class2_average}')

# 2.43 Даны два целых числа a и b. Если a делится на b или b делится на a, то вывести 1, иначе — любое другое число.
# Условные операторы и операторы цикла не использовать.

# def check_division(a, b):
#     return 1 if a % b == 0 or b % a == 0 else 0
#
# import random
# a = random.randint(1,10)
# b = random.randint(1,10)
# print(a)
# print(b)
# print(check_division(a, b))
# print(check_division(b, a))

# 17.7 Известны стоимости 12 марок телевизоров (все значения разные).
# Определить стоимость телевизора, являющегося "пятым из самых дешевых моделей".

# import random
# tv_prices = [random.randint(100, 1000) for _ in range(12)]
# print(tv_prices)
# # Сортируем список в порядке возрастания
# sorted_prices = sorted(tv_prices)
# print(sorted_prices)
# # Выводим стоимость пятого телевизора среди самых дешевых
# print(sorted_prices[4])

# 6.97 Известно количество очков, набранных каждой из 20-ти команд-участниц
# первенства по футболу. Перечень очков дан в порядке убывания (ни одна пара
# команд не набрала одинаковое количество очков). Определить, какое место
# заняла команда, набравшая N очков (естественно, что значение N имеется
# в перечне). Условный оператор не использовать.

# def find_team_position(scores, team_score):
#     return scores.index(team_score) + 1
# import random
# scores = [random.randint(1, 100) for _ in range(20)]
# print(scores)
# team_score = random.choice(scores)
# print(team_score)
# sorted_scores = sorted(scores, reverse=True)
# print(sorted_scores)
# print(find_team_position(sorted_scores, team_score))