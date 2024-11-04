# Получаем шестизначный номер билета от пользователя
n = input("Введите шестизначный номер билета: ")

# Проверяем, что номер состоит из 6 цифр
if len(n) == 6 and n.isdigit():
    # Разбиваем номер на две половины
    first_half = n[:3]
    second_half = n[3:]
    
    # Считаем сумму первых трех и последних трех цифр
    sum_first_half = int(first_half[0]) + int(first_half[1]) + int(first_half[2])
    sum_second_half = int(second_half[0]) + int(second_half[1]) + int(second_half[2])
    
    # Проверяем счастливость билета
    if sum_first_half == sum_second_half:
        print("yes")
    else:
        print("no")
else:
    print("Ошибка: Введите корректный шестизначный номер.")
