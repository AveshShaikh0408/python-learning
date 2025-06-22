def display_menu():
    print("Contact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("6. Exit")

def add_contact(contact_book):
    name = input("Enter contact name: ")
    if name in contact_book:
        print("Contact already exists!")
    else:
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        address = input("Enter address: ")
        contact_book[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        print("Contact added successfully!")
    
def view_contact(contact_book):
    name = input("Enter contact name to view: ")
    if name in contact_book:
        print(f"Name: {name.capitalize()}")
        for key, value in contact_book[name].items():
                print(f"{key.capitalize()}: {value}")
    else:
        print("Contact not found!")

def edit_contact(contact_book):
    name = input("Enter contact name to edit: ")
    if name in contact_book:
        phone = input("Enter new phone number: ")
        email = input("Enter new email address: ")
        address = input("Enter new address: ")
        contact_book[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        print("Contact updated successfully!")
    else:
        print("Contact not found!")

def delete_contact(contact_book):
    name = input("Enter contact name to delete: ")
    if name in contact_book:
        del contact_book[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

def list_all(contact_book):
    if contact_book == {}:
        print("No contacts available.")
    else:
        for key, value in contact_book.items():
            print(f"Name: {key.capitalize()}")
            for key_new, value_new in value.items():
                print(f"{key_new.capitalize()}: {value_new}")
            print()
    
def main():
    contact_book = {}
    while True:
        display_menu()
        choice = input("Enter input:")
        if choice == "1":
            add_contact(contact_book)
        elif choice == "2":
            view_contact(contact_book)
        elif choice == "3":
            edit_contact(contact_book)
        elif choice == "4":
            delete_contact(contact_book)
        elif choice == "5":
            list_all(contact_book)
        elif choice == "6":
            break
        else:
            print("Wrong choice try again!")
            
if __name__ == "__main__":
    main()