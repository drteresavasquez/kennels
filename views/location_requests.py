import sqlite3
import json
from models import Location, Employee, Animal, Customer

def get_all_locations():
    # Open a connection to the database
    with sqlite3.connect("./kennel.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            l.id,
            l.name,
            l.address
        FROM Location l
        """)

        # Initialize an empty list to hold all animal representations
        locations = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            location = Location(row['id'], row['address'], row['name'])

            locations.append(location.__dict__)

    return locations

# Function with a single parameter
def get_single_location(id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            l.id,
            l.name,
            l.address
        FROM Location l
        WHERE l.id = ?
        """, ( id, ))
        
        # Load the single result into memory
        data = db_cursor.fetchone()
        location = Location(data['id'], data['address'], data['name'])
        
        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.address,
            e.location_id
        FROM Employee e
        WHERE e.location_id = ?
        """, ( id, ))

        employees = []
        
        employees_data = db_cursor.fetchall()

        for row in employees_data:
            employee = Employee(row['id'], row['name'], row['location_id'], row['address'])
            employees.append(employee.__dict__)

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.status,
            a.breed,
            a.customer_id,
            a.location_id,
            c.name customer_name,
            c.address customer_address,
            c.email customer_email
        FROM Animal a
        JOIN Customer c
            ON c.id = a.customer_id
        WHERE a.location_id = ?
        """, ( id, ))

        animals = []
        
        animals_data = db_cursor.fetchall()

        for row in animals_data:
            animal = Animal(row['id'], row['name'], row['breed'],
                            row['status'], row['location_id'],
                            row['customer_id'])
            customer = Customer(row['id'], row['customer_name'], row['customer_address'], row['customer_email'])
            animal.customer = customer.__dict__
            animals.append(animal.__dict__)

        location.employees = employees
        location.animals = animals
        return location.__dict__

# def create_location(location):
#     max_id = LOCATIONS[-1]["id"]
#     new_id = max_id + 1
#     location["id"] = new_id
#     LOCATIONS.append(location)

#     return location

# def delete_location(id):
#     location_index = -1

#     for index, location in enumerate(LOCATIONS):
#         if location["id"] == id:
#             location_index = index

#     if location_index >= 0:
#         LOCATIONS.pop(location_index)

# def update_location(id, new_location):
#     for index, location in enumerate(LOCATIONS):
#         if location["id"] == id:
#             LOCATIONS[index] = new_location
#             break
