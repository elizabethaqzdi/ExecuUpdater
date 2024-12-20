import tkinter as tk
from tkinter import filedialog, messagebox
import os
import shutil
import requests

class ExecuUpdater:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("ExecuUpdater")
        self.window.geometry("400x300")

        # GUI Elements
        self.label_file = tk.Label(self.window, text="Select an Executable to Update:")
        self.label_file.pack(pady=10)

        self.entry_file = tk.Entry(self.window, width=50)
        self.entry_file.pack(pady=5)

        self.btn_browse = tk.Button(self.window, text="Browse", command=self.browse_file)
        self.btn_browse.pack(pady=5)

        self.label_version = tk.Label(self.window, text="Enter New Version URL:")
        self.label_version.pack(pady=10)

        self.entry_version = tk.Entry(self.window, width=50)
        self.entry_version.pack(pady=5)

        self.btn_update = tk.Button(self.window, text="Update", command=self.update_exe)
        self.btn_update.pack(pady=20)

        self.text_log = tk.Text(self.window, height=8, width=45, state='disabled')
        self.text_log.pack(pady=10)

        self.window.mainloop()

    def browse_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Executable Files", "*.exe")])
        if file_path:
            self.entry_file.delete(0, tk.END)
            self.entry_file.insert(0, file_path)

    def log(self, message):
        self.text_log.config(state='normal')
        self.text_log.insert(tk.END, f"{message}\n")
        self.text_log.config(state='disabled')
        self.text_log.see(tk.END)

    def update_exe(self):
        exe_path = self.entry_file.get()
        new_version_url = self.entry_version.get()

        if not exe_path or not new_version_url:
            messagebox.showerror("Error", "Both file and URL are required!")
            return

        try:
            # Backup original file
            backup_path = exe_path + ".backup"
            shutil.copy(exe_path, backup_path)
            self.log(f"Backup created: {backup_path}")

            # Download the new version
            self.log("Downloading new version...")
            response = requests.get(new_version_url, stream=True)
            response.raise_for_status()

            with open(exe_path, 'wb') as exe_file:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        exe_file.write(chunk)

            self.log(f"Update successful: {exe_path}")
            messagebox.showinfo("Success", "Executable updated successfully!")
        except Exception as e:
            self.log(f"Error: {str(e)}")
            messagebox.showerror("Error", f"Update failed: {str(e)}")

if __name__ == "__main__":
    ExecuUpdater()
