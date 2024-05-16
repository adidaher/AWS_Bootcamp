
-- Retrieve all students enrolled in “Mathematics”.
SELECT s.first_name, s.last_name
FROM students s
JOIN enrollments e ON s.id = e.student_id 
JOIN courses c ON e.course_id = c.course_id
WHERE c.course_name = 'Mathematics';


-- Update Bob Johnson's grade in Mathematics.
UPDATE enrollments
SET grade = 'A-'
WHERE student_id = 2 AND course_id = 1 AND semester = 'Fall 2024';


-- Remove students below the age 21.
DELETE FROM students 
WHERE age < 21;
