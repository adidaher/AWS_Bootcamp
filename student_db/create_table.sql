
-- Creating an empty database.
CREATE DATABASE student_db;
USE student_db;


-- Creating empty tables for the database.

-- Student table
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT
);

-- Courses table
CREATE TABLE courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(50),
    teacher VARCHAR(50)
);


-- Enrollment table
CREATE TABLE enrollments (
    student_id INT, 
    course_id INT,
    semester VARCHAR(50),
    grade CHAR(2),
    PRIMARY KEY (student_id, course_id, semester),
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);
