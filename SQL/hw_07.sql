-- Подключитесь к базе данных hr (которая находится на удаленном сервере)
USE hr;
-- Выведите количество сотрудников в базе
select count(employee_id) count_employee
from employees;
-- Выведите количество департаментов (отделов) в базе
select count(department_id) count_department
from departments;
-- Подключитесь к базе данных World (которая находится на удаленном сервере)
USE world;
-- Выведите среднее население в городах Индии (таблица City, код Индии - IND)
select avg(Population) avg_population
from city
where CountryCode = 'IND';
-- Выведите минимальное население в индийском городе и максимальное.
select min(Population) min_population, max(Population) max_population
from city
where CountryCode = 'IND';
-- Выведите самую большую площадь территории.
select max(SurfaceArea) max_surfaceArea
from country;
-- Выведите среднюю продолжительность жизни по странам.
select avg(LifeExpectancy) avg_lifeExpectancy
from country;
-- Найдите самый населенный город (подсказка: использовать подзапросы)
select c.Name, c.Population
from city c
join (select max(Population) max_population from city) p on c.Population = p.max_population

