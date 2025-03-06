# Создание класса с логированием доступа к атрибутам
# Описание:
#
# Создайте класс LoggedAttributes, который будет вести лог всех операций по установке, получению и
# удалению атрибутов, а также предоставлять значения по умолчанию для отсутствующих атрибутов.
# Все операции должны логироваться в список log.
#
# Требования:
#
# Переопределите метод __setattr__ для логирования установки атрибутов.
# Переопределите метод __getattribute__ для логирования доступа к атрибутам.
# Переопределите метод __getattr__ для логирования и предоставления значения по умолчанию для отсутствующих атрибутов.
# Переопределите метод __delattr__ для логирования удаления атрибутов.
# Шаги:
#
# Создайте класс LoggedAttributes.
# Добавьте список log в качестве атрибута класса для хранения логов операций.
# Реализуйте методы __setattr__, __getattribute__, __getattr__ и __delattr__ с логированием операций.
# Тестируйте класс, создавая экземпляр и выполняя различные операции с атрибутами.

# class LoggedAttributes:
#     log = []  # Общий лог для всех экземпляров (можно сделать и на уровне экземпляра, если нужно)
#
#     def __setattr__(self, name, value):
#         self.__class__.log.append(f"Set attribute '{name}' to '{value}'")
#         super().__setattr__(name, value)
#
#     def __getattribute__(self, name):
#         if name != 'log':  # чтобы избежать рекурсии при доступе к логу
#             self.__class__.log.append(f"Get attribute '{name}'")
#         return super().__getattribute__(name)
#
#     def __getattr__(self, name):
#         self.__class__.log.append(f"Attribute '{name}' not found, returning default value")
#         return None  # значение по умолчанию для отсутствующих атрибутов
#
#     def __delattr__(self, name):
#         self.__class__.log.append(f"Delete attribute '{name}'")
#         super().__delattr__(name)
#
# # Тестирование
# obj = LoggedAttributes()
#
# # Установка атрибутов
# obj.attr1 = 'value1'
# obj.attr2 = 'value2'
#
# # Получение атрибутов
# print(obj.attr1)
# print(obj.attr3)  # отсутствующий атрибут
#
# # Удаление атрибута
# del obj.attr1
#
# # Проверка лога
# for entry in LoggedAttributes.log:
#     print(entry)


class LoggedAttributes:
    def __init__(self):
        super().__setattr__('log',[])

    def __setattr__(self, name,value):
        self.log.append(f"Set attribute {name} {value}")
        super().__setattr__(name,value)

    def __getattribute__(self,name):
        if name == 'log':
            log = super().__getattribute__('log')
            log.append(f"Get attribute {name}")
        return super().__getattribute__(name)

    def __getattr__(self, name):
        self.log.append(f"Get missing attribute")
        return 'default  value'

    def __delattr__(self, name):
        self.log.append(f"Delete attribute")
        super().__delattr__(name)

tnt = LoggedAttributes()
tnt.a = 10
print(tnt.a)
print(tnt.log)