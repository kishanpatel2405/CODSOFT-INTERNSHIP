'''
Contact Book
TASK 5
Contact Information: Store name, phone number, email, and address for each contact.
Add Contact: Allow users to add new contacts with their details.
View Contact List: Display a list of all saved contacts with names and phone numbers.
Search Contact: Implement a search function to find contacts by name or phone number.
Update Contact: Enable users to update contact details.
Delete Contact: Provide an option to delete a contact.
User Interface: Design a user-friendly interface for easy interaction
'''
import tkinter as tk
from tkinter import messagebox
import pandas as pd

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        # Create data frame
        self.contacts = pd.DataFrame(columns=["Name", "Phone", "Email", "Address"])

        # GUI components
        self.name_label = tk.Label(root, text="Name:")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(root, width=30)
        self.name_entry.grid(row=0, column=1)

        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_label.grid(row=1, column=0)
        self.phone_entry = tk.Entry(root, width=30)
        self.phone_entry.grid(row=1, column=1)

        self.email_label = tk.Label(root, text="Email:")
        self.email_label.grid(row=2, column=0)
        self.email_entry = tk.Entry(root, width=30)
        self.email_entry.grid(row=2, column=1)

        self.address_label = tk.Label(root, text="Address:")
        self.address_label.grid(row=3, column=0)
        self.address_entry = tk.Text(root, width=30, height=5)
        self.address_entry.grid(row=3, column=1)

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, columnspan=2)

        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=5, column=0, columnspan=2)

        self.search_label = tk.Label(root, text="Search:")
        self.search_label.grid(row=6, column=0)
        self.search_entry = tk.Entry(root, width=30)
        self.search_entry.grid(row=6, column=1)
        self.search_button = tk.Button(root, text="Search", command=self.search_contact)
        self.search_button.grid(row=6, column=2)

        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=7, column=0, columnspan=2)

        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=8, column=0, columnspan=2)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get("1.0", "end-1c")

        if name and phone:
            self.contacts = self.contacts.append({"Name": name, "Phone": phone, "Email": email, "Address": address}, ignore_index=True)
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please enter name and phone number.")

    def view_contacts(self):
        contact_list = self.contacts.to_string()
        messagebox.showinfo("Contact List", contact_list)

    def search_contact(self):
        search_term = self.search_entry.get()
        result = self.contacts[self.contacts.isin([search_term]).any(axis=1)]
        if not result.empty:
            messagebox.showinfo("Search Result", result.to_string())
        else:
            messagebox.showinfo("Search Result", "Contact not found.")

    def update_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get("1.0", "end-1c")

        if name:
            self.contacts.loc[self.contacts["Name"] == name, ["Phone", "Email", "Address"]] = [phone, email, address]
            messagebox.showinfo("Success", "Contact updated successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Contact not found.")

    def delete_contact(self):
        name = self.name_entry.get()
        if name:
            self.contacts = self.contacts[self.contacts["Name"]!= name]
            messagebox.showinfo("Success", "Contact deleted successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Contact not found.")

    def clear_entries(self):
        self.name_entry.delete(0, "end")
        self.phone_entry.delete(0, "end")
        self.email_entry.delete(0, "end")
        self.address_entry.delete("1.0", "end")

root = tk.Tk()
contact_book = ContactBook(root)
root.mainloop()



