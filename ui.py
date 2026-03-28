from tkinter import *
from tkinter import messagebox
import storage
import encryption
import random
import string

class PasswordVaultUI:

    def __init__(self, window):
        self.window = window
        
       
        title_label = Label(self.window, text="🗝️ CHAMBER OF SECRETS 🗝️", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        

        Label(self.window, text="Site Name:").pack()
        self.site_entry = Entry(self.window, width=35)
        self.site_entry.pack(pady=2)
        

        Label(self.window, text="Username:").pack()
        self.user_entry = Entry(self.window, width=35)
        self.user_entry.pack(pady=2)

        
        Label(self.window, text="Password / API Key:").pack()
        self.pass_entry = Entry(self.window, width=35)
        self.pass_entry.pack(pady=2)
        
        
        self.strength_label = Label(self.window, text="Strength: -", fg="gray")
        self.strength_label.pack()
        self.pass_entry.bind("<KeyRelease>", self.check_password_strength)

        
        Button(self.window, text="🎲 Generate Password", command=self.generate_password).pack(pady=2)
        Button(self.window, text="📋 Copy Password", command=self.copy_password).pack(pady=2)

        
        Label(self.window, text="Master Key (Number):").pack()
        self.key_entry = Entry(self.window, width=35, show="*")
        self.key_entry.pack(pady=2)

        
        Button(self.window, text="[ Save Entry ]", bg="lightgreen", command=self.save_data).pack(pady=10)
        Button(self.window, text="[ Show Password ]", bg="lightblue", command=self.show_password).pack(pady=2)
        Button(self.window, text="[ Delete Entry ]", bg="salmon", command=self.delete_data).pack(pady=2)

        
        Label(self.window, text= "🔍 Search Site:").pack(pady=(15, 0))
        self.search_entry = Entry(self.window, width= 35)
        self.search_entry.pack(pady=2)
        self.search_entry.bind("<KeyRelease>", self.search_site)


        Label(self.window, text="--- Saved Accounts ---").pack(pady=(15, 0))
        self.listbox = Listbox(self.window, height=6, width=40)
        self.listbox.pack(pady=5)

        Label(self.window, text="--- Account Info ---").pack()
        self.info_text = Text(self.window, height=5, width=40, state="disabled") 
        self.info_text.pack(pady=5)

    
        self.load_listbox()
        self.load_listbox()

    def load_listbox(self):
        self.listbox.delete(0, END)
        entries = storage.load_entries()
        for entry in entries:
            self.listbox.insert(END, entry["site"])

    def save_data(self):
        site = self.site_entry.get()
        username = self.user_entry.get()
        password = self.pass_entry.get()
        key = self.key_entry.get()

        if not (site and username and password and key):
            messagebox.showwarning("Warning", "Please fill all fields!")
            return
        
        try:
            shift=int(key)
        except ValueError:
            messagebox.showerror("Error", "Master Key must be a number!")
            return
        
        encrypted_pass = encryption.encrypt_password(password, shift)
        storage.save_entry(site, username, encrypted_pass)


        self.site_entry.delete(0, END)
        self.user_entry.delete(0, END)
        self.pass_entry.delete(0, END)

        self.load_listbox()
        messagebox.showinfo("Succes", "Account saved successfully!")
    
    def show_password(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a site from the list!")
            return
        selected_site = self.listbox.get(selection[0])
        key_str = self.key_entry.get()
        try:
            shift = int(key_str)
        except ValueError:
            messagebox.showerror("Error", "Please enter your numeric Master Key to decrypt the password!")
            return
        entries = storage.load_entries()
        for entry in entries:
            if entry["site"] == selected_site:
                decrypted_pass = encryption.decrypt_password(entry["encrypted"], shift)
                self.info_text.config(state="normal")
                self.info_text.delete(1.0, END)
                info = f"Site: {entry['site']}\nUsername: {entry['username']}\nPassword: {decrypted_pass}"
                self.info_text.insert(END, info)
                self.info_text.config(state="disabled")
                break
    def delete_data(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showwarning("Warning", "Please select a site from the list to delete!")
            return
        selected_site = self.listbox.get(selection[0])
        confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete the entry for {selected_site}?")
        if confirm:
            storage.delete_entry(selected_site)
            self.load_listbox()
            self.info_text.config(state="normal")
            self.info_text.delete("1.0", END)
            self.info_text.config(state="disabled")
            messagebox.showinfo("Deleted", f"{selected_site} has been deleted from the vault.")            


    def generate_password(self):
        chars = string.ascii_letters + string.digits + "!@#$%^&*()-+"
        random_password = ''.join(random.choice(chars) for _ in range(12))
        self.pass_entry.delete(0, END)
        self.pass_entry.insert(0, random_password)
        self.check_password_strength()

    
    def copy_password(self):
        password_to_copy = self.pass_entry.get()
        if password_to_copy:
            self.window.clipboard_clear()
            self.window.clipboard_append(password_to_copy)
            messagebox.showinfo("Copied", "Password copied to clipboard!")
        else:
            messagebox.showwarning("Warning", "No password to copy!")

    
    def check_password_strength(self, event=None):
        password = self.pass_entry.get()
        
        if not password:
            self.strength_label.config(text="Password Strength: -", fg="gray")
            return
        
        has_letter = any(c.isalpha() for c in password)
        has_number = any(c.isdigit() for c in password)
        has_special = any(c in "!@#$%^&*()-+" for c in password)
        if len(password) < 6:
            self.strength_label.config(text="Password Strength: Weak", fg="red")
        elif len(password) >=8 and has_letter and has_number and has_special:
            self.strength_label.config(text="Password Strength: Strong", fg="green")
        else:
            self.strength_label.config(text="Password Strength: Medium", fg="orange")

    
    def search_site(self, event=None):
        search_term = self.search_entry.get().lower()
        self.listbox.delete(0, END)

        entries = storage.load_entries()

        for entry in entries:
            if search_term in entry["site"].lower():
                self.listbox.insert(END, entry["site"])





