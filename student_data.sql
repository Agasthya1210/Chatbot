CREATE TABLE studentdata (
    student_name VARCHAR(100),
    roll_number VARCHAR(11),
    attendance_percentage DECIMAL(5, 2),
    phone_number VARCHAR(15),
    first_semester_gpa DECIMAL(3, 2),
    second_semester_gpa DECIMAL(3, 2),
    cgpa DECIMAL(3, 2)
);
INSERT INTO studentdata (student_name, roll_number, attendance_percentage, phone_number, first_semester_gpa, second_semester_gpa, cgpa)
VALUES 
    ('Agasthya', 22261A1254, 85.5, '9032168082', 8.2, 8.6, 8.45),
    ('vedant', 22261A1262, 92.3, '987-654-3210', 9.0, 9.6, 9.3),
    ('Bhanu', 23265A1202, 78.9, '6301 473 904', 8.0, 8.5, 8.25),
    ('Ruthik', 22261A1263, 96.7, '789-012-3456', 4.0, 4.0, 4.0),
    ('Satvik', 22261A1217, 88.2, '321-654-9870', 3.5, 3.6, 3.55);
