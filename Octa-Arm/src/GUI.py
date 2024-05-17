import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ConnectionHandler import check_url
import asyncio


class OctaArmApp:
    def __init__(self, root:tk.Tk):
        self.root = root
        self.root.title("Octa Arm")
        self.root.geometry("400x500")

        # Create welcome label
        self.welcome_label = tk.Label(root, text="Welcome to Octa Arm")
        self.welcome_label.pack(pady=10)


        self.enter_url = tk.Label(root, text="Enter Your Server URL: ")

        # Create option buttons
        self.option1_button = tk.Button(root, text="Choose Existing Octa Hub Server", command=self.show_progressbar)
        self.option1_button.pack(pady=5)

        self.option2_button = tk.Button(root, text="Choose My Server", command=self.show_input_field)
        self.option2_button.pack(pady=5)

        self.back_button = tk.Button(root, text="Back", command=self.clear_widgets)

        # Create progress bar (initially hidden)
        self.progressbar = ttk.Progressbar(root, mode='indeterminate')
        
        # Create input field and submit button (initially hidden)
        self.input_field = tk.Entry(root)
        self.submit_button = tk.Button(root, text="Submit", command=self.submit_server)

    def clear_widgets(self):
        """Hide all main widgets"""
        self.welcome_label.pack_forget()
        self.option1_button.pack_forget()
        self.option2_button.pack_forget()
        self.progressbar.pack_forget()
        self.input_field.pack_forget()
        self.submit_button.pack_forget()

    def show_progressbar(self):
        """Show the progress bar for option 1"""
        self.clear_widgets()
        self.progressbar.pack(pady=20)
        self.progressbar.start()

    def show_input_field(self):
        """Show the input field and submit button for option 2"""
        self.clear_widgets()
        self.enter_url.pack(pady=10)
        self.input_field.pack(pady=10)
        self.submit_button.pack(pady=5)

    def submit_server(self)->str:
        """Handle server URL submission"""
        server_url = self.input_field.get()
        if server_url:
            messagebox.showinfo("Server URL", f"Server URL submitted: {server_url}")
            self.server_url = server_url
            asyncio.run(check_url(server_url))
        else:
            messagebox.showwarning("Input Error", "Please enter a server URL")
        
    