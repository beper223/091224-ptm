use world;
-- результат запроса возвращает 216 строк
SELECT 
    CountryCode, SUM(Population) Population
FROM
    city
GROUP BY CountryCode
HAVING SUM(Population) > 3000;

SELECT 
    co.Name, SUM(ci.Population) Population
FROM
    city ci
JOIN country co ON ci.CountryCode = co.Code
GROUP BY ci.CountryCode
HAVING SUM(ci.Population) > 3000;

SELECT 
    AVG(co.amount_of_cities) amount_of_cities
FROM
    (SELECT 
        co.Name, ci.amount_of_cities
    FROM
        (SELECT 
        CountryCode, COUNT(*) amount_of_cities
    FROM
        city
    GROUP BY CountryCode) ci
    INNER JOIN country co ON ci.CountryCode = co.Code) AS co



