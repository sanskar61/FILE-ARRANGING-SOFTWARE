import os
import shutil
import tkinter as tk
from tkinter import messagebox, filedialog, ttk

class AnimatedLoginWindow:
    def __init__(self, master):
        self.master = master
        master.title("Login")
        master.geometry("400x300")

        # Background
        self.background_canvas = tk.Canvas(master, bg="#34495E", width=400, height=300)
        self.background_canvas.pack(fill="both", expand=True)

        # Title
        self.title_label = tk.Label(master, text="Login", font=("Helvetica", 24), fg="#FFFFFF", bg="#34495E")
        self.title_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        # Username Entry
        self.username_label = tk.Label(master, text="Username:", font=("Helvetica", 14), fg="#FFFFFF", bg="#34495E")
        self.username_label.place(relx=0.3, rely=0.4, anchor=tk.CENTER)
        self.username_entry = ttk.Entry(master, font=("Helvetica", 12))
        self.username_entry.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        # Password Entry
        self.password_label = tk.Label(master, text="Password:", font=("Helvetica", 14), fg="#FFFFFF", bg="#34495E")
        self.password_label.place(relx=0.3, rely=0.5, anchor=tk.CENTER)
        self.password_entry = ttk.Entry(master, font=("Helvetica", 12), show="*")
        self.password_entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Login Button
        self.login_button = ttk.Button(master, text="Login", command=self.login, style="Primary.TButton")
        self.login_button.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

        # Style
        self.style = ttk.Style()
        self.style.configure("Primary.TButton", font=("Helvetica", 14), foreground="#FFFFFF", background="#2980B9")
        self.style.map("Primary.TButton", background=[("active", "#1F618D")])

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Dummy authentication, replace with your authentication mechanism
        if username == "admin" and password == "password":
            self.master.destroy()
            root = tk.Tk()
            app = FileArrangerApp(root)
            root.mainloop()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

class FileArrangerApp:
    def __init__(self, master):
        self.master = master
        master.title("File Arranging Software")
        master.geometry("800x600")

        # Title
        self.title_label = tk.Label(master, text="File Arranging Software", font=("Helvetica", 24), fg="#333333")
        self.title_label.pack(pady=20)

        # Select Folder Button
        self.select_button = ttk.Button(master, text="Select Folder", command=self.select_folder, style="Primary.TButton")
        self.select_button.pack(pady=10)

        # Arrange Files Button
        self.arrange_button = ttk.Button(master, text="Arrange Files", command=self.arrange_files, state=tk.DISABLED, style="Primary.TButton")
        self.arrange_button.pack(pady=5)

        # Status Label
        self.status_label = tk.Label(master, text="", font=("Helvetica", 14), fg="#333333")
        self.status_label.pack()

        # Progress Bar
        self.progressbar = ttk.Progressbar(master, orient=tk.HORIZONTAL, length=600, mode='determinate')
        self.progressbar.pack(pady=20)

    def select_folder(self):
        self.selected_folder = filedialog.askdirectory()
        if self.selected_folder:
            self.arrange_button.config(state=tk.NORMAL)
            self.status_label.config(text=f"Selected Folder: {self.selected_folder}")
        else:
            self.status_label.config(text="No folder selected")

    def arrange_files(self):
        if not self.selected_folder:
            messagebox.showerror("Error", "Please select a folder first.")
            return

        try:
            total_files = len(os.listdir(self.selected_folder))
            self.progressbar['maximum'] = total_files
            progress = 0

            for filename in os.listdir(self.selected_folder):
                if os.path.isfile(os.path.join(self.selected_folder, filename)):
                    file_extension = filename.split('.')[-1]
                    destination_folder = os.path.join(self.selected_folder, file_extension)
                    if not os.path.exists(destination_folder):
                        os.makedirs(destination_folder)
                    shutil.move(os.path.join(self.selected_folder, filename), destination_folder)
                    progress += 1
                    self.progressbar['value'] = progress
                    self.master.update()

            self.status_label.config(text="Files arranged successfully")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

def main():
    root = tk.Tk()
    app = AnimatedLoginWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
