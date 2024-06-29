# Contact Book

contact_book = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact_book[name] = {"phone": phone, "email": email, "address": address}
    print("Contact added successfully!")

def view_contacts():
    if not contact_book:
        print("No contacts found!")
    else:
        for name, details in contact_book.items():
            print(f"{name} - {details['phone']}")

def search_contact():
    search_term = input("Enter name or phone number to search: ")
    for name, details in contact_book.items():
        if search_term in [name, details["phone"]]:
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
            return
    print("Contact not found!")

def update_contact():
    search_term = input("Enter name to update: ")
    if search_term in contact_book:
        contact_book[search_term]["phone"] = input("Enter new phone number: ")
        contact_book[search_term]["email"] = input("Enter new email: ")
        contact_book[search_term]["address"] = input("Enter new address: ")
        print("Contact updated successfully!")
    else:
        print("Contact not found!")

def delete_contact():
    search_term = input("Enter name to delete: ")
    if search_term in contact_book:
        del contact_book[search_term]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again!")