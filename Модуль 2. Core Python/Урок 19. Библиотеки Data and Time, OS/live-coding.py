import datetime
from icecream import ic as print
# Тема: Модуль datetime
# Покажите в режиме live-coding и объясните как использовать модуль datetime:
# - получать дату и время,
#
# now = datetime.datetime.now()
# print(now)
# print(now.date())
# print(now.time())
#
# # - производить с ними сложения и вычитания,
# past = now - datetime.timedelta(days=10)
# print(past)
# future = now + datetime.timedelta(days=10)
# print(future)
#
# # - конвертировать в строку и обратно.
#
#
#
# str_datetime = "2021/06/11 14:35:45"
#
# date_ojc = datetime.datetime.strptime(str_datetime, "%Y/%m/%d %H:%M:%S")
#
# print(date_ojc.strftime("%d--%m--%Y %H:%M:%S"))
#






# Тема: Модуль os
# Покажите в режиме live-coding и объясните:
# - Как работать с модулем os.
# - Основные команды: getcwd, listdir, mkdir, remove, rmdir, rename.

import os

path = os.getcwd()
print(path)
print(os.listdir(path))
os.mkdir("test")
print(os.listdir(path))
os.rmdir("test")
print(os.listdir(path))
with open("test", "w") as file:
    file.write("test")
os.rename("test", "new_test")
print(os.listdir(path))
