# print(open("emps_data.txt").read())
# This code reads the contents of a file named "emps_data.txt" and prints it to the console.
# The file is expected to contain employee data, and the code will display that data when executed.
# The file should be in the same directory as this script for it to work correctly.
# The code uses the built-in `open` function to open the file in read mode and the `read` method to read its contents.
# The `print` function is then used to display the contents of the file.
# Make sure to handle exceptions in a real-world scenario to avoid errors if the file does not exist or is inaccessible.
# Note: This code does not include any error handling, so if the file does not exist or cannot be read, it will raise an exception.
# The code is a simple demonstration of file I/O in Python.
f = open("emps_data.txt")
print(f.readlines())
