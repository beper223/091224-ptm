-- Подключитесь к базе данных world (которая находится на удаленном сервере).
use world;

-- Выведите список стран с языками, на которых в них говорят.
select c.`Name`, group_concat(if(l.Language is not null, l.Language, '-') SEPARATOR ', ') Language from country c
left join countrylanguage l on c.Code = l.CountryCode
group by c.`Name`
order by c.`Name`;

-- Выведите список городов с их населением и названием стран
select ci.Name city_name, ci.Population, co.Name country_name from city ci
left join country co on ci.CountryCode = co.Code;

-- Выведите список городов в South Africa
select ci.Name city_name, co.Name country_name from city ci
join country co on ci.CountryCode = co.Code and co.Region = 'South Africa';

-- Выведите список стран с названиями столиц.
-- Подсказка: в таблице country есть поле Capital,
-- которое содержит номер города из таблицы City.
select co.Name country_name, if(ci.ID is not null,ci.Name,'-') Capital from country co
left join city ci on co.Capital = ci.ID;

-- Измените запрос 4 таким образом, чтобы выводилось население в столице
select co.Name country_name, if(ci.ID is not null,ci.Name,'-') capital_name,  if(ci.ID is not null,ci.Population,'-') capital_population from country co
left join city ci on ci.ID = co.Capital;

-- Напишите запрос, который возвращает название столицы United States
select co.Name country_name, ci.Name capital_name from country co
left join city ci on ci.ID = co.Capital
where co.Name = 'United States';

-- Используя базу hr_data.sql, вывести имя, фамилию и город сотрудника.
use hr;
select e.first_name, e.last_name, if(l.city is not null,l.city,'-') city from employees e
left join departments d on e.department_id = d.department_id
left join locations l on d.location_id = l.location_id;

-- Используя базу hr_data.sql, вывести города и соответствующие городам страны
select l.city, c.country_name country from locations l
left join countries c on l.country_id = c.country_id
order by l.city;


