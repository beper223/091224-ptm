use world;
-- 1. Вывести количество городов для каждой страны. Результат должен содержать
-- CountryCode, CityCount (количество городов в стране). Поменяйте запрос с использованием
-- джойнов так, чтобы выводилось название страны вместо CountryCode.
select c.CountryCode, co.Name, count(*) c_cnt from city c
left join country co ON co.Code = c.CountryCode
group by c.CountryCode;

-- 2. Используя оконные функции, вывести список стран с продолжительностью жизнью и
-- средней продолжительностью жизни.
SELECT Name,
       LifeExpectancy,
       ROUND(AVG(LifeExpectancy) OVER(), 2) AS avg_life_exp
FROM country;

-- 3. Используя ранжирующие функции, вывести страны по убыванию продолжительности жизни.
SELECT co.Name,
co.LifeExpectancy,
RANK() OVER (ORDER BY co.LifeExpectancy DESC) LE_rank
FROM country co;

-- 4. Используя ранжирующие функции, вывести третью страну с самой высокой
-- продолжительностью жизни.
select `Name` from (select `Name`,
LifeExpectancy,
RANK() OVER(ORDER BY LifeExpectancy DESC) class_rank
from country) as t1
where t1.class_rank = 3;