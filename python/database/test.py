import mysql.connector


try:
    connection = mysql.connector.connect(
        host="127.0.0.1",       
        user="root",            
        password="nahi2006",    
        database="uec"         
    )

    if connection.is_connected():
        print("Connected to MySQL database")
        
        # Perform database operations
        cursor = connection.cursor()  
        query = "SELECT * FROM student"  
        
        # Fetch and print all rows
        result = cursor.fetchall()
        for row in result:
            print(row)
        
        
        
    while True:
        roll = (input("Enter Roll Number: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        address = input("Enter Address: ")
        marks = int(input("Enter Marks: "))
        
        # SQL query to insert data
        insert_query = """
        INSERT INTO student (roll, name, age, address, marks)
        VALUES (%s, %s, %s, %s, %s)
        """

        values = (roll, name, age, address, marks)
        cursor.execute(insert_query, values)
        connection.commit()
        
        choice = input("Do you want to add another record? (yes/no): ").strip().lower() #The .strip() method in Python is used to remove leading and trailing whitespace or specified characters from a string. It is often used to clean up user input or text data.
        if choice != 'yes':
            break
            
    

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Ensure the connection is closed
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Connection closed.")
