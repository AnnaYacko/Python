### 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
duration = int(input("Введите число: "))
if duration < 60:
    print(str(duration), "сек")
elif duration < 60 * 60:
    print(str(duration // 60), "мин", str(duration % 60), "сек")
elif duration < 60 * 60 * 24:
    print(str(duration // (60 * 60)), "час", str(duration % (60 * 60) // 60), "мин", str(duration % 60), "сек")
else:
    print(str(duration // (60 * 60 * 24)), "дн", str(duration % (60 * 60 * 24) // (60 * 60)), "час", str(duration % (60 * 60 * 24) % (60 * 60) // 60), "мин", str(duration % 60), "сек")


