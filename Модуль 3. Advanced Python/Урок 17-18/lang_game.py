import requests
import random
import logging


logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
file_handler = logging.FileHandler(f"{'user_actions}.log", mode='w')

formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s - %(asctime)s", datefmt="%Y-%m-%d %H:%M:%S")

handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(handler)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

API_URL = "https://api.mymemory.translated.net/get"

class Translator:

    def __init__(self, logger):
        self.api = API_URL
        self.logger = logger
    def api_check(self):
        try:
            response = requests.get(self.api, timeout=3)
            print(f'api доступен')
        except requests.Timeout:
            print("Timeout error!")
            self.logger.error("Timeout error!")
        except requests.ConnectionError:
            print("Connection error")
            self.logger.error("Connection error!")

    def get_translation(self, word):
        params = {"q": word, "langpair": "ru|en"}
        response = requests.get(self.api, params=params).json()

        translations = [match["translation"] for match in response.get("matches", []) if match["translation"]]
        return list(set(translations)) if translations else []

class LanguageGame:

    def __init__(self, logger):
        self.translator = Translator(logger)
        self.words_list = ["стол", "дверь", "автомобиль", "овощ", "карта", "механизм"]
        self.counter = 0
        self.tryes = 0
        self.logger = logger


    def random_word(self, count = 3):
        random_words = ["apple", "table", "chair", "bottle", "window", "book", "computer", "car", "street", "house"]
        result = random.sample(random_words, min(count, len(random_words)))
        result = list(map(str.lower, result))
        return result

    def play(self):
        while True:
            any_word = random.choice(self.words_list)
            translated_word = self.translator.get_translation(any_word)
            correct_answer = translated_word[0].lower()
            mix_answers = self.random_word() + [correct_answer]
            random.shuffle(mix_answers)
            print(f"Ваше слово '{any_word}', выберите правильный вариант: {mix_answers}")
            try:
                user_choice = input("Введите ваш выбор: ")
                if user_choice == correct_answer:
                    self.counter += 1
                    print("Ответ верный!")
                else:
                    print(f"Ответ не верный! Правильный ответ - {correct_answer}")
                    self.tryes += 1
            except ValueError:
                print("Неверный ввод!")
                self.logger.warning("Неверный ввод!")
            except KeyboardInterrupt:
                print("Пока пока!")
                self.logger.info("Пользователь отменил ввод")
                break

            self.result_counter()

    def result_counter(self):
        if self.counter == 5:
            print("Вы победили! Игра окончена")
            exit(0)
        if self.tryes == 3:
            print("Вы проиграли! Игра окончена")
            exit(0)


def main():
    translator = Translator(logger)
    game = LanguageGame(logger)

    print(translator.api_check())

if __name__ == '__main__':
    game = LanguageGame(logger)
    game.play()
