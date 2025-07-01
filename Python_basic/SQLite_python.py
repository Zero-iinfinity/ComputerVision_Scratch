#------------------------------------------------------------------------------
# CODE TO RUN SQL IN PYTHON
#------------------------------------------------------------------------------


import sqlite3

# First, we have to connect to a database. This line of code will connect you to an existing database or create a new database of the given name
conn = sqlite3.connect('demo.db') ## use sqlite3.connect(':memory:') for not creating or connecting to a database this will start fresh every time

# this will create a cursor that will move in the SQL file to write, and it is super important.
c = conn.cursor()


for writing SQL code first, we have to write c.execute() every time we write SQL code.
c.execute("""CREATE TABLE students(
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    class INT,
    age INT
);
""")

#for running this code, it's like sending it to the database, so we have to  do c.commit() after every sql Query
c.commit()

c.execute("""INSERT INTO students (student_id, name, class, age) VALUES
  (1, 'Aryan Singh', 10, 16),
  (2, 'Meera Gupta', 10, 15),
  (3, 'Ravi Patel', 11, 17),
  (4, 'Nisha Sharma', 12, 18),
  (5, 'Kabir Das', 11, 16),
  (6, 'Pooja Mehta', 12, 17),
  (7, 'Sita Devi', 10, 15),    -- Not enrolled in any course.
  (8, 'Rohan Jain', 11, 16),   -- Additional students for grouping.
  (9, 'Deepa Nair', 11, 17),
  (10, 'Arjun Rao', 11, 16);""")

conn.commit()

#we don't have to do c.commit for running SELECT query, but this will not print the result for getting the result we have to use c.fetchall(),c.fetchone() etc.
c.execute("SELECT * FROM students")
print(c.fetchall())
print(c.fetchone())

#The `conn.close()` method is used to terminate the connection to an SQLite database properly. This method is crucial for proper database management and resource handling.
conn.close()

#-------------------------------------------------------------------------------------------------------------------------------------------------------
#SQL IN EFFICIENT WAY: Using context management window (you don't need to commit after every query you write and no worries of closing the connection)
#--------------------------------------------------------------------------------------------------------------------------------------------------------

#for the whole database
with sqlite3.connect('demo.db') as conn:
# Your all Queries.

'''or'''

#for each query
with conn:
    c.execute("""CREATE TABLE students (
        student_id INT PRIMARY KEY,
        name VARCHAR(50),
        class INT,
        age INT);
    """)

