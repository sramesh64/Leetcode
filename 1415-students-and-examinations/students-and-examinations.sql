# Write your MySQL query statement below
 

# Write a solution to find the number of times each student attended each exam.

SELECT Students.student_id, student_name, Subjects.subject_name, count(Examinations.subject_name) AS attended_exams
FROM Students
CROSS JOIN Subjects
LEFT JOIN Examinations ON Students.student_id = Examinations.student_id AND Examinations.subject_name = Subjects.subject_name
GROUP BY Students.student_id, Subjects.subject_name
ORDER BY Students.student_id, Subjects.subject_name