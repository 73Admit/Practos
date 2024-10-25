def welcome():
    print("Добро пожаловать в игру!")
    print("Вам предстоит пройти пять уровней и решить логические задачи.\n")

def level_one(inventory):
    print("Уровень 1: Вы находитесь в темной комнате.")
    print("На полу лежит ключ. Также есть дверь.")
    
    while True:
        action = input("Что вы хотите сделать? (взять ключ/открыть дверь): ").strip().lower()
        if action == "взять ключ":
            inventory.append("ключ")
            print("Вы взяли ключ.")
            continue
        elif action == "открыть дверь":
            if "ключ" in inventory:
                print("Вы открыли дверь и прошли дальше.")
                return True
            else:
                print("Дверь закрыта. Вам нужен ключ.")
        else:
            print("Неизвестная команда.")

def level_two(inventory):
    print("\nУровень 2: Вы оказались в саду с тремя деревьями.")
    print("На одном из деревьев висит загадка: 'Что приходит, но никогда не приходит?'")
    
    while True:
        answer = input("Введите ваш ответ: ").strip().lower()
        if answer == "завтра":
            print("Правильно! Вы нашли сундук с сокровищами.")
            inventory.append("сундук")
            return True
        else:
            print("Неправильный ответ. Попробуйте снова.")

def level_three(inventory):
    print("\nУровень 3: Вы находитесь перед врагом.")
    print("У вас есть: ", inventory)
    
    while True:
        action = input("Выберите действие (атаковать/убежать): ").strip().lower()
        if action == "атаковать":
            if "сундук" in inventory:
                print("Вы победили врага, используя сокровища из сундука!")
                return True
            else:
                print("У вас нет оружия, вы проиграли.")
        elif action == "убежать":
            print("Вы убегаете от врага.")
            return False
        else:
            print("Неизвестная команда.")

def level_four(inventory):
    print("\nУровень 4: Вы перед загадочной дверью.")
    print("На двери есть замок, который требует код из трех цифр.")

    attempts = 3
    
    while attempts > 0:
        user_code = input("Введите код (например 123): ")
        if user_code == "123":
            print("Код верный! Вы открыли дверь и прошли дальше.")
            return True
        else:
            attempts -= 1
            print(f"Неправильный код. Осталось попыток: {attempts}.")
    
    print("Вы исчерпали все попытки. Игра окончена.")
    return False

def level_five(inventory):
    print("\nУровень 5: Вы оказались в библиотеке с множеством книг.")
    print("На полках стоят 5 книг, но только одна содержит ключ.")
    
    books = ["Книга о драконах", "Книга заклинаний", "Книга о подземельях", "Книга о ведьмах", "Божественная книга"]
    
    print("Доступные книги:")
    for idx, book in enumerate(books, 1):
        print(f"{idx}. {book}")
    
    choice = input("Выберите номер книги для проверки: ")
    
    if choice.isdigit() and 1 <= int(choice) <= len(books):
        chosen_book = books[int(choice) - 1]
        if chosen_book == "Божественная книга":
            print("Вы нашли ключ внутри книги! Теперь можете открыть следующую дверь.")
            inventory.append("ключ_от_библиотеки")
            return True
        else:
            print("Эта книга не содержит ключа.")
            return False
    else:
        print("Некорректный выбор.")
        return False

def main():
    welcome()
    inventory = []
    
    # Уровень 1
    level_completed = False
    while not level_completed:
        level_completed = level_one(inventory)
    
    # Уровень 2
    level_completed = False
    while not level_completed:
        level_completed = level_two(inventory)
    
    # Уровень 3
    level_completed = False
    while not level_completed:
        level_completed = level_three(inventory)
    
    # Уровень 4
    level_completed = False
    while not level_completed:
        level_completed = level_four(inventory)
    
    if level_completed:
        # Уровень 5
        level_completed = False
        while not level_completed:
            level_completed = level_five(inventory)

    print("\nПоздравляем! Вы прошли игру!")

if __name__ == "__main__":
    main()