s = input("Введите строку: ")
n = len(s)
half_n = n // 2
result = s[:half_n].replace('п', '*') + s[half_n:]
print("Результат:", result)
