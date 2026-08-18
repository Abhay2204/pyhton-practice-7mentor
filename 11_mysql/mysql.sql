-- ============================================================
--  MySQL Practice — All Core Topics (Before JOINs)
--  7Mentor Python + SQL Training | Abhay Mallick
-- ============================================================


-- ============================================================
-- SECTION 1: DATABASE & TABLE CREATION
-- ============================================================

CREATE DATABASE IF NOT EXISTS school_db;
USE school_db;

CREATE TABLE students (
    student_id   INT PRIMARY KEY AUTO_INCREMENT,
    name         VARCHAR(100),
    age          INT,
    city         VARCHAR(50),
    marks        FLOAT,
    grade        VARCHAR(5)
);

CREATE TABLE teachers (
    teacher_id   INT PRIMARY KEY AUTO_INCREMENT,
    name         VARCHAR(100),
    subject      VARCHAR(50),
    salary       FLOAT
);


-- ============================================================
-- SECTION 2: INSERT DATA
-- ============================================================

INSERT INTO students (name, age, city, marks, grade) VALUES
('Abhay Mallick',   21, 'Pune',      88.5, 'A'),
('Rohit Sharma',    22, 'Mumbai',    72.0, 'B'),
('Sneha Patil',     20, 'Pune',      95.0, 'A+'),
('Amit Kulkarni',   23, 'Nashik',    55.0, 'C'),
('Priya Desai',     21, 'Mumbai',    63.0, 'B'),
('Ravi Joshi',      22, 'Aurangabad',40.5, 'D'),
('Neha Gupta',      20, 'Pune',      91.0, 'A'),
('Suresh Yadav',    24, 'Nagpur',    78.5, 'B+');

INSERT INTO teachers (name, subject, salary) VALUES
('Mr. Ramesh',   'Python',      65000),
('Ms. Anjali',   'Mathematics', 58000),
('Mr. Vikas',    'English',     52000),
('Ms. Kavita',   'Science',     70000);


-- ============================================================
-- SECTION 3: SELECT — Basic Queries
-- ============================================================

-- Fetch all students
SELECT * FROM students;

-- Fetch only name and marks
SELECT name, marks FROM students;

-- Fetch distinct cities
SELECT DISTINCT city FROM students;


-- ============================================================
-- SECTION 4: WHERE — Filtering Rows
-- ============================================================

-- Students with marks above 80
SELECT name, marks FROM students WHERE marks > 80;

-- Students from Pune
SELECT name, city FROM students WHERE city = 'Pune';

-- Students with grade 'A' or 'A+'
SELECT name, grade FROM students WHERE grade = 'A' OR grade = 'A+';

-- Students NOT from Mumbai
SELECT name, city FROM students WHERE city != 'Mumbai';


-- ============================================================
-- SECTION 5: AND / OR / NOT / BETWEEN / IN / LIKE
-- ============================================================

-- Marks between 60 and 90
SELECT name, marks FROM students WHERE marks BETWEEN 60 AND 90;

-- Students from Pune or Mumbai
SELECT name, city FROM students WHERE city IN ('Pune', 'Mumbai');

-- Names starting with 'R'
SELECT name FROM students WHERE name LIKE 'R%';

-- Names containing 'a' anywhere
SELECT name FROM students WHERE name LIKE '%a%';

-- Students younger than 22 AND marks above 85
SELECT name, age, marks FROM students WHERE age < 22 AND marks > 85;


-- ============================================================
-- SECTION 6: ORDER BY — Sorting Results
-- ============================================================

-- Sort by marks descending (highest first)
SELECT name, marks FROM students ORDER BY marks DESC;

-- Sort by name alphabetically
SELECT name FROM students ORDER BY name ASC;


-- ============================================================
-- SECTION 7: LIMIT — Restrict Rows
-- ============================================================

-- Top 3 students by marks
SELECT name, marks FROM students ORDER BY marks DESC LIMIT 3;

-- First 5 records inserted
SELECT * FROM students LIMIT 5;


-- ============================================================
-- SECTION 8: AGGREGATE FUNCTIONS
-- ============================================================

-- Total number of students
SELECT COUNT(*) AS total_students FROM students;

-- Average marks
SELECT AVG(marks) AS average_marks FROM students;

-- Highest marks
SELECT MAX(marks) AS highest_marks FROM students;

-- Lowest marks
SELECT MIN(marks) AS lowest_marks FROM students;

-- Sum of all marks
SELECT SUM(marks) AS total_marks FROM students;


-- ============================================================
-- SECTION 9: GROUP BY & HAVING
-- ============================================================

-- Count of students per city
SELECT city, COUNT(*) AS student_count
FROM students
GROUP BY city;

-- Average marks per city
SELECT city, AVG(marks) AS avg_marks
FROM students
GROUP BY city;

-- Cities where average marks > 75
SELECT city, AVG(marks) AS avg_marks
FROM students
GROUP BY city
HAVING AVG(marks) > 75;


-- ============================================================
-- SECTION 10: UPDATE & DELETE
-- ============================================================

-- Update marks of a student
UPDATE students SET marks = 92.0 WHERE name = 'Rohit Sharma';

-- Update grade based on new marks
UPDATE students SET grade = 'A' WHERE marks >= 90;

-- Delete a student record
DELETE FROM students WHERE name = 'Ravi Joshi';

-- Verify changes
SELECT * FROM students;


-- ============================================================
-- SECTION 11: ALTER TABLE — Modify Structure
-- ============================================================

-- Add a new column
ALTER TABLE students ADD COLUMN email VARCHAR(100);

-- Rename a column
ALTER TABLE students RENAME COLUMN email TO student_email;

-- Change data type of a column
ALTER TABLE students MODIFY COLUMN age TINYINT;

-- Drop a column
ALTER TABLE students DROP COLUMN student_email;


-- ============================================================
-- SECTION 12: DROP / TRUNCATE
-- ============================================================

-- Remove all rows but keep table structure
-- TRUNCATE TABLE students;

-- Delete table completely
-- DROP TABLE students;

-- Delete entire database
-- DROP DATABASE school_db;


-- ============================================================
-- SECTION 13: OTT PLATFORM PRACTICE (Real-World)
-- ============================================================

CREATE DATABASE IF NOT EXISTS ott_platform;
USE ott_platform;

CREATE TABLE netflix (
    show_id   INT PRIMARY KEY AUTO_INCREMENT,
    show_name VARCHAR(100),
    rating    FLOAT,
    category  VARCHAR(50)
);

CREATE TABLE disney_hotstar (
    show_id   INT PRIMARY KEY AUTO_INCREMENT,
    show_name VARCHAR(100),
    rating    FLOAT,
    category  VARCHAR(50)
);

INSERT INTO netflix (show_name, rating, category) VALUES
('Stranger Things',  8.7, 'Sci-Fi'),
('Breaking Bad',     9.5, 'Drama'),
('Wednesday',        8.1, 'Fantasy'),
('Ozark',            8.4, 'Thriller'),
('Money Heist',      8.3, 'Action');

INSERT INTO disney_hotstar (show_name, rating, category) VALUES
('The Avengers',     8.7, 'Action'),
('Loki',             8.2, 'Sci-Fi'),
('The Mandalorian',  8.7, 'Action'),
('Criminal Justice', 8.1, 'Crime'),
('WandaVision',      7.9, 'Sci-Fi');

-- Q1: Shows with rating above 8.5 on Netflix
SELECT show_name, rating FROM netflix WHERE rating > 8.5;

-- Q2: All Sci-Fi shows on Disney+
SELECT show_name FROM disney_hotstar WHERE category = 'Sci-Fi';

-- Q3: Count of shows per category on Netflix
SELECT category, COUNT(*) AS total FROM netflix GROUP BY category;

-- Q4: Top 3 rated shows on Disney+
SELECT show_name, rating FROM disney_hotstar ORDER BY rating DESC LIMIT 3;

-- Q5: Average rating per category on Netflix
SELECT category, AVG(rating) AS avg_rating FROM netflix GROUP BY category;
