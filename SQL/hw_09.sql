
-- 1. Вывести текущую дату и время.
SELECT DATE_FORMAT(NOW(), '%Y-%m-%d %H:%i:%s') as curent_date;

-- 2. Вывести текущий год и месяц
SELECT DATE_FORMAT(NOW(), '%Y-%m') as curent_year_and_month;

-- 3. Вывести текущее время
SELECT DATE_FORMAT(NOW(), '%H:%i:%s') as curent_year_and_month;

-- 4. Вывести название текущего дня недели
SELECT
CASE WEEKDAY(NOW())
WHEN 0 THEN 'Понедельник'
WHEN 1 THEN 'Вторник'
WHEN 2 THEN 'Среда'
WHEN 3 THEN 'Четверг'
WHEN 4 THEN 'Пятница'
WHEN 5 THEN 'Суббота'
WHEN 6 THEN 'Воскресение'
END as 'week_day';


-- 5. Вывести номер текущего месяца
SELECT DATE_FORMAT(NOW(), '%m') as curent_month;

-- 6. Вывести номер дня в дате “2020-03-18”
SELECT DATE_FORMAT('2020-03-18', '%d') as curent_day;

-- 7. Подключиться к базе данных shop (которая находится на удаленном сервере).
-- Определить какие из покупок были совершены апреле (4-й месяц)
use shop;
SELECT * FROM ORDERS o
where DATE_FORMAT(o.ODATE , '%m')='04';

-- 8. Определить количество покупок в 2022-м году
SELECT * FROM ORDERS o
where DATE_FORMAT(o.ODATE , '%Y')='2022';

-- 9. Определить, сколько покупок было совершено в
-- каждый день. Отсортировать строки в порядке возрастания
-- количества покупок. Вывести два поля - дату и количество покупок
SELECT o.ODATE ,COUNT(o.ORDER_ID) as count_orders FROM ORDERS o
group by o.ODATE
order by count_orders;

-- 10. Определить среднюю стоимость покупок в апреле
SELECT round(avg(o.AMT), 2) from ORDERS o
where DATE_FORMAT(o.ODATE , '%m')='04';
