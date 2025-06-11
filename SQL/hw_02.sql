use hr;
-- 1. вывести список всех сотрудников. 
SELECT * FROM employees;
-- 2. Найти поле с зарплатой сотрудника.
-- Ответ: это поле salary в таблице employees
-- 3. Используя операторы case/when/end, изменить запрос так, чтобы результатом был только один столбец,
-- назовите его SALARY_GROUP и оно будет принимать значение 1 если зп сотрудника больше 10000 и значение 0, если меньше.
SELECT 
    CASE
        WHEN salary > 10000 THEN 1
        ELSE 0
    END SALARY_GROUP
FROM
    employees;
-- 4. Ответить одним предложением: почему выводится только один столбец?
-- Ответ: после команды SELECT описан лишь один столбец
-- 5. Изменить запрос, так, чтобы вывелось два столбца: имя сотрудника и новое поле SALARY_GROUP.
SELECT 
    first_name,
    salary,
    CASE
        WHEN salary > 10000 THEN 1
        ELSE 0
    END SALARY_GROUP
FROM
    employees;
-- 6. Вывести среднюю зарплату для департаментов с номерами 60, 90 и 100 используя составное условие.
SELECT 
    AVG(CASE
        WHEN
            department_id = 60 OR department_id = 90
                OR department_id = 100
        THEN
            salary
        ELSE NULL
    END) AS avg_dp60_90_100
FROM
    hr.employees;
-- 7. Разделить уровни (level) сотрудников на junior < 10000,10000<mid<15000, senior>15000 в зависимости от их зарплаты.
-- Вывести список сотрудников (first_name, last_name, level).
SELECT 
    first_name,
    last_name,
    -- salary,
    CASE
        WHEN salary < 10000 THEN 'junior'
        WHEN salary > 10000 and salary < 15000 THEN 'mid'
        WHEN salary > 15000 THEN 'senior'
        ELSE 0
    END `level`
FROM
    employees;
-- 8. осмотреть содержимое таблицы jobs. Написать запрос c использованием оператора case/when/end,
-- который возвращает 2 столбца: job_id, payer_rank, где столбец payer_rank формируется по правилу:
-- если максимальная зарплата больше 10000, то “high_payer”, если меньше, то “low payer”.
SELECT 
    job_id,
    -- max_salary,
    CASE
        WHEN max_salary < 10000 THEN 'low payer'
        WHEN max_salary > 10000 THEN 'high_payer'
        ELSE 0
    END payer_rank
FROM
    jobs;

-- 9. Переписать этот запрос с использованием оператора IF.
-- 10. Поменять предыдущий запрос так, чтобы выводилось 3 столбца, к двум существующим добавьте max_salary и отсортировать результат по убыванию.
SELECT 
    job_id,
    max_salary,
    IF(max_salary < 10000,
        'low payer',
        IF(max_salary > 10000, 'high_payer', 0)) payer_rank
FROM
    jobs
order by max_salary desc