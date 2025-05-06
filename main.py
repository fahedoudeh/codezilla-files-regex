import csv
import prettytable

def main():
    # Read Employees Dat
    employees_data = read_csv_file("employees_data.csv")
    
    # Double the salary of each Employee
    updated_employees_data = update_salary(employees_data)

    # Sort employees by salary 
    sorted_employess_data = sort_data(updated_employees_data)

    # Write employees data to a file   
    write_csv_file("employees_data_new",sorted_employess_data)
    print("Done!")

def read_csv_file(file_name):
    """Get file name
    Read the data from the file
    Return the data in the file as a list"""
    with open(file_name) as f:
        csv_data = csv.reader(f)
        data_lst = list(csv_data) 
        return data_lst
    
def update_salary(list): 
    """Get employees list
    Update salary
    Return list after updating salary"""
    for employee in list:
        employee[-1] = employee[-1].replace(",", "")
        employee[-1] = float(employee[-1]) * 2 
    return list

def sort_data(data_list):
    """sort the data by salary and then by name
    
       parameters:
       data_list: list of lists which contains the data to be sorted

       return:
       sorted_employees_data: list of lists which contains the sorted data
    """
    sorted_employees_data = sorted(data_list, key=lambda employee: (employee[3], employee[0]))
    return sorted_employees_data

def write_csv_file(file_name, new_data):
    """Get file name and data to be writen
    Write data as a csv file """
    with open(file_name, "w") as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerows(new_data)

if __name__ == '__main__':
    main()

 



with open("employees_data_new") as fp:
    mytable = prettytable.from_csv(fp)

print(mytable)   
help(prettytable) 

# you can define the key for sorted data in the method sorted(list, key= lambda x: x[-1] ) as a function or using lambda
# def salary(list_data):
#     return list_data[3]

   
      