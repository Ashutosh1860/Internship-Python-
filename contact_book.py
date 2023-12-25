import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        self.contacts = []

        # GUI Elements
        self.label_name = tk.Label(root, text="Name:")
        self.label_phone = tk.Label(root, text="Phone:")
        self.label_email = tk.Label(root, text="Email:")
        self.label_address = tk.Label(root, text="Address:")

        self.entry_name = tk.Entry(root)
        self.entry_phone = tk.Entry(root)
        self.entry_email = tk.Entry(root)
        self.entry_address = tk.Entry(root)

        self.btn_add = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.btn_view = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.btn_search = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.btn_update = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.btn_delete = tk.Button(root, text="Delete Contact", command=self.delete_contact)

        # Grid placement
        self.label_name.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
        self.label_phone.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
        self.label_email.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
        self.label_address.grid(row=3, column=0, padx=10, pady=5, sticky=tk.E)

        self.entry_name.grid(row=0, column=1, padx=10, pady=5)
        self.entry_phone.grid(row=1, column=1, padx=10, pady=5)
        self.entry_email.grid(row=2, column=1, padx=10, pady=5)
        self.entry_address.grid(row=3, column=1, padx=10, pady=5)

        self.btn_add.grid(row=4, column=0, columnspan=2, pady=10)
        self.btn_view.grid(row=5, column=0, columnspan=2, pady=5)
        self.btn_search.grid(row=6, column=0, columnspan=2, pady=5)
        self.btn_update.grid(row=7, column=0, columnspan=2, pady=5)
        self.btn_delete.grid(row=8, column=0, columnspan=2, pady=5)

    def add_contact(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        email = self.entry_email.get()
        address = self.entry_address.get()

        if name and phone:
            contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
            self.contacts.append(contact)
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showerror("Error", "Name and Phone are required fields.")

    def view_contacts(self):
        if self.contacts:
            contact_list = "\n".join([f"{contact['Name']}: {contact['Phone']}" for contact in self.contacts])
            messagebox.showinfo("Contacts", contact_list)
        else:
            messagebox.showinfo("Contacts", "No contacts found.")

    def search_contact(self):
        search_term = simpledialog.askstring("Search Contact", "Enter name or phone number:")
        if search_term:
            results = []
            for contact in self.contacts:
                if (search_term.lower() in contact["Name"].lower()) or (search_term in contact["Phone"]):
                    results.append(contact)
            if results:
                contact_list = "\n".join([f"{result['Name']}: {result['Phone']}" for result in results])
                messagebox.showinfo("Search Results", contact_list)
            else:
                messagebox.showinfo("Search Results", "No matching contacts found.")
        else:
            messagebox.showinfo("Search Contact", "Please enter a search term.")

    def update_contact(self):
        search_term = simpledialog.askstring("Update Contact", "Enter name or phone number:")
        if search_term:
            for contact in self.contacts:
                if (search_term.lower() in contact["Name"].lower()) or (search_term in contact["Phone"]):
                    # Update contact details
                    contact["Name"] = simpledialog.askstring("Update Contact", "Enter new name:", initialvalue=contact["Name"])
                    contact["Phone"] = simpledialog.askstring("Update Contact", "Enter new phone number:", initialvalue=contact["Phone"])
                    contact["Email"] = simpledialog.askstring("Update Contact", "Enter new email:", initialvalue=contact.get("Email", ""))
                    contact["Address"] = simpledialog.askstring("Update Contact", "Enter new address:", initialvalue=contact.get("Address", ""))
                    messagebox.showinfo("Success", "Contact updated successfully!")
                    break
            else:
                messagebox.showinfo("Update Contact", "No matching contact found.")
        else:
            messagebox.showinfo("Update Contact", "Please enter a search term.")

    def delete_contact(self):
        search_term = simpledialog.askstring("Delete Contact", "Enter name or phone number:")
        if search_term:
            for contact in self.contacts:
                if (search_term.lower() in contact["Name"].lower()) or (search_term in contact["Phone"]):
                    self.contacts.remove(contact)
                    messagebox.showinfo("Success", "Contact deleted successfully!")
                    break
            else:
                messagebox.showinfo("Delete Contact", "No matching contact found.")
        else:
            messagebox.showinfo("Delete Contact", "Please enter a search term.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
