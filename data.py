import sqlite3
import tkinter as tk

#This project is a python script that interacts with a SQL database that keeps track of employee information. 

conn=sqlite3.connect('data.db')
cursor=conn.cursor()
#CRUD (Create, Read, Update, Delete) functions: 

#Create function: adding an employee
def addEmployee():
    #employee_id is not asked for; this is because it is auto-incrementing
    name = name_entry.get()
    age = int(age_entry.get())
    position = position_entry.get()
    salary = int(salary_entry.get())
    email = email_entry.get()
    cursor.execute('''
        INSERT INTO data (name, age, position, salary, email)
        VALUES(?,?,?,?,?)
''',(name, age, position, salary, email))
    conn.commit()

#Delete function: removing an employee
def removeEmployee():
    employee_id = employee_id_entry.get()
    cursor.execute('''
        DELETE FROM data WHERE employee_id = ?
    ''',(employee_id,))
    conn.commit()

#Read function: viewing all employees currently in the database
def viewEmployees():
    cursor.execute("SELECT * FROM data")
    rows = list(cursor)
    if(len(rows) == 0):
        result_label.config(text="No current employees")
    else:
        for row in rows:
            result_label.config(text='''

''')
            for row in rows:
                result_label.config(text=result_label.cget("text") + str(row) + "\n")

#Update function: updates information of currently existing employee
def updateCurrentEmployee():
    employee_id = int(update_id_entry.get())
    field_to_update = update_field_entry.get()
    new_value = update_value_entry.get()
    if field_to_update == "age" or field_to_update == "salary":
        new_value = int(new_value)
    cursor.execute(f'''
        UPDATE data
        SET {field_to_update} = ?
        WHERE employee_id = ?;
    ''', (new_value, employee_id))
    conn.commit()


#Additional functions: 
    
#This function shows all of the possible methods that the user can use
def viewMethods():
    result_label.config(text='''
                        
        Add Employee: Adds an employee to the database
        Remove Employee: Removes an employee from the database given their ID
        View Employees: Displays all current employees
        Update Employee: Changes the information of a currently existing employees
        Remove All Employees: Removes all currently existing employees
        Help/View Methods: Provides explanation on functionality
          ''')

#removes all employees from database
def removeAll(cursor,conn):
    cursor.execute('''
        DELETE FROM data;
''')
    conn.commit()


#main window
root = tk.Tk()
root.title("Employee Management System")

#Adding employee
add_frame = tk.Frame(root)
add_frame.pack(pady=10)

tk.Label(add_frame,text="Name: ").grid(row=0,column=0)
name_entry = tk.Entry(add_frame)
name_entry.grid(row=0,column=1)
name_entry.after_cancel

tk.Label(add_frame,text="Age: ").grid(row=1,column=0)
age_entry = tk.Entry(add_frame)
age_entry.grid(row=1,column=1)

tk.Label(add_frame, text="Position:").grid(row=2, column=0)
position_entry = tk.Entry(add_frame)
position_entry.grid(row=2, column=1)

tk.Label(add_frame, text="Salary:").grid(row=3, column=0)
salary_entry = tk.Entry(add_frame)
salary_entry.grid(row=3, column=1)

tk.Label(add_frame, text="Email:").grid(row=4, column=0)
email_entry = tk.Entry(add_frame)
email_entry.grid(row=4, column=1)

add_button = tk.Button(add_frame, text="Add Employee", command=addEmployee)
add_button.grid(rowspan=5,columnspan=2,pady=5)


# Removing employee
remove_frame = tk.Frame(root)
remove_frame.pack(pady=10)

tk.Label(remove_frame, text="Employee ID:").grid(row=0, column=0)
employee_id_entry = tk.Entry(remove_frame)
employee_id_entry.grid(row=0, column=1)

remove_button = tk.Button(remove_frame, text="Remove Employee", command=removeEmployee)
remove_button.grid(rowspan=1, columnspan=2, pady=5)

# Updating Employees
update_frame = tk.Frame(root)
update_frame.pack(pady=10)

tk.Label(update_frame,text="Enter ID of employee to be updated: ").grid(row=0,column=0)
update_id_entry=tk.Entry(update_frame)
update_id_entry.grid(row=0,column=1)

tk.Label(update_frame,text="What field should be updated? (name/age/position/salary/email)").grid(row=1,column=0)
update_field_entry = tk.Entry(update_frame)
update_field_entry.grid(row=1,column=1)

tk.Label(update_frame,text="What is this field's new value? ").grid(row=2,column=0)
update_value_entry = tk.Entry(update_frame)
update_value_entry.grid(row=2,column=1)

update_button = tk.Button(update_frame, text="Update Employee", command=updateCurrentEmployee)
update_button.grid(rowspan=3,columnspan=2,pady=5)

# Removing All Employees


# Viewing Employees
view_frame = tk.Frame(root)
view_frame.pack(pady=10)

view_button = tk.Button(view_frame, text="View Employees", command=viewEmployees)
view_button.pack()

result_label = tk.Label(view_frame, text="")
result_label.pack()

# Help method
help_frame = tk.Frame(root)
help_frame.pack(pady=10)

help_button = tk.Button(view_frame, text="Help/View Methods", command=viewMethods)
help_button.pack()

result_label = tk.Label(view_frame, text="")
result_label.pack()

root.mainloop()
conn.close()