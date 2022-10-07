# Итоговый совместный проект по теме API.

Бэкенд для работы с произведениям, отзывами и комментариями. 
Реализовано согласно ТЗ в формате redoc. Доступно после запуска проекта:
http://localhost:8000/redoc/

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Ramiras123/api_yamdb.git
```

```
cd api_yamdb/
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

## Импорт данных 

Импорт данных из static/data:
```
python3 manage.py import_data
```

Внимание, если при импорте возникают конфликты с ранее загруженными данными, то можно запустить скрипт с аругментов для предварительной очистки всех моделей:
```
python3 manage.py import_data --clear
```

Правда, в этом случае и суперюзер будет удален, так что скорее всего придется сделать 
```
python manage.py createsuperuser
```
Суперюзером можно войти в админку и посмотреть заполненность данных.