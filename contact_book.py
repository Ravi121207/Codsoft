contacts = {}

def add_contact():
    name = input("Enter name: ")
    if name in contacts:
        print("Contact already exists.")
        return
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
    print("Contact added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts available.")
        return
    print("\nContact List:")
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}")

def view_contact_detail():
    name = input("Enter contact name to view: ")
    contact = contacts.get(name)
    if contact:
        print(f"\nName: {name}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Address: {contact['address']}")
    else:
        print("Contact not found.")

def search_contact():
    key = input("Enter name or phone number to search: ")
    found = False
    for name, details in contacts.items():
        if key.lower() in name.lower() or key in details['phone']:
            print(f"\nName: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            found = True
    if not found:
        print("No matching contact found.")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        print("Leave field blank to keep current value.")
        phone = input("Enter new phone number: ") or contacts[name]['phone']
        email = input("Enter new email: ") or contacts[name]['email']
        address = input("Enter new address: ") or contacts[name]['address']
        contacts[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

while True:
    print("\nContact Book")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. View Contact Details")
    print("4. Search Contact")
    print("5. Update Contact")
    print("6. Delete Contact")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        view_contact_detail()
    elif choice == "4":
        search_contact()
    elif choice == "5":
        update_contact()
    elif choice == "6":
        delete_contact()
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")    