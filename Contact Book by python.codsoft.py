import json
import os

CONTACT_FILE = 'contacts.json'


def load_contacts():
    if os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, 'r') as file:
            return json.load(file)
    return {}


def save_contacts(contacts):
    with open(CONTACT_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")
    contacts[name] = {"phone": phone, "email": email, "address": address}
    print("Contact added.")


def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}")


def search_contact(contacts):
    search_term = input("Enter name or phone number to search: ")
    found = False
    for name, details in contacts.items():
        if search_term.lower() in name.lower() or search_term in details['phone']:
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
            found = True
    if not found:
        print("No contact found.")


def update_contact(contacts):
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        phone = input(f"Enter new phone number (current: {contacts[name]['phone']}): ")
        email = input(f"Enter new email address (current: {contacts[name]['email']}): ")
        address = input(f"Enter new address (current: {contacts[name]['address']}): ")
        contacts[name] = {"phone": phone, "email": email, "address": address}
        print("Contact updated.")
    else:
        print("Contact not found.")


def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")


def main():
    contacts = load_contacts()

    while True:
        print("\nContact Management Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
            save_contacts(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
            save_contacts(contacts)
        elif choice == '5':
            delete_contact(contacts)
            save_contacts(contacts)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
