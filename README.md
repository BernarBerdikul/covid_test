Зависимости:
* Redis 5+
* Django 3+
* Python 3.9+

создать и запустить виртуальное пространство:
`python -m venv env`

Запустить можно в терминале `. ./env/Scripts/activate`
Либо в настройках вашей IDE

Сколнировать репозиторий: 
`https://github.com/BernarBerdikul/covid_test.git`

Скачать все нужные библиотеки: 
`pip install -r requirements.txt`

Создать миграции:
`py manage.py migrate`

Создать супер пользователя:
`py manage.py createsuperuser`

Запустить проект: 
`py manage.py runserver`
