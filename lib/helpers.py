from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson

def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)

def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f"Department {name} not found"
    )

def find_department_by_id():
    id_ = input("Enter the deparment's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(
        f"Department {id_} not found"
    )

def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f"Success: {department}")
    except Exception as e:
        print("Error creating department: ", e)

def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f"Success: {department}")
        except Exception as e:
            print("Error updating department: ", e)
    else:
        print(f"Department {id_} not found")

def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f"Department {id_} deleted")
    else:
        print(f"Department {id_} not found")


# You'll implement the employee functions in the lab

def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print(employee)

def find_employee_by_name():
    name = input("Enter employee's name: ")
    employee = Employee.find_by_name(name)
    print(employee) if employee else print(
        f"Employee {name} not found")

def find_employee_by_id():
    id_ = input("Enter employee's id: ")
    employee = Employee.find_by_id(id_)
    print(employee) if employee else print(
        f"Employee {id_} not found")

def create_employee():
    name = input("Enter new employee name: ")
    job = input("Enter employee's job title: ")
    department = input("Enter employee's department id: ")
    try:
        dep_id = int(department) # user input is str, need to convert to int
        employee = Employee.create(name, job, dep_id)
        print(f"Success: {employee}")
    except Exception as e:
        print("Error creating employee: ", e)

def update_employee():
    id_ = input("Enter employee's id: ")
    if employee := Employee.find_by_id(id_):
        try:
            name = input("Enter employee's new name: ")
            employee.name = name
            job = input("Enter employee's new job title: ")
            employee.job_title = job
            department = input("Enter employee's new department id: ")
            dep_id = int(department)
            employee.department_id = dep_id

            employee.update()
            print(f"Success: {employee}")
        except Exception as e:
            print("Error updating employee: ", e)
    else:
        print(f"Employee {id_} not found")

def delete_employee():
    id_ = input("Enter employee's id: ")
    if employee := Employee.find_by_id(id_):
        employee.delete()
        print(f"Employee {id_} deleted")
    else:
        print(f"Employee {id_} not found")

def list_department_employees():
    id_ = input("Enter department id: ")
    if department := Department.find_by_id(id_):
        for employee in department.employees():
            print(employee)
    else:
        print(f"Department {id_} not found")
