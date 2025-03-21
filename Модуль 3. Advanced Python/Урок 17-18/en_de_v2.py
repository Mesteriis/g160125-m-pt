import requests
import itertools


class Translator:
    API_URL = "https://api.mymemory.translated.net/get"

    @staticmethod
    def get_translation(word, source_lang, target_lang):
        try:
            params = {"q": word, "langpair": f"{source_lang}|{target_lang}"}
            response = requests.get(Translator.API_URL, params=params).json()
            return response.get("responseData", {}).get("translatedText", "")
        except requests.RequestException:
            return "[Ошибка перевода]"


class LanguageGame:
    def __init__(self, source_lang, target_lang, word_list):
        self.source_lang = source_lang
        self.target_lang = target_lang
        self.word_list = itertools.cycle(word_list)  # Бесконечный цикл по списку слов
        self.score = 0

    def generate_options(self, correct_translation):
        options = [correct_translation]
        used_words = set(options)

        for word in self.word_list:
            if len(options) >= 4:
                break
            translation = Translator.get_translation(word, "en", self.target_lang)
            if translation and translation not in used_words:
                options.append(translation)
                used_words.add(translation)

        return sorted(options, key=lambda x: x)  # Для перемешивания без random

    def play_round(self):
        word = next(self.word_list)  # Берем следующее слово из цикла
        correct_translation = Translator.get_translation(word, self.source_lang, self.target_lang)
        options = self.generate_options(correct_translation)

        print(f"Переведите слово: {word}")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

        try:
            user_choice = int(input("Выберите номер ответа: "))
            if options[user_choice - 1] == correct_translation:
                print("Правильно!\n")
                self.score += 1
            else:
                print(f"Неправильно! Верный ответ: {correct_translation}\n")
        except (ValueError, IndexError):
            print("Некорректный ввод. Ответ не засчитан.\n")

    def play_game(self, rounds=5):
        for _ in range(rounds):
            self.play_round()
        print(f"Игра окончена! Ваш счет: {self.score}/{rounds}")


if __name__ == "__main__":
    word_list = ["apple", "banana", "cherry", "dog", "cat", "house", "car", "tree", "sun", "moon"]
    game = LanguageGame("en", "de", word_list)
    game.play_game()
