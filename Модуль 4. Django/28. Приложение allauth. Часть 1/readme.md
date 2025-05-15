## Урок 28

1. **Добавлена поддержка переменных окружения**:
   - Теперь конфиденциальные данные (`SECRET_KEY`, настройки почты, данные БД) хранятся в `.env`, а не в коде.
   - Используется библиотека `python-dotenv` для загрузки переменных окружения в `settings.py`.
   - Это улучшает безопасность и упрощает деплой на разных средах.

2. **Обновлены настройки PostgreSQL**:
   - Убраны фиксированные значения настройки БД, теперь используются переменные окружения (`PG_NAME`, `PG_USER`, `PG_PASSWORD`, `PG_HOST`, `PG_PORT`).
   - Это делает конфигурацию более гибкой и удобной для работы с разными базами данных.

3. **Оптимизированы настройки Django**:
   - `DEBUG` теперь корректно интерпретируется как `bool`, исключая возможные ошибки (`DEBUG = os.getenv('DEBUG', 'False').lower() in ('true', '1')`).
   - `SECRET_KEY` загружается из `.env`, убирая его из репозитория.

4. **Обновлены зависимости в `requirements.txt`**:
   - Добавлена библиотека: `python-dotenv`.

**commit: `Урок 28: улучшена конфигурация через .env, обновлены зависимости и настройки PostgreSQL`**

#### 1. Добавление `django-allauth` в `INSTALLED_APPS`
`django-allauth` — это мощное приложение для `Django`, которое предоставляет гибкую систему аутентификации и регистрации пользователей. Оно поддерживает как локальную аутентификацию (по email и паролю), так и аутентификацию через социальные сети (например, Google, Facebook).
```python
INSTALLED_APPS = [
    ...
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    ...
]
```

#### 2. Добавление `allauth.account.middleware.AccountMiddleware` в `MIDDLEWARE`
`MIDDLEWARE` в `Django` — это набор классов, которые обрабатывают запросы и ответы. `Middleware` может выполнять различные задачи, такие как аутентификация, обработка сессий, логирование и т.д.
Добавление `allauth.account.middleware.AccountMiddleware` необходимо для корректной работы `django-allauth`. Это `middleware` обеспечивает правильную обработку сессий пользователей и других аспектов аутентификации.
```python
MIDDLEWARE = [
    ...
    'allauth.account.middleware.AccountMiddleware',  # Добавьте эту строку
]
```

#### 3. Настройка `SITE_ID`
`SITE_ID` используется для идентификации сайта в системе `Django Sites Framework`. Это необходимо для работы `django-allauth`, так как оно использует эту информацию для управления сайтами.
```python
SITE_ID = 1
```

#### 4. Настройка `AUTHENTICATION_BACKENDS`
`AUTHENTICATION_BACKENDS` определяет, какие бэкенды аутентификации использовать. В данном случае мы используем стандартный бэкенд `Django` (`ModelBackend`) и бэкенд `django-allauth` (`allauth.account.auth_backends.AuthenticationBackend`).
```python
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)
```

#### 5. Настройка параметров аутентификации
Эти настройки определяют, как `django-allauth` будет обрабатывать аутентификацию пользователей:
- `ACCOUNT_EMAIL_REQUIRED = True`: Требует указания `email` при регистрации.
- `ACCOUNT_EMAIL_VERIFICATION = "mandatory"`: Требует обязательного подтверждения `email`.
- `ACCOUNT_AUTHENTICATION_METHOD = "email"`: Использует `email` в качестве основного метода аутентификации.
- `ACCOUNT_USERNAME_REQUIRED = False`: Не требует указания имени пользователя при регистрации.
- `ACCOUNT_USER_MODEL_USERNAME_FIELD = None`: Указывает, что поле имени пользователя не используется.
```python
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
```

#### 6. Настройка кастомной формы регистрации
Мы создали кастомную форму регистрации, чтобы включить дополнительные поля (имя и фамилия). Эта настройка указывает `Django` использовать нашу кастомную форму вместо стандартной.
```python
ACCOUNT_FORMS = {
    'signup': 'users.forms.CustomSignupForm',
}
```

#### 7. Создание и применение миграций
Миграции необходимы для создания таблиц в базе данных, которые используются `django-allauth`.
Даже если вы не вносили изменений в модели данных, добавление нового приложения может требовать создания новых таблиц.

```sh
python manage.py makemigrations
python manage.py migrate
```

Теперь в наше приложение настроено для использования `django-allauth` с кастомными шаблонами и формой регистрации.
Пользователи смогут зарегистрироваться, подтвердить свой `email` и авторизоваться с помощью `email` и пароля.

**commit: `Урок 28: добавили регистрацию через email`**

1. **Добавлено логирование (комментированное, но готово к использованию)**
   - Теперь можно включить детализированное логирование запросов Django и библиотеки allauth.
   - Это поможет в отладке процессов аутентификации и в общем мониторинге работы приложения.

2. **Настроена аутентификация через Django allauth**
   - Изменены настройки `ACCOUNT_*` для улучшенной работы email-верификации:
     - `ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3`: подтверждение email теперь действительно 3 дня.
     - `ACCOUNT_EMAIL_CONFIRMATION_HMAC = True`: дополнительная защита подтверждения email через HMAC.
     - `ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True`: автоматический вход после подтверждения email.
   - Теперь email используется в качестве `username`.

3. **Обновлена система сессий**
   - `SESSION_ENGINE = 'django.contrib.sessions.backends.db'`: сессии теперь хранятся в базе данных.
   - `SESSION_COOKIE_AGE = 1209600` (2 недели) для удобства пользователей.
   - `SESSION_SAVE_EVERY_REQUEST = True`: продлевает сессию пользователя при каждом запросе.

4. **Рефакторинг форм и вьюх пользователей**
   - Убран `RegisterUserForm`, теперь `CustomSignupForm` оформлен с Bootstrap 5.
   - В `CustomSignupForm` добавлены классы `form-control` для стилизации полей.
   - Добавлен `CustomConfirmEmailView`, который редиректит подтвержденных пользователей сразу на страницу входа.

5. **Оптимизированы шаблоны**
   - Убран `col-md-6` → заменен на `col-md-8` в форме регистрации.
   - В `signup.html` добавлен скрытый `next` для редиректа после успешного входа.

6. **Обновлены URL и представления**
   - `RegisterUser` удален, вместо него теперь используется встроенный allauth `account_signup`.
   - `LoginUser` заменен на allauth `account_login`.
   - `LogoutUser` теперь редиректит на `account_login`.

7. **Добавлены сигналы для автоматической верификации email**
   - `signals.py` теперь содержит `update_verified_status`, который обновляет статус email после подтверждения.

**commit: `Урок 28: дополнительные настройки allauth`**