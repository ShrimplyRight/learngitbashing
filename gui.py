import tkinter as tk
from tkinter import filedialog, messagebox
import json
import yaml
import xml.etree.ElementTree as ET
import jsonschema
from jsonschema import validate
import threading

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Data Conversion")
        self.geometry("400x200")

        self.label = tk.Label(self, text="Choose a file to process")
        self.label.pack(pady=20)

        self.button = tk.Button(self, text="Browse", command=self.browse_file)
        self.button.pack(pady=20)

    def browse_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            threading.Thread(target=self.process_file, args=(file_path,)).start()

    def process_file(self, file_path):
        # Implement file processing logic here
        messagebox.showinfo("File Processed", f"Processed file: {file_path}")

if __name__ == "__main__":
    app = App()
    app.mainloop()
