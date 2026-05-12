import tkinter as tk
from tkinter import ttk, messagebox
import datetime
import json

imageexist = True
try:
    from PIL import Image, ImageTK
except:
    imageexist = False
    messagebox.showerror("Error, library PIL failed to Initialise, please read the README.MD file and restart the Program")
    
storeitems = [
    {"id": "001","name":"Keyboard","colour":"#E94343","dayprice":"9.99"},
    {"id": "002","name":"Headphones","colour":"#CF5353","dayprice":"7.99"},
    {"id": "003","name":"Mouse","colour":"#D9DC32","dayprice":"11.99"},
    {"id": "004","name":"Gaming Keyboard","colour":"#91D131","dayprice":"14.99"},
    {"id": "005","name":"Gaming HeadphonesB","colour":"#33C882","dayprice":"11.99"},
    {"id": "006","name":"Gaming HeadphonesP","colour":"#35D9C6","dayprice":"12.99"},
    {"id": "007","name":"Gaming Mouse","colour":"#2797D7","dayprice":"14.99"},
    {"id": "008","name":"XB1 Controller","colour":"#4B28CB","dayprice":"9.99"},
    {"id": "009","name":"PS5 Controller","colour":"#DC26CA","dayprice":"9.99"},
    {"id": "010","name":"Dummy Item","colour":"#C92780","dayprice":"9.99"}
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
        
        self.cart = {}
        self.item_qty = {}
        
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
        self.notebook.add(self.returns, text="Returns")
        self.notebook.add(self.admin, text="Staff Access")
        
        self.rentalsUI()
        self.returnsUI()
        self.adminUI()
        
    def rentalsUI(self):
        outer = tk.Frame(self.rentals, bg="#000000")
        outer.pack(expand=True, fill="both", padx=10, pady=10)
        
        left = tk.Frame(outer)
        left.pack(left, fill="y")
        left.pack_propagate(False)
        
        tk.Label(left, text="Hireble Equipment",font=("Helvetica", 15, "bold"))
        
        for item in storeitems:
            self.itemrows(left, item)
            
        right = tk.Frame(outer)
        right.pack(right, fill="y", expand=True, padx=(12,0))
        
        Dates = tk.LabelFrame(right,text="Rental Dates", font=("Helvetica", 12, "bold"), bg="black", fg="gray", padx=6, pady=4)
        Dates.pack(fill="x", padx=(0,6))
        
        self.Dickup_date = tk.StringVar(value=datetime.date.today().strftime("%d/%m/%Y"))
        self.Dropoff_date = tk.StringVar(value=(datetime.date.today() +datetime.timedelta(days=1)).strftime("%d/%m/%Y"))
        
        self.Daterow(Dates, "Pickup Date", self.pickup_date,0)
        self.Daterow(Dates, "Dropoff Date", self.dropoff_date,1)
        
        Name = tk.LabelFrame(right,name="Customer Name" ,font=("Helvetica", 12, "bold"), bg="black", fg="gray", padx=6, pady=4)
        Name.pack(fill="x", padx=(0,6))
        
        self.Name_entry = tk.StringVar()
        tk.Entry(Name, textvariable=self.name_entry, font=("Helvetica", 12), width=24, relief="raised",bd=1).pack(fill="x")
        
        ItemCart = tk.LabelFrame(right, text="Cart", font=("Helvetica", 12, "bold"), bg="black", fg="gray")
        ItemCart.pack(fill="x", padx=(0,6))
        
        self.CartText = tk.Label(ItemCart,)
        self.CartText.pack(expand=True, fill="both")
        
        totalprice = tk.Frame(right, bg="gray")
        totalprice.pack(fill="x")
        
        self.days_hired = self.row_totals(totalprice, "Duration:", "0 Days", 0)
        self.price_subtotal = self.row_totals(totalprice, "Subtotal:", "$0.00", 1)
        self.Sales_tax = self.row_totals(totalprice,f"({int(0.15*100)}%):","$0.00",2)
        self.Total_price = self.row_totals(totalprice,"Total Price:","0.00",3)
        
        tk.Button(right, text="Checkout", command=self.checkout, pady=6).pack(fill="both",padx=(0,6))
        
        self.updatecart()
    
    def itemrows(self, parrent, item):
        frame = tk.Frame(parrent, bg=item["Colour"],height=60)
        frame.pack(fill="x",pady=3)
        
        info = tk.Label(frame,bg=item["Colour"])
        info.pack(fill="x",pady=3)
        tk.Label(info,text=item["name"], font=("Helvetica", 12, "bold"))
        tk.Label(info,text=f"${item['daily_rate']:.2f}/day", font=("Helvetica", 12, "bold"))
        
        qty_button = tk.Frame(frame, bg=item["Colour"])
        qty_button(side="right",padx=8)
        
        qty_label = tk.Label(qty_button, text="0", font=("Helvetica", 12, "bold"),fg="white", bg=item["color"], width=2, anchor="center")
        qty_label.grid(row=0,column=1,pady=2)
        self.item_qty[item["id"]] = qty_label
        
        tk.Button(qty_button, text="+", width=2, font=("Helvetica", 9, "bold"),
                  relief="flat", bg="white", fg=item["color"], cursor="hand2",
                  command=lambda i=item: self._cart_change(i, 1)).grid(row=0, column=2, padx=(2, 0))
        tk.Button(qty_button, text="−", width=2, font=("Helvetica", 9, "bold"),
                  relief="flat", bg="white", fg=item["color"], cursor="hand2",
                  command=lambda i=item: self._cart_change(i, -1)).grid(row=0, column=0, padx=(0, 2))
    def daterow(self, parrent, label,var, row):
        

        
        
    def returnsUI(self):
        return
    def adminUI(self):
        return
        
            
if __name__ == "__main__":
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.bind("<Escape>", lambda e: root.attributes('-fullscreen', False))
    app = boltbyteproject(root)
    root.mainloop()