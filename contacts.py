import re
import json
import sys

#CLASSES FIRST

class contact_details: #class for the details
    def __init__(info, name, phone, email, address): #the details
        info.name = name
        info.phone = phone
        info.email = email
        info.address = address

    def __str__(info):
        return f"Name: {info.name}, Phone number: {info.phone}, Email: {info.email}, Address: {info.address}" #output details

class correct_format: #class to check if e.g phone number has 11 digits or email has @ sign etc
    def __init__(info, file_path="contacts.json"): #_init_ is for new object in class
        info.file_path = file_path #file_path parameter
        info.contacts = [] #list
        info.load_contacts() #all contacts

    def check_email(info, email): #check if email format is correct
        return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email) #(each character's meaning is in the notes file)

    def check_phone(info, phone): #check if 11 digits in phone number and no letters
        return re.match(r"^\d{11}$", phone)

    def add_contact_details(info, name, phone, email, address): #definition for adding emails #self is to call the class contact details
        if not info.check_phone(phone):
            raise ValueError("The phone number format is invalid.") #error
        if not info.check_email(email):
            raise ValueError("The email address format is invalid.") #error
        contact = contact_details(name, phone, email, address) #the details make a contact and store in the class contact_details
        info.contacts.append(contact)
        info.save_contacts()

    def remove_contact(info, name): #deleting contacts
        info.contacts = [c for c in info.contacts if c.name.lower() != name.lower()]
        info.save_contacts() #save contacts with what has been altered

    def update_contact(info, name, phone=None, email=None, address=None): #updating contacts
        for contact in info.contacts:
            if contact.name.lower() == name.lower(): #checking if details are correct 
                if phone:
                    if not info.check_phone(phone):
                        raise ValueError("Invalid phone number format.")
                    contact.phone = phone
                if email:
                    if not info.check_email(email):
                        raise ValueError("Invalid email address format.")
                    contact.email = email
                if address:
                    contact.address = address
                info.save_contacts()
                return
        raise ValueError("Contact not found.")

    def find_contacts(self, keyword): #look for that contact
        return [c for c in self.contacts if keyword.lower() in c.name.lower() or keyword in c.phone or keyword.lower() in c.email.lower()]

    def list_contacts(self): # all contacts
        return self.contacts

    def save_contacts(self): #save contacts
        with open(self.file_path, "w") as file: #w is write mode
            json.dump([contact.__dict__ for contact in self.contacts], file)

    def load_contacts(self):
        try:
            with open(self.file_path, "r") as file: #r is read mode
                self.contacts = [correct_format(data) for data in json.load(file)]
        except (FileNotFoundError, json.JSONDecodeError): #file not found or file not found in json
            self.contacts = []


#MAIN DEFINITION 

def main(): #main definition
    format = correct_format()

    while True: #while format = correct_format() is True, these are the options
        print("1.Add Contact")
        print("2.Remove Contact")
        print("3.Update Contact")
        print("4.Find Contacts")
        print("5.List Contacts")
        print("6.Exit to leave")

        choice = input("Choose an option (the number): ")

        if choice == "1": #add contact, add these details
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            try:
                format.add_contact(name, phone, email, address) #add to contacts in this order
                print("Contact added successfully.")
            except ValueError as n:
                print(n) #if error

        elif choice == "2": #remove contact
            name = input("Enter name of contact to remove: ") #only need name, then can locate
            format.remove_contact(name)
            print("Contact removed successfully.")

        elif choice == "3": #update contact
            name = input("Enter name of contact to update: ")
            phone = input("Enter new phone (leave blank to skip): ")
            email = input("Enter new email (leave blank to skip): ")
            address = input("Enter new address (leave blank to skip): ")
            try:
                format.update_contact(name, phone or None, email or None, address or None) #None if for when left blank
                print("Contact updated successfully.")
            except ValueError as n:
                print(n) #error

        elif choice == "4": #find contact
            keyword = input("Enter search keyword: ")
            results = format.find_contacts(keyword) #look up with the info they give as a clue
            if results:
                for contact in results:
                    print(contact)
            else:
                print("No contacts found")

        elif choice == "5": #list contact
            for contact in format.list_contacts(): #just output all contacts
                print(contact)

        elif choice == "6": #Exit to leave
            print("Exit")
            break

        else:
            print("Please try again") #if none of the 6 were chosen


if __name__ == "__main__": #needed so unnecessary code doesn't run
    main()
