use 091224ptm_Sergii;
drop table if exists weather;

CREATE TABLE weather (
    city VARCHAR(50),
    forecast_date date,
    temperature integer);

insert into weather values
("Berlin","2023-08-29",30);    

insert into weather values
("Norwich","2023-08-28",11),
("Stuttgart","2023-08-27",-5),
("Freiburg","2023-08-26",-3);

UPDATE weather 
SET temperature = 26
WHERE city = 'Berlin';

UPDATE weather 
SET city = 'Paris'
WHERE temperature > 25;

alter table weather
add column min_temp integer;

UPDATE weather 
SET min_temp = 0;

SELECT * FROM weather;