import random
import time

secret_number = random.randint(1, 100)

start_time = time.time()

attempts = 0
print(" Я загадал число от 1 до 100. Попробуйте его угадать!")

while True:
    try:
        user_guess = int(input(" Введите ваше предположение: "))
        attempts += 1

        if user_guess < secret_number:
            print("🔼 Больше")
        elif user_guess > secret_number:
            print("🔽 Меньше")
        else:
            print(f" Поздравляю! Вы угадали число {secret_number} за {attempts} попыток.")
            break
    except ValueError:
        print(" Пожалуйста, введите целое число!")
end_time = time.time()
elapsed_time = end_time - start_time
print(f" Вы потратили {elapsed_time:.2f} секунд на игру.")

with open("results.txt", "a", encoding="utf-8") as file:
    file.write(f"Число: {secret_number}, Попытки: {attempts}, Время: {elapsed_time:.2f} секунд\n")
