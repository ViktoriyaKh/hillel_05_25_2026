while True:
    word = input("Введи слово з літерою 'h': ")

    if "h" in word.lower():
        print("Введено правильне слово:", word)
        break
    else:
        print("Немає літери 'h', спробуй ще раз")
