import sqlite3

#This project is a python script that interacts with a SQL database that keeps track of employee information. 
#CRUD (Create, Read, Update, Delete) functions: 

#Create function: adding an employee
def addEmployee(conn,cursor):
    #employee_id is not asked for; this is because it is auto-incrementing
    name = input("Enter employee name: ")
    age = int(input("Enter employee age: "))
    position = input("Enter employee position: ")
    salary = int(input("Enter employee salary: "))
    email = input("Enter employee email: ")
    cursor.execute('''
        INSERT INTO data (name, age, position, salary, email)
        VALUES(?,?,?,?,?)
''',(name, age, position, salary, email))
    conn.commit()

#Delete function: removing an employee
def removeEmployee(cursor,conn):
    employee_id = int(input("Enter the ID of the employee to be removed: "))
    cursor.execute('''
        DELETE FROM data WHERE employee_id = ?
    ''',(employee_id,))
    conn.commit()

#Read function: viewing all employees currently in the database
def viewEmployees(cursor,conn):
    cursor.execute("SELECT * FROM data")
    rows = list(cursor)
    if(len(rows) == 0):
        print("No current employees")
    else:
        for row in rows:
            print(row)
    conn.commit()

#Update function: updates information of currently existing employee
def updateCurrentEmployee(cursor,conn):
    employee_id = int(input("Enter the ID of the employee to be edited: "))
    fieldToUpdate = input("What about this employee would you like to update (name/age/position/salary/email) ? ")
    newValue = input("Enter the new value of the employee's " + fieldToUpdate + ": ")
    if(fieldToUpdate == "age" or fieldToUpdate == "salary"):
        newValue = int(newValue)
    cursor.execute(f'''
        UPDATE data
        SET {fieldToUpdate} = ?
        WHERE employee_id = ?;
''',(newValue,employee_id))
    conn.commit


#Additional functions: 
    
#This function shows all of the possible methods that the user can use
def viewMethods():
    print('''
          .add: adds employee
          .remove: removes employee
          .view: views all employees
          .update: updates information of current employee
          .help: shows possible methods
          .removeAll: removes all employees from database
          .stats: prints the 5-number summary including mean
          .exit: quit the program
          ''')

#removes all employees from database
def removeAll(cursor,conn):
    cursor.execute('''
        DELETE FROM data;
''')
    conn.commit()


#main function
def main():
    #SQL code to initialize database:
    #   CREATE TABLE data (
    #      employee_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    #      name TEXT,
    #      age INTEGER,
    #      position TEXT,
    #      salary INTEGER,
    #      email TEXT
    #   );

    #connects to the database
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    while True: 
        #The program asks the user for a method choice
        choice = input("Choose a method, or type \".help\" to view methods: ")
        #A method is called based on the user's choice
        if choice == ".add":
            addEmployee(cursor,conn)
        elif choice == ".remove":
            removeEmployee(cursor,conn)
        elif choice == ".view":
            viewEmployees(cursor,conn)
        elif choice == ".update":
            updateCurrentEmployee(cursor,conn)
        elif choice == ".help":
            viewMethods()
        elif choice == ".removeAll":
            removeAll(cursor,conn)
        elif choice == ".exit":
            break
        else:
            print("Invalid choice, try again")
    conn.close()

#executes main 
if __name__ == "__main__":
    main()