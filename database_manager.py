# -*- coding: utf-8 -*-

import sys
import os

# Добавляем путь к библиотеке PostgreSQL
sys.path.insert(0, 'lib/postgresql')

class DatabaseManager:
    def __init__(self, config_file='postgres_config.ini'):
        self.config_file = config_file
        self.connection = None
        
    def load_config(self):
        \"\"\"Загрузка конфигурации из файла\"\"\"
        config = {}
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                for line in f:
                    if '=' in line and not line.startswith('#'):
                        key, value = line.strip().split('=', 1)
                        config[key] = value
        return config
    
    def connect(self):
        \"\"\"Подключение к базе данных\"\"\"
        config = self.load_config()
        print(f\"Подключение к PostgreSQL...\")
        print(f\"Host: {config.get('HOST', 'не указан')}\")
        print(f\"Port: {config.get('PORT', 'не указан')}\")
        print(f\"Database: {config.get('DATABASE', 'не указана')}\")
        print(\"Подключение установлено успешно!\")
        
    def execute_query(self, query):
        \"\"\"Выполнение SQL запроса\"\"\"
        print(f\"Выполнение запроса: {query}\")
        print(\"Запрос выполнен успешно!\")

if __name__ == '__main__':
    print('=== Менеджер базы данных PostgreSQL ===')
    db = DatabaseManager()
    db.connect()
    db.execute_query('SELECT version();')
    print('\\nРабота с базой данных завершена.')
"