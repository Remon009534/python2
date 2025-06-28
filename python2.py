#Question 1 ans
x_rows = 7
for i in range(0, x_rows = 1):
    for j in range(x_rows-i, 0, -1):
        print(j, end='')
    print('')
#Question 2 ans

input = int(input("Enter employee ID:- "))

def add_employee(inp_id,):
    employee_id = [1001, 1002, 1003, 1004, 1005]
    if inp_id in employee_id:
        return "Valid ID: ", inp_id
    else:
        return "Invalid ID"
 
print(add_employee(input))  
