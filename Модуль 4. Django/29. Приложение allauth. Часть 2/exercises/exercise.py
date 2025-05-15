# 1. перенести все важные и чувствительные настройки в .env

# 2. настроить gmail (или другую почту с которой вы будете посылать письма для подтверждения регистрации)
#    на двухфакторную авторизацию

# 3. Создать пароль-приложение для отправки писем о подтверждении регитстрации

# 4. Настроить в админ-панели sites

# 5. Вписать все необходимые настройки в settings.py

# 6. Создать сигнал, форму, представление и маршруты для отправки почты

# 7. Попробовать зарегистрироваться с помощью почты

# 8. Добавить восстановление через почту

# 9. Конечный список маршрутов — представлений — шаблонов:
#    Регистрация — /accounts/signup/ 
#                — CustomSignupView 
#                — templates/account/signup.html
#    Вход — /accounts/login/ 
#         — CustomLoginView 
#         — templates/account/login.html
#    Подтверждение Email — /accounts/confirm-email/<ключ>/ 
#                        — CustomConfirmEmailView 
#                        — templates/account/confirm_email.html
#    Запрос сброса пароля — /accounts/password/reset/ 
#                         — CustomPasswordResetView 
#                         — templates/account/password_reset.html
#    Ввод нового пароля — /accounts/password/reset/key/<ключ>/ 
#                       — CustomPasswordResetFromKeyView 
#                       — templates/account/password_reset_from_key.html
#    Успешный сброс — /accounts/password/reset/key/done/ 
#                   — templates/account/password_reset_from_key.html 
#                   — templates/account/password_reset_from_key_done.html
