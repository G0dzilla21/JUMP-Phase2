import json
import employee as emp
import _prompts as pr
import exceptions as exc
import filters as filter


# Method used for fetching and then displaying list of employees from employees.json by Adeel
def displayEmployeeList():
    # Loads employee details from relevant file
    with open('employees.json', 'rt') as file:
        data = json.load(file)

    for key, value in data.items():
        if (key != "0"):
            print(f"-----Employee Number {key}-----\n")
            currentEmployee = emp.Employee(value["First Name"], value["Last Name"], value["Age"], value["Birth"], value["Employee ID"], value["Employment Date"], value["Department"], value["Salary"], value["Email"])
            currentEmployee.toString()


# Method used for adding employee to employees.json by Cody
def addEmployee():   
    
    addEmployee = True
    while addEmployee:
        first_name = pr.get_first_name()
        last_name = pr.get_last_name()
        age = pr.get_age()
        dob = pr.get_dob()
        emp_id = generateId()
        emp_date = pr.get_emp_date()
        department = pr.get_department()
        salary = pr.get_salary()
        email = generateEmail(first_name, last_name, dob, emp_id)
        emp_info = {
            "First Name": first_name.title(),
            "Last Name": last_name.title(),
            "Age": age,
            "Birth": dob,
            "Employee ID": emp_id,
            "Employment Date": emp_date,
            "Department": department.title(),
            "Salary": str(salary),
            "Email": email
                    }

        with open('employees.json', 'rt') as file:
            data = json.load(file)

        data[emp_id] = emp_info
        
        with open('employees.json', 'w') as file:
            json.dump(data, file, indent=4)
        
        print("\nEmployee Added!")

        addEmployee = pr.repeat_action()

# Method used for generating unique email based on employee name, date of birth and id by Cody
def generateEmail(first_name, last_name, dob, emp_id):
    email = f"{first_name}.{last_name}{dob[-2:]}{emp_id}@cognixia.com"
    return email

# Method used for generating unique employee id by reference of employees.json by Adeel
def generateId():
    employeeIdPlaceholder = None

    with open('employees.json', 'rt') as file:
        data = json.load(file)

    employeeIdPlaceholder = data["0"]
    data["0"] = employeeIdPlaceholder + 1

    with open('employees.json', 'w') as file:
        json.dump(data, file, indent=4)

    return employeeIdPlaceholder + 1

# Method used for updating Employee data in employees.json by Adeel
def updateEmployeeAttribute(emp_id, attribute, value):
    
    with open('employees.json', 'rt') as file:
        data = json.load(file)

    data[str(emp_id)][attribute] =  value

    with open('employees.json', 'w') as file:
        json.dump(data, file, indent=4)
    
# Method used for updating Employee email in employees.json when employee name or date of birth is changed by Adeel
def updateEmail(emp_id):
    
    with open('employees.json', 'rt') as file:
        data = json.load(file)

    data[str(emp_id)]["Email"] = generateEmail(data[str(emp_id)]["First Name"], data[str(emp_id)]["Last Name"], data[str(emp_id)]["Birth"], data[str(emp_id)]["Employee ID"])

    with open('employees.json', 'w') as file:
        json.dump(data, file, indent=4)

# Method used for updating employee data
def updateEmployeeData():
    updateEmployee = True
    employeeID = input("Please enter the Employee Id of the Employee you wish to update: ")

    with open('employees.json', 'rt') as file:
        data = json.load(file)
    
    employeeFound = False
    for key, value in data.items():
        if (employeeID == key and employeeID != "0"):
            employeeFound = True

    if (employeeFound == False):
        exc.EmployeeNotFound()
        updateEmployee = False

    while updateEmployee:
        print(f"You may update the following:\n1 First Name \n2 Last Name\n3 Age\n4 Birth\n5 Employment Date\n6 Department\n7 Salary\n")
        updateField = input(f"What would you like to update for this employee? ")
        match updateField.title():
            case "First Name":
                updateEmployeeAttribute(employeeID, "First Name", pr.get_first_name())
                updateEmail(employeeID)
                print("\nEmployee First Name Updated!")
            case "Last Name":
                updateEmployeeAttribute(employeeID, "Last Name", pr.get_last_name())
                updateEmail(employeeID)
                print("\nEmployee Last Name Updated!")
            case "Age":
                updateEmployeeAttribute(employeeID, "Age", int(pr.get_age()))
                print("\nEmployee Age Updated!")
            case "Birth":
                updateEmployeeAttribute(employeeID, "Birth", pr.get_dob())
                updateEmail(employeeID)
                print("\nEmployee Date of Birth Updated!")
            case "Employment Date":
                updateEmployeeAttribute(employeeID, "Employment Date", pr.get_emp_date())
                print("\nEmployee Employment Date Updated!")
            case "Department":
                updateEmployeeAttribute(employeeID, "Department", pr.get_department())
                print("\nEmployee Department Updated!")
            case "Salary":
                updateEmployeeAttribute(employeeID, "Salary", str(pr.get_salary()))
                print("\nEmployee Salary Updated!")
            case _:
                print("Invalid employee field choice. Please choose an appropriate field to update.")

        updateEmployee = pr.repeat_action()


# Method used for removing employees from employees.json by Senthu
def removeEmployee():    
    removeEmployee = True
    while removeEmployee:
        emp_id = input("Please enter the Employee ID for the employee you wish to remove: ")
        
        with open('employees.json', 'rt') as file:
            data = json.load(file)
        
        employeeFound = False
        for key, value in data.items():
            if (emp_id == key and emp_id != "0"):
                employeeFound = True
        
        if (employeeFound):
            del data[emp_id]
        else:
            exc.EmployeeNotFound()

        try:
            with open('employees.json', 'w') as file:
                json.dump(data, file, indent=4)
        except:
            raise exc.FileNotFound()
        
        print("\nEmployee Removed!")
        removeEmployee = pr.repeat_action()


# Method used for filtering employees and displaying them by using functions in filters.py by Adeel
def filterEmployee():
    filterEmployee = True
    while filterEmployee:
        print(f"You may filter Employees in the following ways:\n1: Name \n2: Age\n3: Birth (By Year)\n4: Employment Date (By Year)\n5: Department\n6: Salary\n7: Exit")
        filterType = input(f"How would you like to filter Employees: ")
        match filterType.title():
            case "Name" | "1":
                filter.filterByName()
            case "Age" | "2":
                filter.filterByAge()
            case "Birth" | "3":
                filter.filterByBirth()
            case "Employment Date" | "4":
                filter.filterByEmploymentDate()
            case "Department" | "5":
                filter.filterByDepartment()
            case "Salary" | "6":
                filter.filterBySalary()
            case "Exit" | "7":
                break
            case _:
                print("Invalid employee field choice. Please choose an appropriate field to update.")

        filterEmployee = pr.repeat_action()