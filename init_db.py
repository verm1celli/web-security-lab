
import sqlite3

# Подключаемся к базе данных
connection = sqlite3.connect("database.db")

# Создаём объект для выполнения SQL-запросов
cursor = connection.cursor()

# Создаём таблицу пользователей
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
""")

# Добавляем тестового пользователя
cursor.execute("""
INSERT OR IGNORE INTO users (username, password)
VALUES (?, ?)
""", ("admin", "admin123"))

# Сохраняем изменения
connection.commit()

# Закрываем соединение
connection.close()

print("База данных успешно создана!")
