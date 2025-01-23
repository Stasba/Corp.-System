max_streak = 0
current_streak = 0 
prev_number = None

print("Введите последовательность чисел (завершается 0):")

while True:
    num = int(input())
    if num == 0:
        break

    if num == prev_number:
        current_streak += 1
    else:
        current_streak = 1  # Начин

    max_streak = max(max_streak, current_streak)
    prev_number = num

print("Наибольшее число подряд идущих элементов, равных друг другу:", max_streak)
