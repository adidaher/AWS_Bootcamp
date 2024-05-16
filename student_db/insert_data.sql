
-- Inserting the data in the tables

-- Studnets
INSERT INTO students (id, first_name, last_name, age) VALUES
(1, 'Alice', 'Smith', 22),
(2, 'Bob', 'Johnson', 21),
(3,'Carol', 'Williams', 23),
(4, 'David', 'Jones', 24);


-- Courses
INSERT INTO courses (course_id, course_name, teacher) VALUES
(1, 'Mathematics', 'Dr. Alan'),
(2, 'English', 'Prof. Elizabeth'),
(3, 'Science', 'Dr. Brown'),
(4, 'History', 'Prof. Charles');


-- Enrollments
INSERT INTO enrollments (student_id, course_id, semester, grade) VALUES
(1, 1, 'Fall 2024', 'A'),
(1, 2, 'Fall 2024', 'B'),
(2, 1, 'Fall 2024', 'C'),
(3, 4, 'Spring 2025', 'B'),
(4, 3, 'Spring 2025', 'A');
