EMPLOYEES = [
    {
        "id": 1,
        "name": "Jenna Solis"
    },
    {
        "id": 2,
        "name": "Dr. T"
    },

]

def get_all_employees():
    """GET all employees"""
    return EMPLOYEES

def get_single_employee(id):
    """GET single employee"""
    req_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            req_employee = employee

    return req_employee

def create_employee(employee):
    max_id = EMPLOYEES[-1]["id"]
    new_id = max_id + 1
    employee["id"] = new_id

    EMPLOYEES.append(employee)

    return employee

def delete_employee(id):
    employee_index = -1

    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            employee_index = index

    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)

def update_employee(id, new_employee):
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            EMPLOYEES[index] = new_employee
            break
