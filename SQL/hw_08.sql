/*Подключитесь к базе данных Students (которая находится на удаленном сервере).*/
use Students;
/*Найдите самого старшего студента*/

SELECT
s.name
,max(age)
FROM Students s ;

/*Найдите самого старшего преподавателя*/
SELECT
name
,max(age)
from Teachers t;

/*Выведите список преподавателей с количеством компетенций у каждого*/
SELECT
t.name
,(SELECT count(tc.competencies_id) FROM Teachers2Competencies tc where tc.teacher_id = t.id)
FROM Teachers t;

/*Выведите список курсов с количеством студентов в каждом*/

SELECT
c.title
,(SELECT count(sc.course_id) FROM Students2Courses sc WHERE sc.course_id=c.id)
From Courses c ;


/*Выведите список студентов, с количеством курсов, посещаемых каждым студентом. */
SELECT
s.name
,(SELECT COUNT(sc.course_id) FROM Students2Courses sc WHERE sc.student_id=s.id)
FROM Students s;