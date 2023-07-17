#own notepad


from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


root = Tk()
root.title("SSG's Notepad")
root.geometry("800x500")
root.wm_iconbitmap("my_icon.ico")


# Text widget for notepad
text_editor = Text(root, font=('times new roman', 24))
text_editor.configure(bg='light blue')
text_editor.pack(fill=BOTH, expand=True)


# Function to create a new file
def new_file():
    text_editor.delete('1.0', END)
    root.title("SSG's Notepad")


# Function to open an existing file
def open_file():
    file = filedialog.askopenfile(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file is not None:
        text_editor.delete('1.0', END)
        contents = file.read()
        text_editor.insert('1.0', contents)
        file.close()
        root.title(f"SSG's Notepad - {file.name}")


# Function to save the file
def save_file():
    file = filedialog.asksaveasfile(mode='w', defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file is not None:
        data = text_editor.get('1.0', END)
        file.write(data)
        file.close()
        root.title(f"SSG's Notepad - {file.name}")
        messagebox.showinfo("Info", "File has been saved successfully! at IIIT A")


# Function to cut the selected text
def cut():
    text_editor.event_generate("<<Cut>>")


# Function to copy the selected text
def copy():
    text_editor.event_generate("<<Copy>>")


# Function to paste the copied text
def paste():
    text_editor.event_generate("<<Paste>>")


# Function to undo the last action
def undo():
    text_editor.event_generate("<<Undo>>")


# Function to redo the last undone action
def redo():
    text_editor.event_generate("<<Redo>>")


# Menu Bar
menu_bar = Menu(root)
root.config(menu=menu_bar)


# File Menu
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)


# Edit Menu
edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)
edit_menu.add_separator()
edit_menu.add_command(label="Undo", command=undo)
edit_menu.add_command(label="Redo", command=redo)


root.mainloop()
