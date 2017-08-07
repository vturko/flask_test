CREATE DATABASE IF NOT EXISTS Users;
USE Users;

DROP TABLE IF EXISTS course_user CASCADE;
DROP TABLE IF EXISTS user CASCADE;
DROP TABLE IF EXISTS courses CASCADE;

CREATE TABLE user (
id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY NOT NULL,
name VARCHAR(50) NOT NULL,
email VARCHAR(255),
status INT(1) NOT NULL,
phone VARCHAR(11),
mobile VARCHAR(11));

CREATE TABLE courses (
id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY NOT NULL,
name VARCHAR(50) NOT NULL,
code VARCHAR(50) NOT NULL);

CREATE TABLE course_user (
user INT UNSIGNED NOT NULL,
course INT UNSIGNED NOT NULL,
PRIMARY KEY (user, course),
CONSTRAINT constr_user_cu
FOREIGN KEY user_cu (user) REFERENCES user(id)
ON DELETE CASCADE ON UPDATE CASCADE,
CONSTRAINT constr_course_cu
FOREIGN KEY course_cu (course) REFERENCES courses(id)
ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO user (name, email, status, phone, mobile) VALUES
('Gary Bysey', 'gary@gmail.com', 1, '83221111111', '80971111111'),
('Jeff Bridges', 'jeff@gmail.com', 0, '83221231234', '80671231234'),
('Harold Stone', 'harold@gmail.com', 0, '83222222222', '80672222222'),
('Alane Dell', 'al@gmail.com', 1, '83222222222', '80672222222');

INSERT INTO user (name, email, status, phone) VALUES
('Don Rick', 'don@gmail.com', 0, '83222222222'),
('Robert White', 'white@gmail.com', 1, '83222200222'),
('Donald Trump', 'don@gmail.com', 1, '88777777777'),
('Ray Milland', 'ray@gmail.com', 0, '12345678912');

INSERT INTO user (name, email, status, mobile) VALUES
('Bruno Dumont', 'bruno@gmail.com', 0, '83222222222'),
('Phil Jore', 'phil@gmail.com', 1, '87654321321'),
('Bernard Pur', 'ben@gmail.com', 0, '12345678912');

INSERT INTO user (name, email, status) VALUES
('Michael Cimino', 'mike@gmail.com', 0),
('Rodger Corman', 'rod@gmail.com', 0),
('John Dow', 'jdow@gmail.com', 1),
('Werner Krauss', 'wern@gmail.com', 0),
('Lucy Caron', 'lucy@gmail.com', 1);

insert into courses (name, code) values
('Python base', 'PO12345'),
('Python database', 'P234567'),
('HTML', 'H345678'),
('Java base', 'J456789'),
('management', 'M987654'),
('JQuery', 'JQ78922'),
('Flask', 'F879552'),
('Django', 'D112484');

insert into course_user (user, course) values
(6, 1),
(3, 4),
(2, 2),
(6, 2),
(2, 8),
(1, 3),
(4, 7),
(5, 4),
(10, 1),
(1, 5);