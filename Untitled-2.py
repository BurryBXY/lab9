
import logging
import random

logging.basicConfig(filename="ex.log", level=logging.INFO)

def play_game(n: int, k: int):
    # Загадываем число от 1 до N
    logging.info("Programm started")
    target = random.randint(1, n)
    # Цикл для каждой попытки
    for i in range(k):
        # Просим пользователя ввести число
        guess = int(input("Введите число от 1 до {}: ".format(n)))
        # Проверяем число
        if guess == target:
            logging.info("the player guessed the number {}".format(target))
            print("Вы угадали!")
            return
        elif guess < target:
            logging.info("The player called the number {} (less than a mystery)".format(guess))
            print("Загаданное число больше")
        else:
            logging.info("The player called the number {} ((more than a mystery))".format(guess))
            print("Загаданное число меньше")
    # Попытки закончились
    logging.warning("Attempts are over")
    print("Попытки закончились")

# Просим пользователя ввести N и k
n = int(input("Введите верхнюю границу диапазона (N): "))
k = int(input("Введите количество попыток (k): "))
# Начинаем игру
play_game(n, k)
