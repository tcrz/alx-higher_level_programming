-- creates a table second_table in the database hbtn_0c_0 
DROP TABLE IF EXISTS second_table;
CREATE TABLE second_table (id INT, name VARCHAR(20), score INT);
INSERT INTO second_table
VALUES
(1, "John", 10),
(2, "Alex", 3),
(3, "Bob", 14),
(4, "George", 8);
