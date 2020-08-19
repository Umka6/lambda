g = [1, 2, 3, 5, -2, -1, -4]
h = list(filter(lambda b: b < 0, g))
b = sum(h)
print(h,'\nсумма отрицательных чисел:',b, '\nабсолютное значение',abs(b))