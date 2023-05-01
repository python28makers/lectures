"""  
psql [db_name] [db_user] - войти в PostgreSQL

\q, exit - выйти из PostgreSQL

CREATE DATABASE db_name; - создание БД

\c db_name [db_user] - подключение к БД

\l - список БД

DROP DATABASE db_name; - удаление БД
"""

"""  
CREATE TABLE table_name(
    column_name data_type [constraint],
); - создание таблиц

ALTER TABLE table_name ...
ALTER TABLE table_name ADD COLUMN column_name data_type [constraint]; - добавление столбца

DROP TABLE table_name; - удаление таблицы
"""

"""  
ТИПЫ ДАННЫХ

Числовые типы:
1. Целые числа:
smallint - 2 байта, -32768 до 32767 
int - 4 байта, -2_147_483_648 до 2_147_483_647
bigint - 8 байт, -9_223_372_036_854_775_808 до 9_223_372_036_854_775_808

2. Числа с автоувеличением:
smallserial - 1 до 32767 
serial - 1 до 2_147_483_647
bigserial - 1 до 9_223_372_036_854_775_808

3. Числа с плавающей точкой
real - 4 байта, точность до 6 знаков после точки
double precision - 8 байт, точность до 15 знаков после точки
decimal / numeric - количество знаков: до 131072 до точки и 16383 после точки
money - точность до 2 знаков после запятой (100 - 100 сом)


Текстовые типы данных:
CHAR(n) - строка с постоянной длиной
VARCHAR(n) - строка с максимальной длиной

CHAR(10) -> 'hello' -> 'hello_ _ _ _ _'
VARCHAR(10) -> 'hello' -> 'hello'

TEXT - строка с неограниченной длиной


Булевые типы:
t/f, true/false, True/False

Datetime Types:
timestamp - дата и время - 2023-05-01 11:57:53.234234
date - дата - 2023-05-01
time - время - 11:57:53.234234
interval - временной промежуток

Enum - ограничение вариантов выбора
CREATE TYPE type_name AS ENUM('good','bad');
"""

"""  
Ограничения

UNIQUE - проверяет на уникальность
NULL - позволяет хранить пустое значение (None)
NOT NULL - нельзя хранить пустое значение
DEFAULT(значение) - устанавливает значение по умолчанию
CHECK(условие) - подходит ли под условие
PRIMARY KEY - уникальный ключ - определяет какое поле будет идентификатором (NOT NULL + UNIQUE)
FOREIGN KEY - внешний ключ - ссылка на другую таблицу
"""
