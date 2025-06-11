-- Подключиться к базе данных world (которая находится на удаленном сервере). 
-- Посмотреть на таблицы city, country из базы world. В каждой таблице есть поле название (Name) и население (Population). Поле Name в одной таблице означает название города, а в другой - название страны. 
-- Написать запрос с помощью UNION, который выводит список названий всех городов и стран с их населением. Итоговая выборка должна содержать два столбца: Name, Population.
use world;
select `Name`, Population from city
union all
select `Name`, Population from country;

-- Посмотреть на таблицы в базе world и объяснить ограничения нескольких столбцов - ответить 1 предложением.
-- Ответ:
-- колонка 'Continent' таблицы 'country' имеет ограничение по значениям:
-- Значения могут быть: 'Asia','Europe','North America','Africa','Oceania','Antarctica','South America'
-- Так же ограничение "NOT NULL" запрещает отсутствие значения (NULL) в ячейке.

-- Далее работаем на локальном сервере. Создать новую таблицу citizen, которая содержит следующие поля:
-- уникальное автоинкрементное, номер соц страхования, имя, фамилию и емейл.
use 091224ptm_Sergii;
-- drop table if exists citizen;
CREATE TABLE citizen (
    id int not null auto_increment primary key,
    ssn VARCHAR(11),
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    email VARCHAR(255));

-- На вашем локальном сервере в любой базе создать таблицу без ограничений (любую, можно взять с урока).
drop table if exists Students2;
CREATE TABLE Students2 (
    first_name VARCHAR(100),
    last_name VARCHAR(100)
);

-- Добавить в таблицу 5 значений. Добавить 3 человека с одинаковыми именами и 2 человека без lastname
insert into Students2 (first_name, last_name) values
("Анатолий", "Волков"),
("Анатолий", "Костенко"),
("Анатолий", "Боровик"),
("Олеся"),
("Ольга");

-- Использовать оператор alter table … modify , чтобы добавить ограничение not null на поле firstname и lastname. 
ALTER TABLE Students2 
MODIFY first_name VARCHAR(100) NOT NULL;
ALTER TABLE Students2 
MODIFY last_name VARCHAR(100) NOT NULL;

-- Добавить ограничение unique для пары firstname\lastname.
ALTER TABLE Students2
ADD CONSTRAINT unique_name UNIQUE (first_name, last_name);

-- Удалить таблицу из базы и пересоздать ее, модифицировав запрос add table так,
-- чтобы он учитывал ограничения (см примеры из класса).
drop table if exists Students2;
CREATE TABLE Students2 (
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    CONSTRAINT unique_firstname_lastname UNIQUE (first_name, last_name)
);

-- Добавить правильные и неправильные данные (нарушающие и не нарушающие ограничения).

-- Правильные значения
insert into Students2 (first_name, last_name) values
("Анатолий", "Волков"),
("Анатолий", "Костенко");

-- Неправильные значения
insert into Students2 (first_name, last_name) values
("Анатолий", "Костенко"),
("Олеся");


