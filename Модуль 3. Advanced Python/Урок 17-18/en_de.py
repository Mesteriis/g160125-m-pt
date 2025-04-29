import requests


def get_translation(word, source_lang, target_lang):
    url = "https://api.mymemory.translated.net/get"
    params = {"q": word, "langpair": f"{source_lang}|{target_lang}"}
    response = requests.get(url, params=params).json()
    return response.get("responseData", {}).get("translatedText", "")


def generate_options(correct_translation, target_lang, word_list):
    options = [correct_translation]
    index = 0
    while len(options) < 4 and index < len(word_list):
        random_word = get_translation(word_list[index], "en", target_lang)
        if random_word and random_word not in options:
            options.append(random_word)
        index += 1
    return options


def play_game(source_lang, target_lang):
    score = 0
    for index, word in enumerate(word_list[:5]):
        correct_translation = get_translation(word, source_lang, target_lang)
        options = generate_options(correct_translation, target_lang, word_list)

        print(f"Переведите слово: {word}")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

        try:
            user_choice = int(input("Выберите номер ответа: "))
            if options[user_choice - 1] == correct_translation:
                print("Правильно!\n")
                score += 1
            else:
                print(f"Неправильно! Верный ответ: {correct_translation}\n")
        except (ValueError, IndexError):
            print("Некорректный ввод. Ответ не засчитан.\n")

    print(f"Игра окончена! Ваш счет: {score}/5")


if __name__ == "__main__":
    word_list = ["apple", "banana", "cherry", "dog", "cat", "house", "car", "tree", "sun", "moon"]
    play_game("en", "de")
