#SQL used for Week 3 Day 1
use coding_dojo;
drop database coding_dojo;
INSERT INTO students (student_firstname, student_lastname, degree_plan, created_at, updated_at) VALUES ("Tae", "kwondo", "BSCS", CURRENT_TIMESTAMP , CURRENT_TIMESTAMP);
INSERT INTO students (student_firstname, student_lastname, degree_plan, created_at, updated_at) VALUES ("Luke", "Skywalker", "MBA", CURRENT_TIMESTAMP , CURRENT_TIMESTAMP);
INSERT INTO students (student_firstname, student_lastname, degree_plan, created_at, updated_at) VALUES ("Chewy", "Chewbaca", "BSKF", CURRENT_TIMESTAMP , CURRENT_TIMESTAMP);
INSERT INTO students (student_firstname, student_lastname, degree_plan, created_at, updated_at) VALUES ("Rey", "jedi", "BSMF", CURRENT_TIMESTAMP , CURRENT_TIMESTAMP);

SELECT * from students;

INSERT INTO faculty (faculty_firstname, faculty_lastname, program, created_at, updated_at) VALUES ("Bret", "May", "Computer Science", CURRENT_TIMESTAMP , CURRENT_TIMESTAMP);
INSERT INTO faculty (faculty_firstname, faculty_lastname, program, created_at, updated_at) VALUES ("Bruce", "Lee", "Martial Arts", CURRENT_TIMESTAMP , CURRENT_TIMESTAMP);
INSERT INTO faculty (faculty_firstname, faculty_lastname, program, created_at, updated_at) VALUES ("Yoda", "Master", "Business department", CURRENT_TIMESTAMP , CURRENT_TIMESTAMP);
INSERT INTO faculty (faculty_firstname, faculty_lastname, program, created_at, updated_at) VALUES ("Han", "Solo", "Pilot deparment", CURRENT_TIMESTAMP , CURRENT_TIMESTAMP);

SELECT * from faculty;

INSERT INTO courses (course_name, course_number, faculty_id) VALUES ("kicking", "101", 2);
INSERT INTO courses (course_name, course_number, faculty_id) VALUES ("training", "101", 1);
INSERT INTO courses (course_name, course_number, faculty_id) VALUES ("flying", "101", 4);
INSERT INTO courses (course_name, course_number, faculty_id) VALUES ("captian", "101", 3);

DELETE from courses where id=9;
SELECT * from courses;

INSERT INTO students_has_courses (student_id, course_id) VALUES (1, 2);
INSERT INTO students_has_courses (student_id, course_id) VALUES (2, 4);
INSERT INTO students_has_courses (student_id, course_id) VALUES (3, 5);
INSERT INTO students_has_courses (student_id, course_id) VALUES (4, 3);

INSERT INTO students_has_courses (student_id, course_id) VALUES (4, 5);

SELECT * from students_has_courses;


SELECT a.student_firstname, a.student_lastname, b.course_name, c.faculty_firstname, c.faculty_lastname 
FROM students a
JOIN students_has_courses ab ON a.id = ab.student_id
JOIN courses b ON ab.course_id = b.id
JOIN faculty c ON b.faculty_id = c.id
WHERE a.id = 4;

DELETE from students where id=12;
