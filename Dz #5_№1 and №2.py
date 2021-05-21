# Задание № 1 и № 2


# с использованием yield
def numbers_generator(num):
    for numbers in range(1, num + 1, 2):
        yield numbers


result = numbers_generator(15)
print(type(result), next(result), next(result),
      next(result), next(result), next(result),
      next(result), next(result), next(result)
      )
# <class 'generator'> 1 3 5 7 9 11 13 15

# и без использования yield, как понял я
numbers_generator_two = (numbers for numbers in range(1, 5 + 1, 2))

print(type(numbers_generator_two), next(numbers_generator_two),
      next(numbers_generator_two), next(numbers_generator_two)
      )
# <class 'generator'> 1 3 5