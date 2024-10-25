from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import os
import ftplib
import tkinter as tk
from tkinter import messagebox
import ctypes

def show_message_box(message, title):
    ctypes.windll.user32.MessageBoxW(0, message, title, 0)
    
class CustomDialog(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Custom Command Input")
        
        # Set window size and center it
        self.geometry("340x180")
        self.center_window()
        
        # Create labels and entry fields for FTP URL, User, and Password
        self.create_widgets()

    def create_widgets(self):
        # Frame for better organization
        frame = tk.Frame(self, padx=10, pady=10)
        frame.pack(expand=True, fill=tk.BOTH)
        
        tk.Label(frame, text="FTP URL:", anchor="w").grid(row=0, column=0, pady=5, sticky="w")
        self.ftp_url = tk.Entry(frame, width=40)
        self.ftp_url.grid(row=0, column=1, pady=5)
        
        tk.Label(frame, text="FTP User:", anchor="w").grid(row=1, column=0, pady=5, sticky="w")
        self.ftp_user = tk.Entry(frame, width=40)
        self.ftp_user.grid(row=1, column=1, pady=5)
        
        tk.Label(frame, text="Password:", anchor="w").grid(row=2, column=0, pady=5, sticky="w")
        self.password = tk.Entry(frame, width=40, show='*')
        self.password.grid(row=2, column=1, pady=5)
        
        tk.Button(frame, text="OK", command=self.on_ok, width=8, height=1, font=("Arial", 10),  relief="raised").grid(row=3, column=0, columnspan=3, pady=10)


    def on_ok(self):
        # Collect inputs
        url = self.ftp_url.get().strip()
        user = self.ftp_user.get().strip()
        passwd = self.password.get().strip()

        # Optionally, perform some validation here
        if not url or not user or not passwd:
            messagebox.showwarning("Input Error", "All fields are required.")
            return

        # Process inputs
        self.result = (url, user, passwd)
        self.destroy()

    def get_result(self):
        return getattr(self, 'result', None)
    
    def center_window(self):
        # Get screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        
        # Calculate x and y coordinates to center the window
        window_width = 335
        window_height = 180
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        
        self.geometry(f'{window_width}x{window_height}+{x}+{y}')

class ProxyFTPHandler(FTPHandler):
    

    def on_login(self, username):
        # Show the custom dialog
        client_ip = self.remote_ip
        print(f"Client IP: {client_ip} attempted to log in with username: {username}")
        dialog = CustomDialog()
        dialog.mainloop()
        
        result = dialog.get_result()
        if result:
            self.real_server_ip, self.real_server_user, self.real_server_password = result
            print(f"Executing custom command with FTP URL: {self.real_server_ip}, User: {self.real_server_user} by user: {username} and password: {self.real_server_password}")
            message = f"Custom command executed with FTP URL: {self.real_server_ip}, User: {self.real_server_user}"
            show_message_box(message, "FTP Command Result")
    def on_file_received(self, file):
        print(f"File received: {file}")
        if self.is_sensitive(file):
            self.block_transfer(file)
        else:
            self.forward_to_real_server(file)

    def is_sensitive(self, file):
        print(f"Checking file for sensitive content: {file}")
        with open(file, 'r') as f:
            content = f.read()
            if "sensitive" in content:  # Replace with actual content checking logic
                print("Sensitive content found.")
                return True
        print("No sensitive content found.")
        return False

    def block_transfer(self, file):
        print(f"Blocking file transfer: {file}")
        show_message_box("550 File transfer blocked: Sensitive content found.","DLP Alert")
        
        print(f"File {file} has been removed.")

    def forward_to_real_server(self, file):
        print(f"Forwarding file to real server: {file}")
        if not getattr(self, 'real_server_ip', None) or not getattr(self, 'real_server_user', None) or not getattr(self, 'real_server_password', None):
            print("Error: Real server details are not set.")
            self.respond("550 Internal server error.")
            show_message_box("Internal server error.", "FTP Command Result")
            return
        
        try:
            ftp = ftplib.FTP(self.real_server_ip)
            ftp.login(self.real_server_user, self.real_server_password)
            with open(file, 'rb') as f:
                ftp.storbinary(f'STOR {os.path.basename(file)}', f)
            ftp.quit()
            
            print(f"File {file} has been forwarded and removed locally.")
            show_message_box(f"File {file} has been forwarded and removed locally.", "FTP Command Result")
        except Exception as e:
            print(f"Error forwarding file: {e}")
            self.respond("550 Error forwarding file to real server.")
            show_message_box("Error forwarding file to real server.", "FTP Command Result")


def main():
    authorizer = DummyAuthorizer()
    authorizer.add_user("user", "12345", "ftp", perm="elradfmwMT")
    authorizer.add_anonymous("ftp")

    handler = ProxyFTPHandler
    handler.authorizer = authorizer

    server = FTPServer(("0.0.0.0", 2121), handler)
    print("Starting FTP proxy server on port 2121...")
    server.serve_forever()

if __name__ == '__main__':
    main()
