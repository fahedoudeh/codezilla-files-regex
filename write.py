# Open the original file "emps_data.txt" in read mode
with open("emps_data.txt") as f:
    # Read all lines from the file and store them in a list (each line is one employee's data)
    employees_data = f.readlines()

# Open (or create) a new file "new_emps_data.txt" in write mode
with open("new_emps_data.txt", "w") as f:
    # Loop through each line (employee record) from the original file
    for employee in employees_data:
        # Remove any leading/trailing whitespace and split the line into parts (name, position, salary)
        emp = employee.strip().split("-")
        # Convert the salary string to float and double it
        salary = float(emp[-1]) * 2
        # Write the updated employee data into the new file with the new salary
        f.write(f"{emp[0]} - {emp[1]} - {emp[2]} {salary}\n")
import os
print(os.getcwd())
