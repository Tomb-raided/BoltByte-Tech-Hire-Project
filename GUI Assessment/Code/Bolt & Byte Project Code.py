import tkinter as tk
from ttkthemes import ThemedTk
from tkinter import ttk
from tkinter import messagebox

imageexist = True
try:
    from PIL import Image, ImageTK
except:
    imageexist = False
    messagebox.showerror("Error, library PIL failed to Initialise, please read the README.MD file and restart the Program")
    
storeitems = [
    {"id": "001","name":"Keyboard","colour":"#E94343","dayprice":"9.99"},
    {"id": "002","name":"Headphones","colour":"#CF5353","dayprice":"9.99"},
    {"id": "003","name":"Mouse","colour":"#D9DC32","dayprice":"9.99"},
    {"id": "004","name":"Gaming Keyboard","colour":"#91D131","dayprice":"9.99"},
    {"id": "005","name":"Gaming HeadphonesB","colour":"#33C882","dayprice":"9.99"},
    {"id": "006","name":"Gaming HeadphonesP","colour":"#35D9C6","dayprice":"9.99"},
    {"id": "007","name":"Gaming Mouse","colour":"#2797D7","dayprice":"9.99"},
    {"id": "008","name":"XB1 Controller","colour":"#4B28CB","dayprice":"9.99"},
    {"id": "009","name":"PS5 Controller","colour":"#DC26CA","dayprice":"9.99"},
    {"id": "010","name":"","colour":"#C92780","dayprice":"9.99"}
]

GST = 0.15

class boltbyteproject():
    def __init__(self,root):
        
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        
        self.root = root
        self.root.title = ("Bylt & Byte Tech Hire Interface")
        self.root.geometry(f"{width}x{height}+0+0")
        self.root.configure(bg="black")
        
        header = tk.Frame(root, bg="#CF7979")
        header.pack(fill="x")
        tk.Label(header, text="Bolt & Byte Tech Hire",font=("Helvetica", 25), fg="#6D96BE",bg="systemTransparent").pack()
        
        style = ttk.Style()
        style.configure("TNotebook", bg="gray",borderwith="0")
        style.configure("TNotebook.tab",)
        
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