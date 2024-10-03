import json
from pymongo import MongoClient

# Подключаемся к MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['bookstore']  # Создаем базу данных
collection = db['books']   # Создаем коллекцию

# Загрузка данных из файла books.json
with open('books.json', 'r', encoding='utf-8') as file:
    books = json.load(file)

# Вставляем книги в коллекцию
collection.insert_many(books)

print(f'Вставлено {len(books)} книг в коллекцию {collection.name}.')

# Примеры запросов к коллекции
# 1. Получить все документы
all_books = collection.find()
for book in all_books:
    print(book)

# 2. Найти книгу по названию
book_title = "A Light in the Attic"
found_book = collection.find_one({"title": book_title})
print(f'Найдена книга: {found_book}')

# 3. Найти книги с ценой меньше 30
cheap_books = collection.find({"price": {"$lt": "30"}})
print("Книги с ценой меньше 30:")
for book in cheap_books:
    print(book)

# 4. Обновление книги (например, изменить цену)
collection.update_one({"title": book_title}, {"$set": {"price": "45.00"}})
updated_book = collection.find_one({"title": book_title})
print(f'Обновленная книга: {updated_book}')

# 5. Удаление книги по названию
collection.delete_one({"title": book_title})
print(f'Книга "{book_title}" удалена.')
