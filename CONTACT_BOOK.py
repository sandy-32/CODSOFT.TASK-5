contact = {}

def display_contact():
    print("name\t\tnumber_email___address")
    for name, details in contact.items():
        phone_number, email, address = details
        print(f"{name}\t\t {phone_number}  {email}  {address}")

while True:
    choice = int(input('1. Add new contact \n2. Search contact \n3. Display contacts\n4. Edit contact\n5. Delete contact\n6. Exit\nEnter your choice: '))
    
    if choice == 1:
        name = input('Enter the contact name: ')
        phone_number = int(input('Enter the contact number: '))
        email = input('Enter the email: ')
        address = input('Enter the city you live in: ')
        contact[name] = (phone_number, email, address)

    elif choice == 2:
        search_name = input('Enter contact name to search: ')
        if search_name in contact:
            print(f"{search_name}'s contact details are: {contact[search_name]}")
        else:
            print('No contact found!')

    elif choice == 3:
        if not contact:
            print('Empty contact book!')
        else:
            display_contact()

    elif choice == 4:
        edit_contact = input('Enter the contact name to edit: ')
        if edit_contact in contact:
            phone_number = int(input('Enter new mobile number: '))
            email = input('Enter new email: ')
            address = input('Enter new address: ')
            contact[edit_contact] = (phone_number, email, address)
            print('Contact updated.')
            display_contact()
        else:
            print('No contact found!')

    elif choice == 5:
        del_contact = input('Enter the contact name to delete: ')
        if del_contact in contact:
            confirm = input('Do you want to delete this contact? (YES/NO) ').capitalize()
            if confirm == 'YES':
                del contact[del_contact]
                print(f"Contact {del_contact} deleted.")
            display_contact()
        else:
            print("Name is not found in the contacts book.")

    elif choice == 6:
        break

    else:
        print("Invalid choice! Please enter a valid option.")
