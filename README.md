# Password Manager 🔐

A secure and user-friendly desktop application built with Python's Tkinter that helps you generate, store, and retrieve website passwords with peace of mind.

## 📝 Description

Password Manager is an intuitive desktop tool designed to solve the problem of remembering multiple complex passwords. The application allows you to generate strong random passwords, store them securely with Base64 encoding, and retrieve them whenever needed - all through a clean, simple interface.

## 🔑 Key Features

**Strong Password Generation**: Create randomized passwords with letters, numbers, and symbols
**Secure Storage**: Save credentials with Base64 encoding to prevent casual viewing
**Quick Retrieval**: Look up passwords by website name
**User-Friendly Interface**: Clean Tkinter GUI with clear labels and buttons
**Password Update**: Automatically updates existing entries when details change

## 🛠️ Prerequisites

Before running the application, make sure you have:

* Python 3.x installed
* Tkinter module (comes with Python standard library)
* Base64 module (comes with Python standard library)

## 📦 Installation

1. Clone the repository
```bash
git clone https://github.com/dbeniamin/Password-Manager.git
cd password-manager
```

2. Make sure the program files are in your directory:
   * `password_manager.py` (main application file)
   * `logo.png` (application logo)

3. Run the application:
```bash
python password_manager.py
```

## 🎯 How to Use

### Generate a Password
1. Enter the website / app name
2. Ensure your email / user name is correct
3. Click "Generate Password"
4. A strong random password will appear in the password field

### Save a Password
1. Enter the website name
2. Verify your email / username
3. Enter a password or use the generated one
4. Click "Add" to save

### Retrieve a Password
1. Enter the website name
2. Click "Show Password"
3. The password will appear in the password field

### Update a Password
1. Enter an existing website
2. Enter your email / user name
3. Generate or enter a new password
4. Click "Add" to update

## 💻 Creating an Executable
To convert the Python script into a standalone Windows executable (.exe) file:

1. Install PyInstaller:
```bash
pip install pyinstaller
```

2. Create the executable:
```bash
pyinstaller --onefile --windowed --add-data "logo.png;." password_manager.py
```

3. Find your executable in the `dist` folder
4. The executable can be shared with users who don't have Python installed

> **Note**: Make sure to include the logo.png file in the same directory as your executable or update the file path in the code accordingly.

## 🔒 Security Features

* Passwords are encoded using Base64 before storing
* Data is saved locally in `data.txt` in an obscured format
* No plain text passwords visible when viewing the data file

## 📄 File Structure

```
password-manager/
│
├── password_manager.py         # Main application file
├── logo.png                    # Application logo
├── data.txt                    # Encoded password storage (created on first use)
└── README.md                   # This file
```

## ⚙️ Technical Details

* Built with Python's Tkinter for the graphical interface
* Uses Base64 encoding from the standard library
* Stores data in a simple text file with "|" delimiters
* Implements error handling for file operations

## ⚠️ Known Limitations
* 🔑 No master password protection for the application itself
* 💻 Local storage only - no cloud synchronization

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Contact

If you have any questions or suggestions, please open an issue on this repository.

---

Made with ❤️ for everyone who's tired of using "password123" everywhere.
