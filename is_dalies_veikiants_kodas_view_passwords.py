import random
import string
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import os
from tkinter import messagebox, scrolledtext, filedialog


# Random password generation code with some functions which will be written below
class PasswordGeneratorApp:
    def __init__(self, master):
        self.root = master
        self.root.title("Password Generator")
        self.passwords = []

        # GUI elements for password generation
        self.length_label = Label(root, text="Password Length:")
        self.length_label.grid(row=0, column=0, padx=10, pady=10)

        self.length_entry = Entry(root)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)

        self.use_uppercase_var = BooleanVar()
        self.use_uppercase_var.set(True)  # Set the initial value of the checkbox
        self.use_uppercase_checkbox = Checkbutton(root, text="Uppercase Letters", variable=self.use_uppercase_var)
        self.use_uppercase_checkbox.grid(row=1, column=1, padx=10, pady=10)

        self.use_lowercase_var = BooleanVar()
        self.use_lowercase_var.set(True)  # Set the initial value of the checkbox
        self.use_lowercase_checkbox = Checkbutton(root, text="Lowercase Letters", variable=self.use_lowercase_var)
        self.use_lowercase_checkbox.grid(row=2, column=1, padx=10, pady=10)

        self.use_numbers_var = BooleanVar()
        self.use_numbers_var.set(True)  # Set the initial value of the checkbox
        self.use_numbers_checkbox = Checkbutton(root, text="Numbers", variable=self.use_numbers_var)
        self.use_numbers_checkbox.grid(row=3, column=1, padx=10, pady=10)

        self.use_symbols_var = BooleanVar()
        self.use_symbols_var.set(True)  # Set the initial value of the checkbox
        self.use_symbols_checkbox = Checkbutton(root, text="Symbols", variable=self.use_symbols_var)
        self.use_symbols_checkbox.grid(row=4, column=1, padx=10, pady=10)

        self.use_view_passwords_var = BooleanVar()
        self.use_view_passwords_var.set(False)  # Set the initial value of the checkbox
        self.use_view_passwords_checkbox = Checkbutton(root, text="View Passwords",
                                                       variable=self.use_view_passwords_var)
        self.use_view_passwords_checkbox.grid(row=1, column=3, padx=10, pady=10)
        self.use_view_passwords_var.trace("w", lambda *args: self.view_passwords())

        self.generate_button = Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        self.generate_multiple_button = Button(root, text="Generate 5 Passwords",
                                               command=self.generate_multiple_passwords)
        self.generate_multiple_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        self.clear_button = Button(root, text="Clear Passwords", command=self.clear_passwords)
        self.clear_button.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

        self.save_button = Button(root, text="Save Passwords to File", command=self.save_passwords_to_file)
        self.save_button.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

        self.output_text = scrolledtext.ScrolledText(root, wrap=WORD, width=100, height=20)
        self.output_text.grid(row=0, column=2, rowspan=10, padx=10, pady=10)

        self.max_length_label = Label(root, text="Recommended maximum character length: 90")
        self.max_length_label.grid(row=0, column=2, padx=10, pady=5)

        # Set the background color of the output_text widget
        self.output_text.configure(bg="lightyellow1")

        # Create the image panel on the right side
        img = Image.open(os.path.join(r"C:\Users\User\Desktop\TEST", "pic.png"))
        resized_img = img.resize((200, 200))  # Resize the image to desired dimensions
        self.img = ImageTk.PhotoImage(resized_img)
        self.panel = Label(master, image=self.img)
        # Use grid layout to position the image panel
        self.panel.grid(row=0, column=3, padx=10, pady=10)

    # Password generation with its functionality
    def generate_password(self):
        # Get user input for password generation
        length_str = self.length_entry.get()

        # Check if password length is provided and is a valid number
        if not length_str:
            messagebox.showerror("HEY, HEY, HEY", "Looks like you forgot to write down password length. "
                                                  "Please would you be kindly, enter a password length.")
            return
        if not length_str.isdigit():
            messagebox.showerror("HEY, HEY, HEY", "I accept only numbers. Enter a valid numeric password length.")
            return

        length = int(length_str)
        use_uppercase = self.use_uppercase_var.get()
        use_numbers = self.use_numbers_var.get()
        use_lowercase = self.use_lowercase_var.get()
        use_symbols = self.use_symbols_var.get()

        characters = ""
        if use_uppercase:
            characters += string.ascii_uppercase
        if use_lowercase:
            characters += string.ascii_lowercase
        if use_numbers:
            characters += string.digits
        if use_symbols:
            characters += string.punctuation

        # Check if password has any character type was chosen
        if not characters:
            messagebox.showerror("HEY, HEY, HEY", "What do you expect me to do? Select at least one character type: "
                                                  "uppercase, lowercase, numbers, or symbols.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        self.passwords.append(password)
        self.output_text.insert(tk.END, password + "\n")

    # Generate multiple passwords functionality, count can be modified
    def generate_multiple_passwords(self):
        # Generate 5 passwords using the generate_password method, modify count to change quantity generated passwords
        count = 5
        length_str = self.length_entry.get()
        # Check if password has a valid number
        if not length_str or not length_str.isdigit():
            messagebox.showerror("HEY, HEY, HEY", "I accept only numbers. Enter a valid numeric password length.")
            return

        length = int(length_str)
        use_uppercase = self.use_uppercase_var.get()
        use_lowercase = self.use_lowercase_var.get()
        use_numbers = self.use_numbers_var.get()
        use_symbols = self.use_symbols_var.get()

        characters = ""
        if use_uppercase:
            characters += string.ascii_uppercase
        if use_lowercase:
            characters += string.ascii_lowercase
        if use_numbers:
            characters += string.digits
        if use_symbols:
            characters += string.punctuation
        # Check if password has any character type was chosen
        if not characters:
            messagebox.showerror("HEY, HEY, HEY", "What do you expect me to do? Select at least one character type: "
                                                  "uppercase, lowercase, numbers, or symbols.")
            return

        for _ in range(count):
            password = ''.join(random.choice(characters) for _ in range(length))
            self.passwords.append(password)
            self.output_text.insert(tk.END, password + "\n")

    # View passwords functionality
    def view_passwords(self):
        # Clear the output text area
        self.output_text.delete(1.0, tk.END)
        # Enumerates generated password
        if self.use_view_passwords_var.get():
            for idx, password in enumerate(self.passwords, start=1):
                self.output_text.insert(tk.END, f"{idx}. {password}\n")
        else:
            self.output_text.insert(tk.END, "\n".join(self.passwords))

    # Clear passwords functionality
    def clear_passwords(self):
        # Clear the generated passwords and the output text area
        self.passwords = []
        self.output_text.delete(1.0, tk.END)

    # Save the generated passwords to a text file
    def save_passwords_to_file(self):
        # Save the generated passwords to a text file enumerate
        filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if filename:
            with open(filename, 'w') as file:
                for idx, password in enumerate(self.passwords, start=1):
                    file.write(f"{idx}. {password}\n")
            messagebox.showinfo("Information", "Passwords saved to file.")


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
