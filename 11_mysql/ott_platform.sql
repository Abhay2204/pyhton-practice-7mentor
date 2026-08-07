create database ott_platform;
use ott_platform;

create table netflix (
    show_id int,
    show_name varchar(100),
    rating float,
    category varchar(100)
);

create table disney_hotstar (
    show_id int,
    show_name varchar(100),
    rating float,
    category varchar(100)
);

insert into netflix values
(1, 'Stranger Things', 8.7, 'Sci-Fi'),
(2, 'Breaking Bad', 9.5, 'Drama'),
(3, 'Wednesday', 8.1, 'Fantasy');

insert into disney_hotstar values
(1, 'The Mandalorian', 8.7, 'Action'),
(2, 'Loki', 8.2, 'Sci-Fi'),
(3, 'Criminal Justice', 8.1, 'Crime');
