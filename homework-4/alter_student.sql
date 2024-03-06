-- 1. Создать таблицу student с полями student_id serial, first_name varchar, last_name varchar, birthday date, phone varchar
CREATE TABLE student
(
	student_id serial,
	first_name varchar,
	last_name varchar,
	birthday date,
	phone varchar
)

-- 2. Добавить в таблицу student колонку middle_name varchar
ALTER TABLE student ADD COLUMN middle_name varchar

-- 3. Удалить колонку middle_name
ALTER TABLE student DROP COLUMN middle_name;

-- 4. Переименовать колонку birthday в birth_date
ALTER TABLE student RENAME COLUMN birthday TO birth_date;

-- 5. Изменить тип данных колонки phone на varchar(32)
ALTER TABLE student
ALTER COLUMN phone SET DATA TYPE varchar(32);

-- 6. Вставить три любых записи с автогенерацией идентификатора
ALTER TABLE student
ADD PRIMARY KEY(student_id);

INSERT INTO student(first_name, last_name, birth_date, phone)
VALUES('VOVA', 'AFONIN', '01-06-1998', '111');
INSERT INTO student(first_name, last_name, birth_date, phone)
VALUES('ARTUR', 'FASHEEV', '15-06-1999', '222');
INSERT INTO student(first_name, last_name, birth_date, phone)
VALUES('LERA', 'AFONINA', '13-06-2004', '333');

-- 7. Удалить все данные из таблицы со сбросом идентификатор в исходное состояние
TRUNCATE TABLE student RESTART IDENTITY