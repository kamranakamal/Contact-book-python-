# 📇 Contact Book CLI Application

A clean, interactive **command-line contact manager** built with Python. This app enables you to store, view, edit, and delete contact entries with built-in **phone number and email validation**. Contact data is stored persistently in a local JSON file with automatic backup on every change.

---

## 🚀 Features

- 🔐 **Validated Inputs**
  - Email format check
  - Phone number must include country code and digits only
- 📝 **Add Contacts**
  - Store name, phone, and email
- 📋 **View Contacts**
  - Show all or select number of saved contacts
- ✏️ **Edit Contacts**
  - Update name, phone, or email with validation
- ❌ **Delete Contacts**
  - Remove by name or index with confirmation
- 💾 **Persistent Storage**
  - Automatically saves to `data.json` with `data_backup.json` created before updates
- 📎 **Simple Menu**
  - Clean terminal interface with numbered options

---

## 📦 Project Structure

```
contact-book/
├── main.py             # Main application logic
├── data.json           # Automatically generated contact storage file
├── data_backup.json    # Backup before each save
└── README.md           # Project documentation
```

---

## 🧪 Input Validation Rules

| Field     | Rule                                                                 |
|-----------|----------------------------------------------------------------------|
| **Name**  | Cannot be empty or duplicate                                         |
| **Phone** | Must start with `+` and contain 7 to 15 digits (e.g., `+919876543210`) |
| **Email** | Must follow standard email format (e.g., `user@example.com`)         |

---

## 🛠 Requirements

- Python 3.x
- No external libraries required

---

## 📥 Installation & Usage

### 1. Clone the Repository

```bash
git clone https://github.com/kamranakmal/contact-book-cli.git
cd contact-book-cli
```

### 2. Run the Application

```bash
python main.py
```

---

## 🧭 Menu Options

```
1 → Add new contact(s)
2 → Edit or delete existing contact(s)
3 → View all or some contacts
4 → Exit application
```

---

## 🗃 Example `data.json` Output

```json
[
  {
    "name": "Ayesha",
    "phone": "+917001234567",
    "email": "ayesha@example.com"
  },
  {
    "name": "Zaid",
    "phone": "+918887766554",
    "email": "zaid@example.com"
  }
]
```

---

## 📚 Learning Highlights

- File operations using `json` and `shutil`
- Regex-based input validation (`re` module)
- Clean CLI-based CRUD (Create, Read, Update, Delete) interface
- Defensive programming and exception handling
- Modular function design

---

## 🧠 Ideal For

- Python learners mastering I/O and validation
- Practicing data manipulation with JSON
- Building structured terminal applications

---

## 📜 License

This project is released under the **MIT License**.

---

## 👤 Author

**Kamran**  
GitHub: [@kamranakmal](https://github.com/kamranakmal)
