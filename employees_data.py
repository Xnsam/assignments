def cal_max(employees):
  """Function to calculate the max of the employee salary and print the data."""
  emp_max_salary = max([i['salary'] for i in employees])
  return [i for i in employees if i['salary'] == emp_max_salary]

def cal_min(employees):
  """Function to calculate the min of the employee salary and print the data."""
  emp_min_salary = min([i['salary'] for i in employees])
  return [i for i in employees if i['salary'] == emp_min_salary]

def cal_avg(designation, employees):
  """Function to calculate average as per the designation."""
  t = [emp['salary'] for emp in employees if emp['designation'] == designation]
  return sum(t) / len(t)
  
  
def get_employees(num_of_employees):
  """Function to get the number of employees."""
  employees = []
  for n in range(num_of_employees):
    emp = {}
    emp['name'] = input("Enter name of employee: \t")
    emp['salary'] = float(input("Enter salary of employee: \t"))
    emp['designation'] = input("Enter the designation of employee: \t")
    emp['tenure'] = input("Enter the tenure of the employee: \t")
    employees.append(emp)
  return employees
  
  
  import pprint

num_of_employees = int(input("Enter number of employees: \t"))
employees = get_employees(num_of_employees)

print('-------------- Employees')
pprint.pprint(employees)

designation = input("Enter designation of employee: \t")


print('-------------- Average Salary as per designation')
print(cal_avg(designation, employees))

print('-------------- Min Salary')
print(cal_min(employees))

print('-------------- Max Salary')
print(cal_max(employees))
