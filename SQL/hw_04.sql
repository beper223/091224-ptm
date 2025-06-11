-- Вывести все заказы, отсортированные по убыванию по стоимости
select * from orders o
order by o.good_price DESC;

-- Вывести всех заказчиков, у которых почта зарегистриварована на gmail.com
SELECT * from customers c
where c.email like '%gmail.com';

-- Вывести заказы, добавив дополнительный вычисляемый столбец status, который вычисляется по стоимости заказа и имеет три значения: low, middle, high. 
SELECT *,
CASE
	WHEN o.good_price < 1 THEN 'low'
	WHEN o.good_price > 3 THEN 'hight'
	ELSE 'middle'
END as "STATUS"
from orders o ;

-- Вывести заказчиков по убыванию рейтинга.
SELECT * FROM customers c 
order by c.id desc;

-- Вывести всех заказчиков из города на ваш выбор. 
SELECT * from customers c 
where c.city = 'Berlin';

-- Написать запрос, который вернет самый часто продаваемый товар. 
SELECT o.good_description, COUNT(o.good_description)
FROM orders o
GROUP BY o.good_description;

-- Вывести список заказов с максимальной скидкой. 
SELECT * FROM orders o
where (o.good_price - o.discounter_price) = (SELECT
max(o.good_price - o.discounter_price) as 'discount'
FROM orders o );

-- Ответьте в 1 предложении: как вы определите скидку? 
-- Разница между ценой и ценой со скидкой

-- Ответьте в 1 предложении: может ли это быть разница между нормальной ценой и скидочной ценой? 
-- может

-- Написать запрос, который выведет все заказы с дополнительным столбцом процент_скидки, который содержит разницу в процентах между нормальной и скидочной ценой?
select * , round((o.discounter_price/o.good_price)*100,2) as "discountPersent"
from orders o;