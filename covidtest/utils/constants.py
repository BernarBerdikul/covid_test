OBJECTS_PER_PAGE_IN_ADMIN = 100
MAX_OBJECTS_IN_MODEL = 1
PASSWORD_MIN_LENGTH = 8

RESULT_EMPTY = 0
POSITIVE = 1
NEGATIVE = 2

PCR_TEST_RESULTS = (
    (RESULT_EMPTY, "Пусто"),
    (POSITIVE, "Позитивный"),
    (NEGATIVE, "Негативный"),
)

CREATED = 0
PERFORMED = 1
PROCESSED = 2
DONE = 3

APPLICATION_STATUSES = (
    (CREATED, "Заявка создана"),
    (PERFORMED, "Выполняется"),
    (PROCESSED, "Обрабатываются результаты"),
    (DONE, "Заявка завершена"),
)

MEN = 0
WOMEN = 1

GENDER_TYPES = (
    (MEN, "Мужской"),
    (WOMEN, "Женский"),
)

USER = 0
STAFF = 1
ADMIN = 2

USER_TYPES = (
    (USER, "USER"),
    (STAFF, "STAFF"),
    (ADMIN, "ADMIN"),
)

DAYS_OF_THE_WEEK = (
    (0, "ПН"),
    (1, "ВТ"),
    (2, "СР"),
    (3, "ЧТ"),
    (4, "ПТ"),
    (5, "СБ"),
    (6, "ВС"),
)

JANUARY = 1
FEBRUARY = 2
MARCH = 3
APRIL = 4
MAY = 5
JUNE = 6
JULY = 7
AUGUST = 8
SEPTEMBER = 9
OCTOBER = 10
NOVEMBER = 11
DECEMBER = 12

MONTHS = (
    (JANUARY, "янв", "январь"),
    (FEBRUARY, "фев", "февраль"),
    (MARCH, "мар", "март"),
    (APRIL, "апр", "апрель"),
    (MAY, "май", "май"),
    (JUNE, "июнь", "июнь"),
    (JULY, "июль", "июль"),
    (AUGUST, "авг", "август"),
    (SEPTEMBER, "сен", "сентябрь"),
    (OCTOBER, "окт", "октябрь"),
    (NOVEMBER, "ноя", "ноябрь"),
    (DECEMBER, "дек", "декабрь"),
)

ACTIVATION_SUBJECT = "Активация аккаунта"
