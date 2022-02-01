-- updates the score of Bob to 10 in the table second_table
-- without using Bob's id value, only the name field
UPDATE second_table t1, second_table t2
SET t1.score = t2.score
WHERE t1.name = "Bob" and t2.name = "John";

