import sqlite3

# stmt contains placeholder ?'s for params
# params is a tuple (val1, val2, ...)
def query(con, stmt, params=None):
  cur = con.cursor()
  if params is None:
    result = cur.execute(stmt)
  else:
    result = cur.execute(stmt, params)
  con.commit()
  return result

con = sqlite3.connect('main.db')

# Create Courses table
res = query(con, "CREATE TABLE Courses (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, CourseNum TEXT NOT NULL, CourseName TEXT NOT NULL);")

# Create CourseReqs Table
res = query(con, "CREATE TABLE CourseReqs (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, CoreID TEXT NOT NULL, MajorID INTEGER NOT NULL, MinorID INTEGER NOT NULL, FOREIGN KEY(CoreID) REFERENCES CoreReqs(ID), FOREIGN KEY(MajorID) REFERENCES MajorReqs(ID), FOREIGN KEY(MinorID) REFERENCES MinorReqs(ID));")

# Create CoreReqs Table
res = query(con, "CREATE TABLE CoreReqs (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, CourseType TEXT NOT NULL);")

# Add Core Requirements
res = query(con, "INSERT INTO CoreReqs (CourseType) VALUES ('CIE');")

res = query(con, "INSERT INTO CoreReqs (CourseType) VALUES ('Diversity and Inequality');")

res = query(con, "INSERT INTO CoreReqs (CourseType) VALUES ('Obligations');")

# Create MajorReqs Table
res = query(con, "CREATE TABLE MajorReqs (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, CourseNum TEXT NOT NULL, CourseName TEXT NOT NULL);")

# Add Major Requirements
res = query(con, "INSERT INTO MajorReqs (CourseNum, CourseName) VALUES ('CS173','Intro');")

res = query(con, "INSERT INTO MajorReqs (CourseNum, CourseName) VALUES ('CS174','OO Programming');")

res = query(con, "INSERT INTO MajorReqs (CourseNum, CourseName) VALUES ('CS274' ,'Architecture');")

# Create MinorReqs Table
res = query(con, "CREATE TABLE MinorReqs (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, CourseNum TEXT NOT NULL, CourseName TEXT NOT NULL);")

res = query(con, "INSERT INTO MinorReqs (CourseNum, CourseName) VALUES ('CHN101', 'Elementary Chinese I');")

res = query(con, "INSERT INTO MinorReqs (CourseNum, CourseName) VALUES ('CHN102', 'Elementary Chinese II');")

res = query(con, "INSERT INTO MinorReqs (CourseNum, CourseName) VALUES ('CHN111', 'Advanced Elementary Chinese I');")


result = res.fetchone()
print(result)

result = res.fetchall()
for row in result:
  print(row)

con.close()