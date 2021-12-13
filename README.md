### Dependencies:
* Redis 5.x+
* Django 3.x+
* Python 3.9+

### Описание

*В проекте две роли:*
* *'Пользователь' - USER*
* *'Сотрудник' - STAFF*


*Проект для регистраций заявок от 'Пользователей', на прохождение ПЦР-теста.
После заполнения заявки, она будет отображена как у 'Пользователя',
так и у 'Сотрудника', с единственным отличием того,
что 'Сотрудник' видит все заявки, а пользователь только свои.*

*Также 'Сотрудник' может менять статусы обработки заявки,
а так же результаты теста, тогда как 'Пользователь' может
их только отслеживать.*

### Инструкция к запуску

**создать и запустить виртуальное пространство:**
```commandline
python -m venv env
```

**Запустить можно в терминале. Либо в настройках вашей IDE:**
```commandline
. ./env/Scripts/activate
```

**Сколнировать репозиторий**: 
```commandline
https://github.com/BernarBerdikul/covid_test.git
```

**Скачать все нужные библиотеки:**
```commandline
pip install -r requirements.txt
```

**Создать миграции:**
```commandline
python manage.py migrate
```

**Создать супер пользователя:**
```commandline
python manage.py createsuperuser
```

**Запустить проект:**
```commandline
python manage.py runserver
```

*В папке /docs/postman, лежат коллекций Postman для тестирования API.*

В корне проекта находится exe-файл (PCR.exe) - 
это скомпилированное клиентское приложение. 
После запуска будет страница Авторизаций.
Можно зайти как superuser с Ролью STAFF, а можно зарегестрироваться как USER

### Страница Авторизаций

![login](https://github.com/BernarBerdikul/covid_test/blob/main/docs/images/login.jpg?raw=true)

### Страница просмотра заявок

![list_applications](https://github.com/BernarBerdikul/covid_test/blob/main/docs/images/list_applications.jpg?raw=true)

### Страница заполнения заявки

![create_application](https://github.com/BernarBerdikul/covid_test/blob/main/docs/images/create_application.jpg?raw=true)


**Ссылка на [административную консоль](http://127.0.0.1:8000/ru/super-secret-admin/)**
