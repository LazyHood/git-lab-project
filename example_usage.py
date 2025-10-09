# Пример использования библиотеки PostgreSQL

from database_manager import DatabaseManager

# Создание экземпляра менеджера БД
db = DatabaseManager('postgres_config.ini')

# Подключение к базе данных
db.connect()

# Примеры SQL запросов
queries = [
    'CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name VARCHAR(100));',
    'INSERT INTO users (name) VALUES (\\'Alice\\');',
    'SELECT * FROM users;'
]

# Выполнение запросов
for query in queries:
    db.execute_query(query)

print('\\nВсе операции выполнены успешно!')
"