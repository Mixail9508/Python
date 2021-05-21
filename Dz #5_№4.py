from time import perf_counter
import sys

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
start = perf_counter()

# Вариант №1. Это вариант решения из представленных мной будет самым быстрым по написанию,
# и по скорости в отличии от варианта № 2 и №3, но по объему памяти больше чем №3.

# [12, 44, 4, 10, 78, 123]- ответ
# 4.799999999999249e-06 - самая лучшая его скорость
# 120- байт занимает по обЪему памяти

speed_result = [src[number] for number in range(1, len(src)) if src[number] > src[number - 1]]
print(speed_result, perf_counter() - start, sys.getsizeof(speed_result))

# Вариант №2. Это вариант решения из представленных мной является медленее чем вариант №1,
# и по объему памяти равен варианту №1.

# [12, 44, 4, 10, 78, 123]- ответ
# 5.3999999999991555e-06 - самая лучшая его скорость
# 120- байт занимает по обЪему памяти

average_result = []
for number in range(1, len(src)):
    if src[number] > src[number - 1]:
        average_result.append(src[number])
print(average_result, perf_counter() - start, sys.getsizeof(average_result))

# Вариант №3. будет медленнее обоих предидущих вариантов по скорости,
# но легче всех по обЪему памяти.

# 12 44 4 10 78 123- ответ
# 5.500000000002031e-06 - самая лучшая его скорость
# 112- байт занимает по обЪему памяти

good_memory_capacity = (src[number] for number in range(1, len(src)) if src[number] > src[number - 1])
print(*good_memory_capacity, perf_counter() - start, sys.getsizeof(good_memory_capacity))


