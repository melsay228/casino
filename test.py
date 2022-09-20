import random

user_money = 100
casino_money = 100

while user_money and casino_money:
    print("У игрока", user_money, "монет")
    print("у казино", casino_money, "монет")

    input("Нажмите ENTER чтобы сдеать ход")

    user_turn = random.randint(1, 6)
    casino_turn = random.randint(1, 6)

    print("Игрок выбросил", user_turn)
    print("Казино выбросил", casino_turn)

    if casino_turn > user_turn:
        print("Казино победило")
        user_money -= 1
        casino_money += 1
    elif user_turn > casino_turn:
        print("Игрок победил")
        user_money += 1
        casino_money -= 1
    else:
        print("Ничья")

if casino_money == 0:
    print("Конец. У казино кончились деньги")
else:
    print("Конец. У игрока кончились деньги")
