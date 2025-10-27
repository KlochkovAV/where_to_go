# Where to go

Интерактивная карта Москвы, для твоих любимых мест.

---

## Оглавление

- [Описание](#описание)
- [Установка](#установка)
- [Запуск](#запуск)
- [Технологии](#технологии)
- [Автор](#автор)

---

## Описание

Сервис предназначен для хранения данных об интересных местах. Загрузить информация можно в admin-зоне или используя комманду:

```
python manage.py load_place url_файла
```

Посмотреть проект можно по ссылке: https://klochkovav.pythonanywhere.com/

---

## Установка

1. Клонируйте репозиторий:

```
git clone https://github.com/KlochkovAV/where_to_go.git
cd where_to_go
```

2. Создайте и активируйте виртуальное окружение:

```
python -m venv venv
source venv/bin/activate  # Linux/macOS
source venv\Scripts\activate     # Windows
```

3. Обновите pip:

```
python -m pip install --upgrade pip
```

4. Установите зависимости:

```
pip install -r requirements.txt
```

5. Выполните миграции базы данных:

```
python manage.py migrate
```

6. Соберите статику:

```
python manage.py collectstatic
```

7. Создайте файл с переменными окружения SECRET_KEY, ALLOWED_HOSTS и DEBUG:

```
touch .env
```
---

## Запуск

```
python manage.py runserver
```

---

## Технологии

- Python
- Django
- Django REST Framework

---

## Автор

https://github.com/KlochkovAV (Артем Клочков)
