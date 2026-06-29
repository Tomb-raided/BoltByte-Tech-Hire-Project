import tkinter as tk
from tkinter import ttk, messagebox
import datetime
import json
import os
import uuid

storeitems = [
    {"id": "001","name":"Item #001","colour": "#901F15","dayprice": 9.00},
    {"id": "002","name":"Item #002","colour": "#DF3614","dayprice": 9.00},
    {"id": "003","name":"Item #003","colour": "#EE7218","dayprice": 9.00},
    {"id": "004","name":"Item #004","colour": "#DBA520","dayprice": 9.00},
    {"id": "005","name":"Item #005","colour": "#2C8D3A","dayprice": 9.00},
    {"id": "006","name":"Item #006","colour": "#1C5BB6","dayprice": 9.00},
]

GST = 0.15
BOLTBYTEFILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "boltbyte_data.json")

def load_data():
    if os.path.exists(BOLTBYTEFILE):
        try:
            with open(BOLTBYTEFILE, "r") as file:
                return json.load(file)
        except Exception:
            pass
    return {"user_data": {}}

def save_data(data):
    with open(BOLTBYTEFILE, "w") as file:
        json.dump(data,file, indent=4)

class boltbyteproject():
    def __init__(self,root):
        self.data = load_data()
        
        self.root = root
        self.root.title("Bolt & Byte Tech Hire Interface")
        self.root.geometry("900x600")
        
        # Base Cream Background for App
        self.root.configure(bg="#FAF9F6")
        
        self.cart = {}
        self.item_qty = {}
        
        # Dark Navy Header
        header = tk.Frame(root, bg="#1B2531", height=80)
        header.pack(fill="x")
        tk.Label(header, text="Bolt & Byte Tech Hire",font=("Helvetica", 25), bg="#1B2531", fg="#FFFFFF").pack()
        
        # Style configurations for Notebook to match Header
        style = ttk.Style()
        style.theme_use('default')
        style.configure("TNotebook", background="#FAF9F6", borderwidth="0")
        style.configure("TNotebook.Tab", background="#1B2531", foreground="#FFFFFF", borderwidth=0, padding=10)
        style.map("TNotebook.Tab", background=[("selected", "#1B2531")], foreground=[("selected", "#D1E028")])
        
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand = True, fill= 'both', padx=0, pady=0)

        # Tab Frames (Using cream background)
        self.rentals = tk.Frame(self.notebook, bg="#FAF9F6", highlightthickness=0)
        self.returns = tk.Frame(self.notebook, bg="#FAF9F6", highlightthickness=0)
        self.admin = tk.Frame(self.notebook, bg="#FAF9F6", highlightthickness=0)
        
        self.notebook.add(self.rentals, text="RENTALS")
        self.notebook.add(self.returns, text="RETURNS")
        self.notebook.add(self.admin, text="STAFF ACCESS")
        
        self.rentalsUI()
        self.returnsUI()
        self.adminUI()
        
    def rentalsUI(self):
        outer = tk.Frame(self.rentals, bg="#FAF9F6")
        outer.pack(expand=True, fill="both", padx=10, pady=10)
        
        left = tk.Frame(outer, bg="#FAF9F6", width=500)
        left.pack(side="left", fill="y")
        left.pack_propagate(False)
        
        tk.Label(left, text="AVAILABLE ITEMS",font=("Helvetica", 10, "bold"), bg="#FAF9F6", fg="#A39E93").pack(anchor="w", pady=6)
        
        for item in storeitems:
            self.itemrows(left, item)
            
        right = tk.Frame(outer, bg="#FAF9F6")
        right.pack(side="right", fill="y", expand=True, padx=(12,0))
        
        Dates = tk.LabelFrame(right,text="Rental Dates", font=("Helvetica", 12, "bold"), bg="#FAF9F6", fg="#1B2531", padx=6, pady=4, bd=0)
        Dates.pack(fill="x", padx=(0,6))
        
        self.Pickup_date = tk.StringVar(value=datetime.date.today().strftime("%d/%m/%Y"))
        self.Dropoff_date = tk.StringVar(value=(datetime.date.today() + datetime.timedelta(days=1)).strftime("%d/%m/%Y"))
        
        self.Daterow(Dates, "PICKUP DATE", self.Pickup_date,0)
        self.Daterow(Dates, "RETURN DATE", self.Dropoff_date,1)
        
        customerName = tk.LabelFrame(right,name="customer Name" ,font=("Helvetica", 10, "bold"), bg="#FAF9F6", fg="#1B2531", padx=6, pady=4, bd=0)
        customerName.pack(fill="x", padx=(0,6))
        
        self.name_entry = tk.StringVar()
        tk.Entry(customerName, textvariable=self.name_entry, font=("Helvetica", 12), width=24, relief="solid",bd=1, bg="#FFFFFF").pack(fill="x")
        
        ItemCart = tk.LabelFrame(right, text="Cart", font=("Helvetica", 12, "bold"), bg="#FAF9F6", fg="#1B2531", bd=0)
        ItemCart.pack(fill="x", padx=(0,6))
        
        self.CartText = tk.Text(ItemCart,font=("Courier", 10,), state="disabled", bg="#FFFFFF", fg="#1B2531", relief="solid", bd=1, height=8)
        self.CartText.pack(expand=True, fill="both")
        
        totalprice = tk.Frame(right, bg="#FAF9F6")
        totalprice.pack(fill="x", pady=10)
        
        self.days_hired = self.row_totals(totalprice, "Duration:", "0 Days", 0)
        self.price_subtotal = self.row_totals(totalprice, "Subtotal:", "$0.00", 1)
        self.Sales_tax = self.row_totals(totalprice,"SALES TAX:","$0.00",2)
        self.Total_price = self.row_totals(totalprice,"TOTAL COST:","0.00",3, bold=True)
        
        # Checkout Button with Navy/Yellow theme
        tk.Button(right, text="CHECKOUT →",command=self.checkout, pady=10, bg="#1B2531", fg="#D1E028", font=("Helvetica", 12, "bold"), relief="flat").pack(fill="both",padx=(0,6))
        
        self.updatecart()
    
    def itemrows(self, parent, item):
        frame = tk.Frame(parent, bg="#FAF9F6", height=60)
        frame.pack(fill="x", pady=3, padx=3)
        frame.propagate(False)
        
        # Color Box
        color_box = tk.Frame(frame, bg=item["colour"], width=30, height=30)
        color_box.pack(side="left", padx=5, pady=3)
        
        info = tk.Frame(frame, bg="#FAF9F6")
        info.pack(side="left", fill="both", expand=True, padx=5, pady=3)
        tk.Label(info, text=item["name"], font=("Helvetica", 12, "bold"), bg="#FAF9F6", fg="#1B2531").pack(anchor="w")
        tk.Label(info, text=f"${item['dayprice']:.2f}/day", font=("Helvetica", 10), bg="#FAF9F6", fg="#A39E93").pack(anchor="w")
        
        qty_button = tk.Frame(frame, bg="#FAF9F6")
        qty_button.pack(side="right", padx=8, pady=3)
        
        qty_label = tk.Label(qty_button, text="0", font=("Helvetica", 12, "bold"), fg="#1B2531", bg="#FAF9F6", width=2, anchor="center")
        qty_label.grid(row=0, column=1, pady=2)
        self.item_qty[item["id"]] = qty_label
        
        tk.Button(qty_button, text="+", width=2, font=("Helvetica", 9, "bold"), relief="solid", bg="#FFFFFF", fg="#1B2531", cursor="hand2", command=lambda i=item: self.cartchange(i, 1)).grid(row=0, column=2, padx=(2, 0))
        tk.Button(qty_button, text="−", width=2, font=("Helvetica", 9, "bold"), relief="solid", bg="#FFFFFF", fg="#1B2531", cursor="hand2", command=lambda i=item: self.cartchange(i, -1)).grid(row=0, column=0, padx=(0, 2))
        
        # Navy Add Button
        tk.Button(qty_button, text="ADD", font=("Helvetica", 9, "bold"), relief="flat", bg="#1B2531", fg="#D1E028", cursor="hand2", command=lambda i=item: self.cartchange(i, 1)).grid(row=0, column=3, padx=(10, 0))
        
    def Daterow(self, parent, label,var, row):
        tk.Label(parent, text=label, font=("Helvetica", 8, "bold"), bg="#FAF9F6", fg="#A39E93", width=12, anchor="w").grid(row=row, column=0, sticky="w", pady=2)
        daterowe = tk.Entry(parent,textvariable=var, font=("Helvetica", 10),width=12, relief="solid", bd=1, bg="#FFFFFF")
        daterowe.grid(row=row, column=1, padx=6, pady=2)
        daterowe.bind("<FocusOut>", lambda ev: self.updatecart())
        
    def row_totals(self, parent, item, value,row, bold=False):
        fnt = ("Helvetica", 10, "bold") if bold else ("Helvetica", 10)
        fg_col = "#1B2531" if bold else "#A39E93"
        tk.Label(parent, text=item, font=fnt, bg="#FAF9F6", fg=fg_col, anchor="w").grid(row=row, column=0, sticky="w")
        label = tk.Label(parent, text=value, font=fnt, bg="#FAF9F6", fg="#1B2531", anchor="w")
        label.grid(row=row, column=1, sticky="e")
        parent.grid_columnconfigure(1, weight=1)
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
        name_var = self.name_entry.get()
        if name_var == "":
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
            "timestamp": datetime.datetime.now().isoformat(),
            "Has_Returned": False
        }
        self.data["user_data"][receipt_id] = record
        save_data(self.data)
        
        for item_id in self.cart.keys():
            self.item_qty[item_id].config(text="0")
        self.cart.clear()
        self.updatecart()
        self.checkoutbill(record)
        return record
        
    def checkoutbill(self, record):
        bill_window = tk.Toplevel(self.root)
        bill_window.title("Rental Receipt")
        bill_window.geometry("400x500")
        bill_window.configure(bg="#FAF9F6")
        
        tk.Label(bill_window, text="Bolt & Byte Tech Hire", font=("Helvetica", 16, "bold"), bg="#FAF9F6").pack(pady=10)
        tk.Label(bill_window, text=f"Receipt ID: {record['receipt_id']}", bg="#FAF9F6").pack()
        tk.Label(bill_window, text=f"Date: {record['timestamp'][:10]}", bg="#FAF9F6").pack()
        tk.Label(bill_window, text="------------------------------", bg="#FAF9F6").pack(pady=5)
        tk.Label(bill_window, text=f"Customer: {record['customer_name']}", bg="#FAF9F6").pack()
        tk.Label(bill_window, text=f"Pickup Date: {record['pickup_date']}", bg="#FAF9F6").pack()
        tk.Label(bill_window, text=f"Dropoff Date: {record['dropoff_date']}", bg="#FAF9F6").pack()
        tk.Label(bill_window, text="Items Rented:", font=("Helvetica", 12, "bold"), bg="#FAF9F6").pack(pady=10)

        for item in record["items"]:
            tk.Label(bill_window, text=f"{item['name']} x{item['quantity']} - ${item['line_cost']:.2f}", bg="#FAF9F6").pack(anchor="center", padx=20)

        tk.Label(bill_window, text=f"Subtotal: ${record['subtotal']:.2f}", bg="#FAF9F6").pack(pady=5)
        tk.Label(bill_window, text=f"Tax ({int(GST*100)}%): ${record['tax']:.2f}", bg="#FAF9F6").pack(pady=5)
        tk.Label(bill_window, text=f"Total: ${record['total']:.2f}", font=("Helvetica", 12, "bold"), bg="#FAF9F6").pack(pady=10)
        
        tk.Button(bill_window, text="Close", command=bill_window.destroy, bg="#1B2531", fg="#FFFFFF").pack(pady=10)
        
    def returnsUI(self):
        # Top Brown section for Returns
        receipt_id_search = tk.Frame(self.returns, bg="#402512")
        receipt_id_search.pack(anchor="n" ,fill="x")
        
        tk.Label(receipt_id_search, text="Input Receipt Number", font=("Helvetica", 16, "bold"), bg="#402512", fg="#FFFFFF").pack(anchor="w", padx=20, pady=(20, 5))
        
        receipt_id_box = tk.Frame(receipt_id_search, bg="#402512")
        receipt_id_box.pack(fill="x", padx=20, pady=(0, 20))
        
        self.receipt_id_entry = tk.Entry(receipt_id_box, font=("Helvetica", 12), width=36, relief="flat", bd=0, bg="#301C0D", fg="#FFFFFF", insertbackground="#FFFFFF")
        self.receipt_id_entry.pack(side="left", expand=True, fill="x", ipady=8)
        
        tk.Button(receipt_id_box, text="SEARCH", font=("Helvetica", 10, "bold"), command=self.search_receipt, bg="#D0672A", fg="#FFFFFF", relief="flat").pack(side="right", ipadx=15, ipady=5)
        
        # Bottom Cream Section
        forgot_receipt = tk.Frame(self.returns, bg="#FAF9F6")
        forgot_receipt.pack(expand=True, anchor="n",fill="both", padx=20, pady=20)
        
        tk.Label(forgot_receipt, text="Forgot your receipt number?", font=("Helvetica", 12, "italic"), bg="#FAF9F6", fg="#D0672A").pack(anchor="w", pady=(10,20))
        
        inputs_frame = tk.Frame(forgot_receipt, bg="#FAF9F6")
        inputs_frame.pack(fill="x")
        
        tk.Label(inputs_frame, text="CUSTOMER NAME", font=("Helvetica", 8, "bold"), bg="#FAF9F6", fg="#A39E93").grid(row=0, column=0, sticky="w")
        self.name_entry_r = tk.Entry(inputs_frame, font=("Helvetica", 12), width=25, relief="solid", bd=1, bg="#FAF9F6")
        self.name_entry_r.grid(row=1, column=0, sticky="w", pady=(0, 20), padx=(0, 20))
        
        tk.Label(inputs_frame, text="PICKUP DATE", font=("Helvetica", 8, "bold"), bg="#FAF9F6", fg="#A39E93").grid(row=0, column=1, sticky="w")
        self.date_pickup = tk.Entry(inputs_frame, font=("Helvetica", 12), width=25, relief="solid", bd=1, bg="#FAF9F6")
        self.date_pickup.grid(row=1, column=1, sticky="w", pady=(0, 20))
        
        tk.Label(inputs_frame, text="DROPOFF DATE", font=("Helvetica", 8, "bold"), bg="#FAF9F6", fg="#A39E93").grid(row=2, column=0, sticky="w")
        self.date_dropoff = tk.Entry(inputs_frame, font=("Helvetica", 12), width=25, relief="solid", bd=1, bg="#FAF9F6")
        self.date_dropoff.grid(row=3, column=0, sticky="w", pady=(0, 20))

        tk.Button(forgot_receipt, text="Search Records", font=("Helvetica", 12, "bold"), command=self.search_name, bg="#D0672A", fg="#FFFFFF", relief="flat").pack(fill="x", pady=20, ipady=8)
        
    def search_receipt(self):
        receipt_code = self.receipt_id_entry.get().strip()
        if receipt_code in self.data["user_data"]:
            record = self.data["user_data"][receipt_code]
            self.checkoutbill(record)
            self.data["Has_Returned"] = True
            save_data(self.data)
        else:
            messagebox.showerror("Not Found", "No receipt found with that Receipt ID.")
        
    def search_name(self):
        name_search = self.name_entry_r.get().strip()
        for record in self.data["user_data"].values():
            if record["customer_name"] == name_search:
                self.checkoutbill(record)
                self.data["Has_Returned"] = True
                save_data(self.data)
                return
        else:
            messagebox.showerror("Not Found", "No receipt found with that customer name.")
        
    def search_dates(self):
        date_search_pickup = self.date_pickup.get()
        date_search_dropoff = self.date_dropoff.get()
        for record in self.data["user_data"].values():
            if record["pickup_date"] == date_search_pickup and record["dropoff_date"] == date_search_dropoff:
                self.checkoutbill(record)
                self.data["Has_Returned"] = True
                save_data(self.data)
                return
        else:
            messagebox.showerror("Not Found", "No product hire with those dates")
            
    def adminUI(self):
        outer = tk.Frame(self.admin, bg="#FAF9F6")
        outer.pack(expand=True, fill="both", padx=20, pady=20)
        
        # Changed from #000000 to match light aesthetic
        left = tk.Frame(outer, width=300, bg="#FAF9F6")
        left.pack(side="left", fill="y")
        left.pack_propagate(False)
        
        tk.Label(left, text="Rental Records", font=("Helvetica", 12, "bold"), bg="#FAF9F6", fg="#1B2531").pack(pady=6, anchor="w")
        record_listbox = tk.Frame(left, bg="#FAF9F6")
        record_listbox.pack(expand=True, fill="both", pady=6)
        
        scrollbar = tk.Scrollbar(record_listbox)
        scrollbar.pack(side="right", fill="y")
        
        self.record_list = tk.Listbox(record_listbox, font=("Helvetica", 10), yscrollcommand=scrollbar.set, bg="#FFFFFF", relief="flat", highlightbackground="#E0DCD3", highlightthickness=1)
        self.record_list.pack(side="left", expand=True, fill="both")
        
        scrollbar.configure(command=self.record_list.yview)
        self.record_list.bind("<<ListboxSelect>>", self.record_show)
        
        right = tk.Frame(outer, bg="#FAF9F6")
        right.pack(side="right", fill="both", expand=True, padx=(20,0))
        
        # Details Header row
        details_header = tk.Frame(right, bg="#FAF9F6")
        details_header.pack(fill="x", pady=(0, 10))
        
        self.record_details_title = tk.Label(details_header, text="RECEIPT ID", font=("Helvetica", 10, "bold"), bg="#FAF9F6", fg="#A39E93")
        self.record_details_title.pack(side="left")
        
        # Green Badge
        tk.Label(details_header, text="RECORD SELECTED", font=("Helvetica", 9, "bold"), bg="#E0F5E9", fg="#39A061", padx=10, pady=4).pack(side="right")
        
        self.record_details_content = tk.Label(right,text="Select a record...",font=("Helvetica", 12), bg="#FAF9F6", fg="#1B2531", justify="left")
        self.record_details_content.pack(anchor="w", fill="x", pady=10)
        
        tk.Label(right, text="ITEMS HIRED", font=("Helvetica", 10, "bold"), bg="#FAF9F6", fg="#A39E93").pack(anchor="w", pady=(10, 5))
        
        item_frame = tk.Frame(right, bg="#FAF9F6")
        item_frame.pack(fill="x", pady=6)
        
        self.item_list = tk.Listbox(item_frame, font=("Helvetica", 10), height=4, bg="#F0EBE1", fg="#1B2531", relief="flat")
        self.item_list.pack(expand=True, fill="x")
        
        # Action Buttons matching Image 3 Theme
        actions_frame = tk.Frame(right, bg="#FAF9F6")
        actions_frame.pack(fill="x", pady=(20, 0))
        
        tk.Button(actions_frame, text="✉ SEND RECORD TO EMAIL", font=("Helvetica", 10, "bold"), command=self.copy_record, bg="#EEF3FC", fg="#26499D", relief="flat", anchor="w", padx=15).pack(fill="x", pady=4, ipady=6)
        tk.Button(actions_frame, text="🖨 PRINT RECORD", font=("Helvetica", 10, "bold"), command=self.copy_record, bg="#F3EFE9", fg="#1B2531", relief="flat", anchor="w", padx=15).pack(fill="x", pady=4, ipady=6)
        tk.Button(actions_frame, text="✕ DELETE RECORD", font=("Helvetica", 10, "bold"), command=self.delete_record, bg="#FDE9E9", fg="#CB3A3A", relief="flat", anchor="w", padx=15).pack(fill="x", pady=4, ipady=6)
        
        self.selected_receipt_ID = None
        self.record_refresh()
        
    def record_refresh(self):
        self.record_list.delete(0, tk.END)
        self.selected_receipt_ID = []
        for receipt_id, record in self.data["user_data"].items():
            self.record_list.insert(tk.END, f" #{receipt_id} {record['customer_name']} {record['pickup_date']} to {record['dropoff_date']}")
            self.selected_receipt_ID.append(receipt_id)
        return
        
    def delete_record(self):
        if not self.record_list.curselection(): return
        delete_id = self.selected_receipt_ID[self.record_list.curselection()[0]]
        confirm = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this record? This action cannot be undone.")
        if confirm:
            self.data["user_data"].pop(delete_id, None)
            save_data(self.data)
            self.record_refresh()
            self.record_details_content.config(text="Select a record...")
            self.item_list.delete(0, tk.END)
        return
        
    def copy_record(self):
        if self.selected_receipt_ID:
            selected_record = self.record_list.curselection()
            if selected_record:
                receipt_id = self.selected_receipt_ID[selected_record[0]]
                record = self.data["user_data"][receipt_id]
                record_text = json.dumps(record, indent=4)
                self.root.clipboard_clear()
                self.root.clipboard_append(record_text)
                messagebox.showinfo("Copied", "Record copied to clipboard.")
            else:
                messagebox.showwarning("No Selection", "Please select a record to copy.")
        else:
            messagebox.showwarning("No Records", "There are no records to copy.")
            
    def record_show(self, event):
        selected_record = self.record_list.curselection()
        if selected_record:
            receipt_id = self.selected_receipt_ID[selected_record[0]]
            record = self.data["user_data"][receipt_id]
            self.record_details_title.config(text=f"RECEIPT ID - #{receipt_id}")
            
            details_text = f"{record['customer_name']}\nDROP-OFF DATE: {record['dropoff_date']}   PICKUP DATE: {record['pickup_date']}"
            self.record_details_content.config(text=details_text)
            
            self.item_list.delete(0, tk.END)
            for item in record["items"]:
                self.item_list.insert(tk.END, f"  {item['name']} x{item['quantity']}")
                
    def staff_list(self):
        return

if __name__ == "__main__":
    root = tk.Tk()
    app = boltbyteproject(root)
    root.mainloop()