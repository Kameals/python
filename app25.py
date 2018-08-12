# Reading Files


# r : read
# w : write
# a : append
# r+ :

employee_file = open("employees.txt", "r")
for employee in employee_file.readlines():
    print(employee)

employee_file.close()

