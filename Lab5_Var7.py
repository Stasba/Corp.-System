prev = int(input("Число: "))
count = 0

while prev != 0:
    current = int(input("Число: "))
    if current == 0:
        break
    if current > prev:
        count += 1
        prev = current

print("Кол-во элементов, больших предыдущего:", count)
