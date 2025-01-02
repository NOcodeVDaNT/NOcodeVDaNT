#vedanbt dahake aka GHOST


import sqlite3

#creating connection
conn = sqlite3.connect('ghostdatabase.db')


c = conn.cursor()
#creating a cursor:This creates a cursor object, which allows you to execute SQL commands.
#The cursor (c) is used to interact with the database, fetch data, and manage transactions.




#creating table:
c.execute('''
          CREATE TABLE IF NOT EXISTS ghost
          (id INTEGER PRIMARY KEY AUTOINCREMENT, name text, age integer, gender text)
          ''')

# (id INTEGER PRIMARY KEY AUTOINCREMENT, name text, age integer, gender text): 
# This defines the columns and their data types in the table:
# - 'id': An integer column that serves as the primary key for the table.
# - 'INTEGER PRIMARY KEY': Specifies that the 'id' column is the primary key and the values in this column will be unique.
# - 'AUTOINCREMENT': Automatically generates a new unique 'id' value for each new row inserted, starting from 1.
# - 'name': A text column to store the name of the person.
# - 'age': An integer column to store the person's age.,real is also a data type that can store float value too
# - 'gender': A text column to store the person's gender.




# c.execute("INSERT INTO ghost (name, age, gender) VALUES ('John', 25, 'Male')")
# data = [
#     ('vedant', 25, 'Male'),
#     ('Alice', 30, 'Female'),
#     ('Bob', 22, 'Male')
# ]

# # Insert multiple rows using a loop
# for person in data:
#     c.execute("INSERT INTO ghost (name, age, gender) VALUES (?, ?, ?)", person)







#retriving data:
#c.execute("SELECT * FROM ghost")
c.execute("SELECT rowid, * FROM ghost") #will give primary key too i.e row id


# print(c.fetchall())
#c.fetchone() give first item
#c.fetchmany(i) give upto ith item
#c.fetchall()[i] give ith item in tuple 0th,1st,2nd=name,age,gender


#cleaner way to print
items=c.fetchall()
for i in items:
    print(f"index:{i[1]} , Name: {i[2]} , Age: {i[3]} , Gender:{i[4]}")
    
    
print("\n\n--------------------------------------------------------------------------------------------------------")
c.execute("SELECT * FROM ghost WHERE age > 24")
print(c.fetchall())  


print("\n\n--------------------------------------------------------------------------------------------------------")
c.execute("SELECT * FROM ghost WHERE name LIKE 'A%'")  # Names starting with 'A'
print(c.fetchall())  


print("\n\n--------------------------------------------------------------------------------------------------------")
c.execute("SELECT * FROM ghost WHERE name LIKE '%o%'")  # Names containing 'o'
print(c.fetchall()) 


print("\n\n--------------------------------------------------------------------------------------------------------")
# WHERE with BETWEEN
c.execute("SELECT * FROM ghost WHERE age BETWEEN 23 AND 30")
print(c.fetchall())  



print("\n\n--------------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------------")


#UPDATE RECORDS
c.execute("""
          UPDATE ghost SET name = 'Ghost_1' WHERE age='30'             
          """) #WHERE rowid=i can be used to update specific row

# Verify the changes after update
c.execute("SELECT * FROM ghost")
print(c.fetchall()) 


print("\n\n--------------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------------")


#DELETE RECORDS
c.execute("DELETE FROM ghost WHERE age='30'") #WHERE rowid=i can be used
# Verify the changes after delete
c.execute("SELECT * FROM ghost")
print(c.fetchall())

print("\n\n--------------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------------")


#ORDER BY is used for sorting the records in ascending or descending order
#ASC is used for ascending order and DESC is used for descending order
c.execute("SELECT * FROM ghost ORDER BY age ASC")
print(c.fetchall())
# c.execute("SELECT * FROM ghost ORDER BY age DESC")

# c.execute("SELECT * FROM ghost ORDER BY name ASC")

# c.execute("SELECT * FROM ghost ORDER BY name ASC")

# c.execute("SELECT * FROM ghost ORDER BY name DESC")

# c.execute("SELECT * FROM ghost ORDER BY age DESC")

# c.execute("SELECT * FROM ghost ORDER BY age ASC")

print("\n\n--------------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------------")





#we can use AND and OR operators to combine conditions





#commiting the changes
conn.commit()
# SQLite uses transactions to ensure the integrity of the database. Any changes (like creating tables, inserting data, or deleting rows) are initially made in a temporary state.
# These changes will not be permanently applied to the database file until conn.commit() is called.
# If you don't call conn.commit() and close the connection, any unsaved changes will be discarded.


#close the connectio
conn.close()

