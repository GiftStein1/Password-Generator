import random
import string
import tkinter as tk
import tkinter.messagebox as messagebox
import tkinter.ttk as ttk

def generate_password():
    password_length = int(length_var.get())
    use_special_chars = special_chars_var.get()
    use_uppercase = uppercase_var.get()
    use_lowercase = lowercase_var.get()
    use_numbers = numbers_var.get()

    characters = ''
    if use_special_chars:
        characters += string.punctuation
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits

    if not characters:
        messagebox.showwarning("Password generation error", "Please select at least one character type!")
        return

    password = ''.join(random.choice(characters) for _ in range(password_length))
    password_entry.delete(0, tk.END)
    password_entry.insert(tk.END, password)
    root.clipboard_clear()
    root.clipboard_append(password)
    messagebox.showinfo("Password generated", "Password copied to clipboard!")

root = tk.Tk()
root.title("Password Generator")


main_frame = ttk.Frame(root, padding=20, style='TFrame')
main_frame.pack()


length_label = ttk.Label(main_frame, text="Password Length:", style='TLabel')
length_label.pack()

length_var = tk.StringVar(root)
length_dropdown = ttk.OptionMenu(main_frame, length_var, "8", "8", "16", "24", "32", "40", "48", "56", "64")
length_dropdown.pack()


special_chars_var = tk.BooleanVar()
special_chars_checkbox = ttk.Checkbutton(main_frame, text="Include Special Characters", variable=special_chars_var, style='TCheckbutton')
special_chars_checkbox.pack()

uppercase_var = tk.BooleanVar()
uppercase_checkbox = ttk.Checkbutton(main_frame, text="Include Uppercase Letters", variable=uppercase_var, style='TCheckbutton')
uppercase_checkbox.pack()

lowercase_var = tk.BooleanVar()
lowercase_checkbox = ttk.Checkbutton(main_frame, text="Include Lowercase Letters", variable=lowercase_var, style='TCheckbutton')
lowercase_checkbox.pack()

numbers_var = tk.BooleanVar()
numbers_checkbox = ttk.Checkbutton(main_frame, text="Include Numbers", variable=numbers_var, style='TCheckbutton')
numbers_checkbox.pack()


generate_button = ttk.Button(main_frame, text="Generate Password", command=generate_password, style='TButton')
generate_button.pack()


password_label = ttk.Label(main_frame, text="Generated Password:", style='TLabel')
password_label.pack()

password_entry = ttk.Entry(main_frame, width=40, state='readonly', style='TEntry')
password_entry.pack()


style = ttk.Style()
style.configure("TFrame", background="#000000")
style.configure("TLabel", background="#000000", foreground="#ffffff")
style.configure("TCheckbutton", background="#000000", foreground="#ffffff")
style.configure("TButton", background="#FFFFFF", foreground="#000000")
style.configure("TEntry", fieldbackground="#ffffff")

root.mainloop()
