SELECT * FROM public.teacher
-- create table user1 (
-- id serial primary key,
-- name varchar(50) not null,
-- surname varchar(50) not null,
-- phone varchar(20) not null,
-- email varchar(50) unique not null,
-- age integer check (age > 0)
--  )

-- insert into user1 (name, surname, phone, email, age)
-- values ('ali', 'vali',54545698, 'sdghj@gmail.com',54)

-- create table teacher (
-- id serial primary key,
-- name varchar(50) not null,
-- surname varchar(50) not null,
-- phone varchar(20) not null,
-- email varchar(50) unique not null,
-- course varchar(15) not null
--  )

-- insert into teacher (name, surname, phone, email, course)
-- values ('ali', 'vali',54545698, 'sdghj@gmail.com','python')

create table teacher (
    id serial primary key,
    first_name varchar(50) not null,
    last_name varchar(50) not null,
    phone varchar(20),
    email varchar(50) unique,
    course varchar(50) not null
)
