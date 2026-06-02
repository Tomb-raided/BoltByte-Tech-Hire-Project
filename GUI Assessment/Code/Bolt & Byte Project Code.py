import tkinter as tk
from tkinter import ttk, messagebox
import datetime
import json
import os
import uuid

#imageexist = True
#try:
#    from PIL import Image, ImageTK
#except:
#    imageexist = False
#    messagebox.showerror("Error, library PIL failed to Initialise, please read the README.MD file and restart the Program")
    
storeitems = [
    {"id": "001","name":"Keyboard","colour": "#E94343","dayprice": 9.99},
    {"id": "002","name":"Headphones","colour": "#CF5353","dayprice": 7.99},
    {"id": "003","name":"Mouse","colour": "#D9DC32","dayprice": 11.99},
    {"id": "004","name":"Gaming Keyboard","colour": "#91D131","dayprice": 14.99},
    {"id": "005","name":"Gaming Headphones_Black","colour": "#33C882","dayprice": 11.99},
    {"id": "006","name":"Gaming Headphones_Pink","colour": "#35D9C6","dayprice": 12.99},
    {"id": "007","name":"Gaming Mouse","colour": "#2797D7","dayprice": 14.99},
    {"id": "008","name":"XB1 Controller","colour": "#4B28CB","dayprice": 9.99},
    {"id": "009","name":"PS5 Controller","colour": "#DC26CA","dayprice": 9.99},
]

GST = 0.15
BOLTBYTEFILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "boltbyte_data.json")

def load_data():
    if os.path.exists(BOLTBYTEFILE):
        with open(BOLTBYTEFILE, "r") as f:
            return json.load(f)
    else:
        return {"rentals": [], "returns": [], "receipt_id": {}}
def save_data(data):
    with open(BOLTBYTEFILE, "w") as f:
        json.dump(data, f, indent=4)

class boltbyteproject():
    def __init__(self,root):
        self.data = load_data()
        
        #width = root.winfo_screenwidth()
        #height = root.winfo_screenheight()
        
        self.root = root
        self.root.title("Bolt & Byte Tech Hire Interface")
        #self.root.geometry(f"{width}x{height}+0+0")
        self.root.geometry("900x600")
        self.root.configure(bg="#FFFFFF")
        
        self.cart = {}
        self.item_qty = {}
        
        header = tk.Frame(root, bg="#FFFFFF", height=80)
        header.pack(fill="x")
        tk.Label(header, text="Bolt & Byte Tech Hire",font=("Helvetica", 25), fg="#6D90B3",bg="systemTransparent").pack()
        
        style = ttk.Style()
        style.configure("TNotebook", bg="#FFFFFF",borderwith="0")
        style.configure("TNotebook.tab",)
        
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand = True, fill= 'both', padx=10, pady=10)

        self.rentals = tk.Frame(self.notebook, highlightbackground="#FFFFFF", highlightthickness=2)
        self.returns = tk.Frame(self.notebook, highlightbackground="#FFFFFF", highlightthickness=2)
        self.admin = tk.Frame(self.notebook, highlightbackground="#FFFFFF", highlightthickness=2)
        
        self.notebook.add(self.rentals, text="Rentals")
        self.notebook.add(self.returns, text="Returns")
        self.notebook.add(self.admin, text="Staff Access")
        
        self.rentalsUI()
        self.returnsUI()
        self.adminUI()
        
    def rentalsUI(self):
        outer = tk.Frame(self.rentals, bg="#FFFFFF")
        outer.pack(expand=True, fill="both", padx=10, pady=10)
        
        left = tk.Frame(outer, bg="#FFFFFF", width=500)
        left.pack(side="left", fill="y")
        left.pack_propagate(False)
        
        tk.Label(left, text="Hireable Equipment",font=("Helvetica", 15, "bold"), bg="#FFFFFF").pack(pady=6)
        
        for item in storeitems:
            self.itemrows(left, item)
            
        right = tk.Frame(outer, bg="#FFFFFF")
        right.pack(side="right", fill="y", expand=True, padx=(12,0))
        
        Dates = tk.LabelFrame(right,text="Rental Dates", font=("Helvetica", 12, "bold"), bg="#FFFFFF", padx=6, pady=4)
        Dates.pack(fill="x", padx=(0,6))
        
        self.Pickup_date = tk.StringVar(value=datetime.date.today().strftime("%d/%m/%Y"))
        self.Dropoff_date = tk.StringVar(value=(datetime.date.today() + datetime.timedelta(days=1)).strftime("%d/%m/%Y"))
        
        self.Daterow(Dates, "Pickup Date", self.Pickup_date,0)
        self.Daterow(Dates, "Dropoff Date", self.Dropoff_date,1)
        
        Name = tk.LabelFrame(right,name="customer Name" ,font=("Helvetica", 12, "bold"), bg="#FFFFFF", fg="gray", padx=6, pady=4)
        Name.pack(fill="x", padx=(0,6))
        
        self.name_entry = tk.StringVar()
        tk.Entry(Name, textvariable=self.name_entry, font=("Helvetica", 12), width=24, relief="raised",bd=1).pack(fill="x")
        
        ItemCart = tk.LabelFrame(right, text="Cart", font=("Helvetica", 12, "bold"),foreground="white", bg="#FFFFFF", fg="gray")
        ItemCart.pack(fill="x", padx=(0,6))
        
        self.CartText = tk.Text(ItemCart,font=("Courier", 10,), state="disabled", bg="#FFFFFF", relief="solid", bd=1, height=8)
        self.CartText.pack(expand=True, fill="both")
        
        totalprice = tk.Frame(right, bg="#FFFFFF")
        totalprice.pack(fill="x")
        
        self.days_hired = self.row_totals(totalprice, "Duration:", "0 Days", 0)
        self.price_subtotal = self.row_totals(totalprice, "Subtotal:", "$0.00", 1)
        self.Sales_tax = self.row_totals(totalprice,f"({int(GST*100)}%):","$0.00",2)
        self.Total_price = self.row_totals(totalprice,"Total Price:","0.00",3)
        
        tk.Button(right, text="Checkout",command=lambda: self.bill(record=self.checkout()) or None, pady=6).pack(fill="both",padx=(0,6))
        
        self.updatecart()
    
    def itemrows(self, parent, item):
        # Create outer frame for each item with fixed height and colored background
        frame = tk.Frame(parent, bg=item["colour"], height=60)
        frame.pack(fill="x", pady=3, padx=3)
        frame.propagate(False)
        
        # Left side: item info (name and price)
        info = tk.Frame(frame, bg=item["colour"])
        info.pack(side="left", fill="both", expand=True, padx=5, pady=3)
        tk.Label(info, text=item["name"], font=("Helvetica", 12, "bold"), bg=item["colour"]).pack(anchor="w")
        tk.Label(info, text=f"${item['dayprice']:.2f}/day", font=("Helvetica", 10), bg=item["colour"]).pack(anchor="w")
        
        # Right side: quantity controls (-, quantity display, +)
        qty_button = tk.Frame(frame, bg=item["colour"])
        qty_button.pack(side="right", padx=8, pady=3)
        
        qty_label = tk.Label(qty_button, text="0", font=("Helvetica", 12, "bold"), fg="white", bg=item["colour"], width=2, anchor="center")
        qty_label.grid(row=0, column=1, pady=2)
        self.item_qty[item["id"]] = qty_label
        
        tk.Button(qty_button, text="+", width=2, font=("Helvetica", 9, "bold"), relief="flat", bg="white", fg=item["colour"], cursor="hand2", command=lambda i=item: self.cartchange(i, 1)).grid(row=0, column=2, padx=(2, 0))
        tk.Button(qty_button, text="−", width=2, font=("Helvetica", 9, "bold"), relief="flat", bg="white", fg=item["colour"], cursor="hand2", command=lambda i=item: self.cartchange(i, -1)).grid(row=0, column=0, padx=(0, 2))
        
    def Daterow(self, parent, label,var, row):
        tk.Label(parent, text=label, font=("Helvetica", 10), bg="#FFFFFF", width=12, anchor="w").grid(row=row, column=0, sticky="w", pady=2)
        daterowe = tk.Entry(parent,textvariable=var, font=("Helvetica", 10),width=12, relief="solid", bd=1)
        daterowe.grid(row=row, column=1, padx=6, pady=2)
        daterowe.bind("<FocusOut>", lambda ev: self.updatecart())
        
    def row_totals(self, parent, item, value,row):
        font = ("Helvetica", 10)
        tk.Label(parent, text=item, font=font, anchor="w")
        label = tk.Label(parent, text=value, font=font, anchor="w")
        label.grid(row=row, column=1, sticky="e")
        return label
        
    def cartchange(self, item, delta):
        current = self.cart.get(item["id"], 0)
        new = max(0, current + delta)
        if new == 0:
            self.cart.pop(item["id"], None)
        else:
            self.cart[item["id"]] = new
        self.item_qty[item["id"]].config(text=str(new))
        self.updatecart()
    def daysduration(self):
        try:
            pickup = datetime.datetime.strptime(self.Pickup_date.get().strip(), "%d/%m/%Y").date()
            dropoff = datetime.datetime.strptime(self.Dropoff_date.get().strip(), "%d/%m/%Y").date()
            daystotal = (dropoff - pickup).days
            return max(1, daystotal)
        except ValueError:
            return 1
    
    def updatecart(self):
        daystotal = self.daysduration()
        catalog_map = {i["id"]: i for i in storeitems}

        lines = []
        subtotal = 0.0
        for item_id, qty in self.cart.items():
            item = catalog_map[item_id]
            line_cost = item["dayprice"] * qty * daystotal
            subtotal += line_cost
            lines.append(f"{item['name']:<22} x{qty}  ${line_cost:>7.2f}")

        tax = subtotal * GST
        total = subtotal + tax

        self.CartText.config(state="normal")
        self.CartText.delete("1.0", tk.END)
        if lines:
            header = f"{'Item':<22} Qty  {'Cost':>8}\n" + "─" * 38 + "\n"
            self.CartText.insert(tk.END, header + "\n".join(lines))
        else:
            self.CartText.insert(tk.END, "  No items in cart.")
        self.CartText.config(state="disabled")

        self.days_hired.config(text=f"{daystotal} day{'s' if daystotal != 1 else ''}")
        self.price_subtotal.config(text=f"${subtotal:.2f}")
        self.Sales_tax.config(text=f"${tax:.2f}")
        self.Total_price.config(text=f"${total:.2f}")
    def checkout(self):
        name_var = self.name_entry.get().strip()
        if not name_var:
            messagebox.showwarning("Name Field is empty"," Please enter a Name.")
            return
        if not self.cart:
            messagebox.showwarning("Cart is empty", "Please add items to cart to proceed.")
            return

        daystotal = self.daysduration()
        storeitemslist = {i["id"]: i for i in storeitems}
        order_items = []
        subtotal = 0.0
        for item_id, qty in self.cart.items():
            item = storeitemslist[item_id]
            line_cost = item["dayprice"] * qty * daystotal
            subtotal += line_cost
            order_items.append({
                "id": item_id,
                "name": item["name"],
                "quantity": qty,
                "line_cost": line_cost
            })
        tax = subtotal * GST
        total = subtotal + tax 
        receipt_id = str(uuid.uuid4())[:8].upper()
        
        record = {
            "receipt_id": receipt_id,
            "customer_name": name_var,
            "pickup_date": self.Pickup_date.get().strip(),
            "dropoff_date": self.Dropoff_date.get().strip(),
            "days_hired": daystotal,
            "items": order_items,
            "subtotal": subtotal,
            "tax": tax,
            "total": total,
            "timestamp": datetime.datetime.now().isoformat()
        }
        self.data["receipt_id"][receipt_id] = record
        save_data(self.data)
        
        for item_id in self.cart.keys():
            self.item_qty[item_id].config(text="0")
        self.cart.clear()
        #self.name_entry.delete(0, tk.END)
        self.updatecart()
        #self.refresh_admin()
        return record
        
    def bill(self, record):
        bill_window = tk.Toplevel(self.root)
        bill_window.title("Rental Receipt")
        bill_window.geometry("400x500")
        
        tk.Label(bill_window, text="Bolt & Byte Tech Hire", font=("Helvetica", 16, "bold")).pack(pady=10)
        tk.Label(bill_window, text=f"Receipt ID: {record['receipt_id']}").pack()
        tk.Label(bill_window, text=f"Date: {record['timestamp'][:10]}").pack()
        tk.Label(bill_window, text="------------------------------").pack(pady=5)
        tk.Label(bill_window, text=f"Customer: {record['customer_name']}").pack()
        tk.Label(bill_window, text=f"Pickup Date: {record['pickup_date']}").pack()
        tk.Label(bill_window, text=f"Dropoff Date: {record['dropoff_date']}").pack()
        tk.Label(bill_window, text="Items Rented:", font=("Helvetica", 12, "bold")).pack(pady=10)

        for item in record["items"]:
            tk.Label(bill_window, text=f"{item['name']} x{item['quantity']} - ${item['line_cost']:.2f}").pack(anchor="w", padx=20)

        tk.Label(bill_window, text=f"Subtotal: ${record['subtotal']:.2f}").pack(pady=5)
        tk.Label(bill_window, text=f"Tax ({int(GST*100)}%): ${record['tax']:.2f}").pack(pady=5)
        tk.Label(bill_window, text=f"Total: ${record['total']:.2f}", font=("Helvetica", 12, "bold")).pack(pady=10)
        
        tk.Button(bill_window, text="Close", command=bill_window.destroy).pack(pady=10)
        
    def returnsUI(self):
        receipt_id_search = tk.LabelFrame(self.returns, text="Search Rental Receipt", font=("Helvetica", 12, "bold"), bg="#000000", padx=6, pady=4)
        receipt_id_search.pack(fill="x")
        self.receipt_id_entry = tk.Entry(receipt_id_search, font=("Helvetica", 10), width=36, relief="solid", bd=1)
        self.receipt_id_entry.grid(row=0, column=1, padx=6, pady=2)
        tk.Button(receipt_id_search, text="Search", command=self.search_receipt, pady=6).grid(row=0, column=2, padx=6, pady=2)
        return
    def search_receipt(self):
        receipt_id = self.receipt_id_entry.get().strip()
        receipt = self.data["receipt_id"].get(receipt_id)
        if receipt:
            details = f"Receipt ID: {receipt['receipt_id']}\nCustomer: {receipt['customer_name']}\nPickup: {receipt['pickup_date']}\nDropoff: {receipt['dropoff_date']}\nItems:\n"
            for item in receipt["items"]:
                details += f"  - {item['name']} x{item['quantity']} (${item['line_cost']:.2f})\n"
            details += f"Subtotal: ${receipt['subtotal']:.2f}\nTax: ${receipt['tax']:.2f}\nTotal: ${receipt['total']:.2f}"
            messagebox.showinfo("Rental Receipt", details)
        else:
            messagebox.showerror("Not Found", "No receipt found with that Receipt ID.")
    def search_name(self):
        name_search = self.name_entry.get().strip()
        receipt = self.data["customer_name"].get(name_search)
        if receipt:
            details = f"Receipt ID: {receipt['receipt_id']}\nCustomer: {receipt['customer_name']}\nPickup: {receipt['pickup_date']}\nDropoff: {receipt['dropoff_date']}\nItems:\n"
            for item in receipt["items"]:
                details += f"  - {item['name']} x{item['quantity']} (${item['line_cost']:.2f})\n"
            details += f"Subtotal: ${receipt['subtotal']:.2f}\nTax: ${receipt['tax']:.2f}\nTotal: ${receipt['total']:.2f}"
            messagebox.showinfo("Rental Receipt", details)
        else:
            messagebox.showerror("Not Found", "No receipt found with that Receipt ID.")
    def adminUI(self):
        return
        
            
if __name__ == "__main__":
    root = tk.Tk()
    app = boltbyteproject(root)
    root.mainloop()