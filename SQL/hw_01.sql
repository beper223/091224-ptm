use hr;
SELECT first_name, last_name, job_id FROM employees
where job_id = 'IT_PROG';

SELECT first_name, last_name, job_id FROM employees
where job_id = 'AD_VP';

SELECT first_name, last_name, salary FROM employees
where salary between 10000 and 20000;

SELECT first_name, last_name, department_id FROM employees
where department_id in (30, 60, 100);

SELECT first_name, last_name FROM employees
where first_name like '_%ll%_';

SELECT first_name, last_name FROM employees
where first_name like '%a';

SELECT first_name, last_name, salary FROM employees
where salary > 10000;

SELECT first_name, last_name, salary FROM employees
where salary > 10000 and first_name like 'L%';

-- 7) Не выполняя запрос к базе данных, предсказать его результат: select *  from employees where salary > 10000 or salary <= 10000;
-- Ответ: в выборку попадут все записи

-- 8) Ответить в 1 предложении: чем он будет отличаться от результата этого запроса? select *  from employees where salary > 10000 or salary < 10000;
-- Ответ: в выборку не покадут записи, где salary = 10000

-- 9) Не выполняя запрос к базе, предсказать результат. select *  from employees where salary > 10000 and salary < 5000;
-- Ответ: в выборку не попадет ни одной записи