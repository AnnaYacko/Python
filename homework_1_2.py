### 2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
#      Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
#      Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
#      К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
#      сумма цифр которых делится нацело на 7.

cube = []
result1 = 0
result2 = 0
for i in range(0, 1001):
    if i % 2 != 0:
        cube.append(i ** 3)
for index in range(len(cube)):
    sum = 0
    number = cube[index]
    while number:
        sum += number % 10
        number = number // 10
    if sum % 7 == 0:
        result1 += cube[index]

    cube[index] += 17
    sum = 0
    number = cube[index]
    while number:
        sum += number % 10
        number = number // 10
    if sum % 7 == 0:
        result2 += cube[index]
print(result1, result2)
