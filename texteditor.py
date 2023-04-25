import tkinter as tk
from tkinter import filedialog

class TextEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("Text Editor")
        self.master.geometry("500x500")

        # Create a text area
        self.text_area = tk.Text(self.master, undo=True)
        self.text_area.pack(expand=True, fill='both')

        # Create a menu bar
        self.menu_bar = tk.Menu(self.master)
        self.master.config(menu=self.menu_bar)

        # Create the file menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=False)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.master.quit)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r") as f:
                file_content = f.read()
            self.text_area.delete('1.0', 'end')
            self.text_area.insert('1.0', file_content)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, "w") as f:
                file_content = self.text_area.get('1.0', 'end')
                f.write(file_content)

if __name__ == "__main__":
    root = tk.Tk()
    TextEditor(root)
    root.mainloop()
