import json
import os
import shutil

# Load existing contacts or initialize empty list
contacts = []
if os.path.exists("data.json") and os.path.getsize("data.json") > 0:
    with open("data.json", "r") as file:
        try:
            contacts = json.load(file)
        except json.JSONDecodeError:
            print("JSON file is corrupted or invalid. Starting with empty contact list.")
            contacts = []

# Function to save contacts to file
def save_contacts():
    shutil.copy("data.json", "data_backup.json") if os.path.exists("data.json") else None
    with open("data.json", "w") as f:
        json.dump(contacts, f, indent=4)

# Function to add new contacts
def add_contact():
    try:
        add_choice = int(input("Enter number of contacts you want to add: "))
        for _ in range(add_choice):
            name = input("Enter name of contact: ").strip()
            if not name:
                print("Name cannot be empty. Skipping.")
                continue

            # Check for duplicate names
            if any(c['name'].lower() == name.lower() for c in contacts):
                print("Contact with this name already exists. Skipping.")
                continue

            phone = input("Enter the number with country code: ")
            email = input("Enter email of contact: ")

            new_contact = {
                "name": name,
                "phone": phone,
                "email": email
            }

            contacts.append(new_contact)

        save_contacts()
        print("Contacts added successfully.\n")

    except (TypeError, ValueError, KeyError):
        print("Something went wrong. Please check your input.\n")
    except Exception as e:
        print(f"Unexpected error: {e}\n")

# Function to display contacts
def view_contacts(num: int):
    if contacts:
        contacts.sort(key=lambda x: x['name'].lower())
        if num == 0:
            for idx, contact in enumerate(contacts):
                print(f"{idx+1}. Name: {contact['name']}\tPhone: {contact['phone']}\tEmail: {contact['email']}")
            print(f"\nTotal {len(contacts)} Contact(s)\n")
        else:
            for i in range(min(num, len(contacts))):
                print(f"{i+1}. Name: {contacts[i]['name']}\tPhone: {contacts[i]['phone']}\tEmail: {contacts[i]['email']}")
            print()
    else:
        print("No Contacts Available\n")

# Function to update or delete contacts
def update_contact():
    view_contacts(num=0)
    try:
        edit_choice = int(input("Enter 1 to edit and 0 to delete contacts: "))
        contact_edit = input("Enter name of contact you want to edit/delete: ").lower()

        if edit_choice == 1:
            for i in range(len(contacts)):
                if contacts[i]['name'].lower() == contact_edit:
                    contacts[i]['name'] = input("Enter Name of contact: ").strip()
                    contacts[i]['phone'] = input("Enter phone number: ")
                    contacts[i]['email'] = input("Enter email of contact: ")
                    break
            else:
                print("No contact found with that name.\n")

        elif edit_choice == 0:
            del_choice = int(input(f"Enter 1 to delete '{contact_edit}' directly or 2 to delete by index: "))
            if del_choice == 1:
                contacts[:] = [x for x in contacts if x.get('name').lower() != contact_edit]
            else:
                while True:
                    del_idx = input("Enter index of contact to delete (or press enter to exit): ")
                    if not del_idx:
                        break
                    try:
                        del contacts[int(del_idx) - 1]
                    except (IndexError, ValueError):
                        print("Invalid index.")
        else:
            print("Invalid option.\n")

        save_contacts()
        print("Contacts updated successfully.\n")

    except (TypeError, ValueError, KeyError):
        print("Something went wrong. Please check your input.\n")
    except Exception as e:
        print(f"Unexpected error: {e}\n")

# Main menu loop
if __name__ == "__main__":
    try:
        print("\n\t\t\tContact Book\t\t\t\n")
        loop_var = int(input("Enter 1 to add, 2 to edit/delete, 3 to view contacts, or 4 to exit: "))
        while loop_var != 4:
            if loop_var == 1:
                add_contact()
            elif loop_var == 2:
                update_contact()
            elif loop_var == 3:
                num = int(input("Enter 0 to view all contacts or enter number of contacts to view: "))
                view_contacts(num)
            else:
                print("Invalid option.\n")
            loop_var = int(input("Enter 1 to add, 2 to edit/delete, 3 to view, 4 to exit: "))
    except (TypeError, ValueError, KeyError):
        print("Something went wrong. Please check your input.\n")
    except Exception as e:
        print(f"Unexpected error: {e}\n")