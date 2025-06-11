# Работаем с базой данных sakila.
# Вывести названия фильмов с расшифровкой рейтинга для каждого. Рейтинги описаны здесь. В таблице film хранятся годы рейтингов. Нужно воспользоваться оператором case чтобы определить для каждого кода условие, по которому будет выводится его развернутое описание (1 предложение).
use sakila;
SELECT
  title,
  rating,
  CASE rating
    WHEN 'G' THEN 'Допускается для всех возрастов.'
    WHEN 'PG' THEN 'Рекомендуется присутствие родителей.'
    WHEN 'PG-13' THEN 'Некоторые материалы могут быть неподходящими для детей до 13 лет.'
    WHEN 'R' THEN 'Лицам до 17 лет обязательно сопровождение родителя или взрослого опекуна.'
    WHEN 'NC-17' THEN 'Лицам до 17 лет просмотр запрещён.'
    ELSE 'Неизвестный рейтинг.'
  END AS rating_description
FROM film;

# Выведите количество фильмов в каждой категории рейтинга. Используем group by.
SELECT c.name, count(fc.film_id) count_film_id FROM film_category fc
left join category c on c.category_id = fc.category_id
group by c.name
order by count_film_id desc;

# Используя оконные функции и partition by, выведите список названий фильмов, рейтинг и количество фильмов в каждом рейтинге.
# Объясните, чем отличаются результаты предыдущего запроса и запроса в этой задаче.
SELECT
  title,
  rating,
  COUNT(*) OVER (PARTITION BY rating) AS rating_count
FROM film;
-- GROUP BY — подводит итоги.
-- PARTITION BY в оконной функции — добавляет агрегированное значение к каждой строке, не теряя строки.

# Изучите таблицы payment и customer. Выведите список всех платежей с указанием имени и фамилии каждого заказчика, датой платежа и суммой.
SELECT
    c.first_name,
    c.last_name,
    p.payment_date,
    p.amount
FROM payment p
JOIN customer c ON p.customer_id = c.customer_id;

# Поменяйте предыдущий запрос так, чтобы дата выводилась в формате “число, название месяца, год” (без времени).
SELECT
    c.first_name,
    c.last_name,
    DATE_FORMAT(p.payment_date, '%e %M %Y') AS formatted_date,
    p.amount
FROM payment p
JOIN customer c ON p.customer_id = c.customer_id;