# 🗝️ Chamber of Secrets (Password Vault)

A highly secure, locally encrypted, and feature-rich desktop password manager built with Python and Tkinter. This application allows users to safely store, manage, and retrieve their passwords using a single Master Key.

## 🚀 Features

* **Advanced Encryption:** Uses `cryptography.fernet` to encrypt all saved passwords. Even if someone accesses your database file, they cannot read your passwords without your Master Key.
* **Master Key Protection:** A single, memorable number is required to save, view, or delete entries.
* **🎲 Random Password Generator:** Instantly generates strong, complex, 12-character passwords with a single click.
* **🛡️ Live Password Strength Checker:** Automatically evaluates your password as Weak, Medium, or Strong while you type.
* **🔍 Live Search Bar:** Quickly filter through your saved accounts in real-time by typing the site name.
* **📋 1-Click Copy:** Easily copy your generated or saved passwords to the clipboard.
* **100% Offline & Local:** No cloud servers. Your encrypted vault stays only on your computer for maximum privacy.

## 🛠️ Technologies Used

* **Python 3**
* **Tkinter** (Graphical User Interface)
* **Cryptography / Fernet** (Symmetric Encryption)

## ⚙️ How to Run

1. Clone this repository to your local machine.
2. Install the required cryptography library if you haven't already:
   ```bash
   pip install cryptography
Run the application:

Bash
python main.py
🔒 Security Note
This project uses a .gitignore file to ensure that the vault.txt (which contains the encrypted passwords) is never uploaded to GitHub. Your data remains completely private
