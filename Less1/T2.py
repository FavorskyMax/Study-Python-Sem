# Получаем количество минут от пользователя
n = int(input("Введите количество минут: "))

# Рассчитываем количество часов и оставшиеся минуты
hours = n // 60
minutes = n % 60

# Выводим результат
print("Часов:", hours)
print("Минут:", minutes)