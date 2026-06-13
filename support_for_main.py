def get_choice(max_value):
    while True:
        try:
            choice = int(input("Ваш выбор"))
        except ValueError:
            print("Выберите только из предложенных вариантов")
            continue
        if choice > max_value or choice < 1:
            print("Выберите только из предложенных вариантов")
            continue
        return choice