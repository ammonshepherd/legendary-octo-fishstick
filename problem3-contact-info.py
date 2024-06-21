'''
Program requirements:
Write a program that creates a contact list for which you keep:
    Name
    Phone number
    Email address
    Physical address
For the name and physical address use appropriate variables that would allow you to have distinctive values for first and last name associate with name, and street, city, state and zip code for the physical address.

In the test program, enter data for three to five people, and display:
    Table with their complete information
    Table with phone numbers
    Given a name, display phone number
    Given a first name, display the full address
    Display the cities and states of all people
'''
# Generate four people and their info as dictionaries
person1 = {
    "first": "Billy",
    "last": "Johns",
    "phone": "555-555-5555",
    "email": "billy@bob.com",
    "street": "1200 Place",
    "city": "Citytown",
    "state": "AZ",
    "zip": "28803"
}
person2 = {
    "first": "Margaret",
    "last": "Oscarson",
    "phone": "444-444-4444",
    "email": "jill@jane.com",
    "street": "3200 Street",
    "city": "Citytown",
    "state": "FL",
    "zip": "88903"
}
person3 = {
    "first": "Susan",
    "last": "Anthony",
    "phone": "222-222-2222",
    "email": "susan@usa.com",
    "street": "8210 Ave",
    "city": "Township",
    "state": "PA",
    "zip": "18491"
}
person4 = {
    "first": "Garth",
    "last": "Williams",
    "phone": "777-777-7777",
    "email": "garth@sup.com",
    "street": "72201 Boulevard",
    "city": "Cityplace",
    "state": "NY",
    "zip": "38990"
}

# put the people into a list
contact_list = [person1, person2, person3, person4]

# function to print out all info for every person
def print_all(contacts):
    print(f'{"Name":<20} {"Phone":<20} {"Email":<20} {"Address":<20}')
    print(f'{"-":-<15} {" ": <4} {"-":-<15} {" ": <4} {"-":-<15} {" ": <4} {"-":-<15} ')
    for c in contacts:
        name = f"{c['first']} {c['last']}"
        print(f"{name:<20} {c['phone']:<20} {c['email']:<20} {
              c['street']} {c['city']}, {c['state']} {c['zip']}")

# Given a list, print out the phone numbers
def phone_nums(contacts):
    print(f'{"Phone Numbers":<20}')
    print(f'{"-":-<15}')
    for c in contacts:
        print(f'{c['phone']}')
        
# Given a name and the contact list
# print out the phone number
def get_phone(name, contacts):
    for c in contacts:
        full_name = f'{c['first']} {c['last']}'
        if name == full_name:
            print(f'{full_name} Phone: ', end='')
            print(c['phone'])

# Given a name and the contact list
# print out the address
def get_address(name, contacts):
    print(f'{name} Address: ', end='')
    for c in contacts:
        if name == c['first']:
            print(f'{c['street']} {c['city']}, {c['state']} {c['zip']}')
    
# Call the functions to generate the outputs
print_all(contact_list)
print()
phone_nums(contact_list)
print()
get_phone("Garth Williams", contact_list)
print()
get_address("Garth", contact_list)