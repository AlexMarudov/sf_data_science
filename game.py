"""game guess the number"""

import numpy as np

number = np.random.randint(1, 101) # загадаем число

count = 0

while True:
    count+=1
    predict_number = int(input("Угадайте число от 1 до 100: "))
    
    if predict_number > number:
        print("Число меньше!")
        print(number)
        
    elif predict_number < number:
        print("Число больше!")
    else:
        print(f"Вы угадали число! Это число = {number}, за {count} попыток")
        break
        