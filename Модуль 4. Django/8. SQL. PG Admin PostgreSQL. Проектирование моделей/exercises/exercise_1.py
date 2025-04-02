# 1. Установить PostgreSQL (не забудьте пароль, который вы придумали)
# 2. Настроить PostgreSQL
# 3. Сделать тестовый запрос с созданием таблиц

# CREATE TABLE users (
#  user_id SERIAL PRIMARY KEY,
#  username VARCHAR(50) NOT NULL,
#  email VARCHAR(100) NOT NULL UNIQUE
# );

# CREATE TABLE orders (
#  order_id SERIAL PRIMARY KEY,
#  user_id INTEGER NOT NULL,
#  order_date DATE NOT NULL,
#  amount DECIMAL(10, 2) NOT NULL,
#  FOREIGN KEY (user_id) REFERENCES users(user_id)
# );
