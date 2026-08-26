# CODSOFT Python Programming Internship
# Task 5 - Contact Book

contacts = {}


def add_contact():
    name = input("Enter name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()

    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }

    print("Contact added successfully.")


def view_contacts():
    if not contacts:
        print("\nNo contacts available.")
        return

    print("\n========== CONTACT LIST ==========")

    for name, details in contacts.items():
        print(f"\nName    : {name}")
        print(f"Phone   : {details['phone']}")
        print(f"Email   : {details['email']}")
        print(f"Address : {details['address']}")


def search_contact():
    search = input("Enter name or phone number to search: ").strip().lower()

    found = False

    for name, details in contacts.items():
        if (
            search in name.lower()
            or search in details["phone"].lower()
        ):
            print("\nContact Found")
            print(f"Name    : {name}")
            print(f"Phone   : {details['phone']}")
            print(f"Email   : {details['email']}")
            print(f"Address : {details['address']}")
            found = True

    if not found:
        print("Contact not found.")


def update_contact():
    name = input("Enter contact name to update: ").strip()

    if name not in contacts:
        print("Contact not found.")
        return

    print("\nEnter new details:")

    phone = input("Enter new phone number: ").strip()
    email = input("Enter new email: ").strip()
    address = input("Enter new address: ").strip()

    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }

    print("Contact updated successfully.")


def delete_contact():
    name = input("Enter contact name to delete: ").strip()

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")


def main():
    while True:
        print("\n==============================")
        print("        CONTACT BOOK")
        print("==============================")

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
            print("Thank you for using Contact Book.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()