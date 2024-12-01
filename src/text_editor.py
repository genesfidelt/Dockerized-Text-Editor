#!/usr/bin/env python3

import tkinter as tk
from tkinter import filedialog, messagebox

# Function to create the main window of the text editor
class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Text Editor")

        # Set the default window size
        self.root.geometry("600x400")

        # Create a Text widget to display the text area
        self.text_area = tk.Text(self.root, wrap=tk.WORD, font=("Arial", 12))
        self.text_area.pack(expand=True, fill=tk.BOTH)

        # Create a menu bar
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # Add a File menu to the menu bar
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)

        # Add an Edit menu for changing font size
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Increase Font Size", command=self.increase_font_size)
        self.edit_menu.add_command(label="Decrease Font Size", command=self.decrease_font_size)

        # Initialize font size
        self.font_size = 12

    # Function to open a file
    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                               filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            try:
                with open(file_path, "r") as file:
                    text = file.read()
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(tk.END, text)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open file: {e}")

    # Function to save a file
    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            try:
                with open(file_path, "w") as file:
                    text = self.text_area.get(1.0, tk.END)
                    file.write(text.strip())  # Strip the extra newline character at the end
                messagebox.showinfo("Save", "File saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {e}")

    # Function to increase the font size
    def increase_font_size(self):
        self.font_size += 2
        self.text_area.config(font=("Arial", self.font_size))

    # Function to decrease the font size
    def decrease_font_size(self):
        if self.font_size > 6:  # Set a minimum font size limit
            self.font_size -= 2
            self.text_area.config(font=("Arial", self.font_size))

# Create the main window and start the application
if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()
