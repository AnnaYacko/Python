### 3.Склонение слова
#   Реализовать склонение слова «процент» во фразе «N процентов».
#   Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:

percent = 1
while percent < 101:
    if percent > 4 and percent < 20:
        print(percent, "процентов")
    elif percent % 10 == 1:
        print(percent, "процент")
    elif percent % 10 == 2 or percent % 10 == 3 or percent % 10 == 4:
        print(percent, "процента")
    else:
        print(percent, "процентов")
    percent += 1