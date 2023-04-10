CUSTOMERS = [
    {
        "id": 1,
        "name": "Ryan Tanay"
    }
]

def get_all_customers():
    """GET all customers"""
    return CUSTOMERS

def get_single_customer(id):
    """Return single customer by id"""
    req_customer = None

    for customer in CUSTOMERS:
        if customer["id"] == id:
            req_customer = customer

    return req_customer

def create_customer(customer):
    # Get the id value of the last animal in the list
    max_id = CUSTOMERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    customer["id"] = new_id

    # Add the animal dictionary to the list
    CUSTOMERS.append(customer)

    # Return the dictionary with `id` property added
    return customer

def delete_customer(id):
    customer_index = -1

    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            customer_index = index

    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)

def update_customer(id, new_customer):
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            CUSTOMERS[index] = new_customer
            break
