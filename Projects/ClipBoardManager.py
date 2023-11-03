#!/usr/bin/python3

import tkinter as tk
import pyperclip


class ClipboardManager:
    def __init__(self, root):
        self.root = root
        self.root.deiconify()
        self.clipboard_data = []
        self.create_ui()
        self.root.bind("<Command-c>", self.copy_to_clipboard)

    def create_ui(self):
        self.root.clipboard_clear()
        self.root.clipboard_append("Clipboard Manager")

        self.listbox = tk.Listbox(self.root)
        self.listbox.pack(fill=tk.BOTH, expand=True)
        self.root.after(500, self.check_clipboard)

    def check_clipboard(self):
        current_clipboard = pyperclip.paste()
        if current_clipboard not in self.clipboard_data:
            self.clipboard_data.append(current_clipboard)
            self.listbox.insert(tk.END, current_clipboard)
        self.root.after(500, self.check_clipboard)

    def copy_to_clipboard(self, event):
        text = self.root.selection_get(selection="CLIPBOARD")
        if text not in self.clipboard_data:
            self.clipboard_data.append(text)
            self.listbox.insert(tk.END, text)


if __name__ == "__main__":
    root = tk.Tk()
    clipboard_manager = ClipboardManager(root)
    root.mainloop()