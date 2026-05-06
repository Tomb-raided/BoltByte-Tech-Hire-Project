import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

imageexist = True
try:
    from PIL import Image, ImageTK
except:
    imageexist = False
    messagebox.showerror("Error, library PIL failed to Initialise, please read the README.MD file and restart the Program")
class boltbyteproject():
    def __init__(self,root):
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        self.root = root
        self.root.title = ("Bylt & Byte Tech Hire Interface")
        self.root.geometry(f"{width}x{height}+0+0")
        
        style = ttk.Style()
        style.configure
        
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand = True, fill= 'both', padx=10, pady=10)

        self.rentals = tk.Frame(self.notebook, highlightbackground="black", highlightthickness=2)
        self.returns = tk.Frame(self.notebook, highlightbackground="black", highlightthickness=2)
        self.admin = tk.Frame(self.notebook, highlightbackground="black", highlightthickness=2)
        
        self.notebook.add(self.rentals, text="Rentals")
        self.notebook.add(self.rentals, text="Returns")
        self.notebook.add(self.admin, text="Staff Access")
    
    
    
    
if __name__ == "__main__":
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.bind("<Escape>", lambda e: root.attributes('-fullscreen', False))
    app = boltbyteproject(root)
    root.mainloop()