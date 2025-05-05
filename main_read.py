# open the text file and save it in a variable
f = open("emps_data.txt")
# print(f.read())

# print(f.readlines())


# make the big string of employees data in the text file as a list where every element of the list has all the employees data as one line
employees_data = f.readlines()

# make loop in the employees data to strip and split the employees data
for employee in employees_data:
    emp = employee.strip().split("-")
    salary = float(emp[-1]) * 2
    print(f"{emp[0]} - {emp[1]} - {emp[2]} - {salary} ")
# close the opened file
f.close()    

# achieving the same using with file as variable:
# with this file used as a variable f: do this and this
with open("emps_data.txt") as f:
    # make the big string of employees data in the text file as a list where every element of the list has all the employees data as one line
    employees_data = f.readlines()
    # make loop in the employees data to strip and split the employees data
    for employee in employees_data:
        emp = employee.strip().split("-")
        salary = float(emp[-1]) * 2
        print(f"{emp[0]} - {emp[1]} - {emp[2]} {salary}")

# doing the same using list comprehensions     



with open("emps_data.txt") as f:
    employees_data = [line.strip().split("-") for line in f]
    for emp in employees_data:
        salary = float(emp[-1]) * 2
        print(f"{emp[0]} - {emp[1]} - {emp[2]} {salary}")

# a cleaner code
with open("emps_data.txt") as f:
    employees = [line.strip().split("-") for line in f]

for e in employees:
    new_salary = float(e[-1]) * 2
    print(f"{e[0]} - {e[1]} - {e[2]} {new_salary}")


