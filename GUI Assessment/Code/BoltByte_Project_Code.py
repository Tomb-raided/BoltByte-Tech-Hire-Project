import tkinter as tk

from tkinter import ttk, messagebox

import datetime

import json

import os

import uuid

Store_items = [
    {"id": "001" ,"name": "Keyboard", "colour": "#E94343", "dayprice": 9.99},
    {"id": "002", "name": "Headphones", "colour": "#CF5353", "dayprice": 7.99},
    {"id": "003", "name": "Mouse", "colour": "#D9DC32", "dayprice": 11.99}, 
    {"id": "004", "name": "Gaming Keyboard", "colour": "#91D131", "dayprice": 14.99},
    {"id": "005", "name": "Gaming Headphones_Black", "colour": "#33C882", "dayprice": 11.99},
    {"id": "006", "name": "Gaming Headphones_Pink", "colour": "#35D9C6", "dayprice": 12.99},
    {"id": "007", "name": "Gaming Mouse", "colour": "#2797D7", "dayprice": 14.99},
    {"id": "008", "name": "XB1 Controller", "colour": "#4B28CB", "dayprice": 9.99},
    {"id": "009", "name": "PS5 Controller", "colour": "#DC26CA", "dayprice": 9.99},
]

GST = 0.15
BOLTBYTEFILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "boltbyte_data.json")
adminpassword = str("TestPassword")
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
        
        self.root.geometry("935x900")
        
        self.Cart = {}
        
        self.Item_amount = {}
        
        Main_frame = ttk.Frame(root)
        
        Main_frame.pack(fill="both")
        
        Main_title = ttk.Label(Main_frame, text="Bolt & Byte Tech Hire",font=("Helvetica", 25))
        Main_title.pack()
        
        style = ttk.Style()

        style.configure("TNotebook",borderwith="0")
        style.theme_use("clam")

        
        self.Notebook = ttk.Notebook(root)
        self.Notebook.pack(expand = True, fill= 'both', padx=10, pady=10)

        self.Rentals = ttk.Frame(self.Notebook)
        
        self.Returns = ttk.Frame(self.Notebook)
        
        self.Admin = ttk.Frame(self.Notebook)
        
        self.Notebook.add(self.Rentals, text="Rentals")
        
        self.Notebook.add(self.Returns, text="Returns")
        
        self.Notebook.add(self.Admin, text="Staff Access")
        
        self.Rentals_UI()
        
        self.Returns_UI()
        
        self.Admin_UI()
        
    def Rentals_UI(self):
        Rentals_outer = ttk.Frame(self.Rentals)
        
        Rentals_outer.pack(expand=True, fill="both", padx=10, pady=10)
        
        Rentals_left = ttk.Frame(Rentals_outer,width=500)
        
        Rentals_left.pack(side="left", fill="y")
        
        Rentals_left.pack_propagate(False)
        
        Item_rows_title = ttk.Label(Rentals_left, text="Hireable Equipment",font=("Helvetica", 15, "bold"))
        Item_rows_title.pack(pady=6)
        
        for item in Store_items:
            self.Item_rows(Rentals_left, item)
            
        Rentals_right = ttk.Frame(Rentals_outer)
        Rentals_right.pack(side="right", fill="y", expand=True, padx=(12,0))
        
        Dates = ttk.Labelframe(Rentals_right,text="Rental Dates")
        Dates.pack(fill="x", padx=(0,6))
        
        self.Pickup_date = tk.StringVar(value=datetime.date.today().strftime("%d/%m/%Y"))
        self.Dropoff_date = tk.StringVar(value=(datetime.date.today() + datetime.timedelta(days=1)).strftime("%d/%m/%Y"))
        
        self.Date_row(Dates, "Pickup Date", self.Pickup_date,0)
        self.Date_row(Dates, "Dropoff Date", self.Dropoff_date,1)
        
        Customer_name = ttk.LabelFrame(Rentals_right, name="customer Name")
        Customer_name.pack(fill="x", padx=(0,6))
        
        self.Name_entry = tk.StringVar()
        Rentals_name_entry = ttk.Entry(Customer_name, textvariable=self.Name_entry, font=("Helvetica", 12), width=24)
        Rentals_name_entry.pack(fill="x")
        
        Item_cart = ttk.LabelFrame(Rentals_right, text="Cart")
        Item_cart.pack(fill="x", padx=6)
        
        self.Cart_text = tk.Text(Item_cart,font=("Courier", 10), relief="solid", bd=1, height=8,bg="#dcdad5",fg="#000000")
        self.Cart_text.pack(expand=True, fill="both")
        
        Total_price_frame = ttk.Frame(Rentals_right)
        Total_price_frame.pack(fill="x")
        
        self.Days_hired = self.row_totals(Total_price_frame, "Duration:", "0 Days", 0)
        self.Price_subtotal = self.row_totals(Total_price_frame, "Subtotal:", "$0.00", 1)
        self.Sales_tax = self.row_totals(Total_price_frame,"Sales Tax(15%):","$0.00",2)
        self.Total_price = self.row_totals(Total_price_frame,"Total Price:","$0.00",3)
        
        Rentals_Checkout = ttk.Button(Rentals_right, text="Checkout",command=self.checkout)
        Rentals_Checkout.pack(fill="both",padx=(0,6))
        
        self.Update_cart()
    
    def Item_rows(self, parent, item):
        Item_rows_frame = tk.Frame(parent, bg=item["colour"], height=60)
        Item_rows_frame.pack(fill="x", pady=3, padx=3)
        Item_rows_frame.propagate(False)
        
        Item_rows_colour = tk.Frame(Item_rows_frame, bg=item["colour"])
        Item_rows_colour.pack(side="left", fill="both", expand=True, padx=5, pady=3)
        
        Item_rows_name = tk.Label(Item_rows_colour, text=item["name"], font=("Helvetica", 12, "bold"), bg=item["colour"])
        Item_rows_name.pack(anchor="w")
        
        Item_rows_price = tk.Label(Item_rows_colour, text=f"${item["dayprice"]}/day", font=("Helvetica", 10), bg=item["colour"])
        Item_rows_price.pack(anchor="w")
        
        Item_rows_button = tk.Frame(Item_rows_frame, bg=item["colour"])
        Item_rows_button.pack(side="right", padx=8, pady=3)
        
        Item_rows_label = tk.Label(Item_rows_button, text="0", font=("Helvetica", 12, "bold"), fg="black", bg=item["colour"], width=2, anchor="center")
        Item_rows_label.grid(row=0, column=1, pady=2)
        self.Item_amount[item["id"]] = Item_rows_label
        
        Item_rows_add = tk.Button(Item_rows_button, text="+", width=2, font=("Helvetica", 9, "bold"), relief="flat", bg=item["colour"], fg=item["colour"], command=lambda i=item: self.Cart_change(i, 1))
        Item_rows_add.grid(row=0, column=2, padx=(2, 0))
        
        Item_rows_minus = tk.Button(Item_rows_button, text="−", width=2, font=("Helvetica", 9, "bold"), relief="flat", bg=item["colour"], fg=item["colour"], command=lambda i=item: self.Cart_change(i, -1))
        Item_rows_minus.grid(row=0, column=0, padx=(0, 2))
        
    def Date_row(self, parent, label,var, row):
        
        Date_row_title = ttk.Label(parent, text=label, font=("Helvetica", 10), width=12, anchor="w")
        Date_row_title.grid(row=row, column=0, padx=6, pady=2)
        
        Date_row_entry = ttk.Entry(parent,textvariable=var, font=("Helvetica", 10),width=12,)
        Date_row_entry.grid(row=row, column=1, padx=6, pady=2)
        
        Date_row_entry.bind("<FocusOut>", lambda run: self.Update_cart())
        
    def row_totals(self, parent, item, value,row):
        
        Row_totals_item = ttk.Label(parent, text=item, font=("Helvetica", 10), anchor="w")
        Row_totals_item.grid(row=row, column=0, sticky="e")
        
        Row_totals_cost = ttk.Label(parent, text=value, font=("Helvetica", 10), anchor="w")
        Row_totals_cost.grid(row=row, column=1, sticky="e")
        
        return Row_totals_cost
        
    def Cart_change(self, item, delta):
        Current_cart = self.Cart.get(item["id"], 0)
        New_cart = max(0, Current_cart + delta)
        if New_cart == 0:
            self.Cart.pop(item["id"], None)
        else:
            self.Cart[item["id"]] = New_cart
        self.Item_amount[item["id"]].config(text=str(New_cart))
        self.Update_cart()
    def Days_duration(self):
        try:
            Pickup = datetime.datetime.strptime(self.Pickup_date.get().strip(), "%d/%m/%Y").date()
            Dropoff = datetime.datetime.strptime(self.Dropoff_date.get().strip(), "%d/%m/%Y").date()
            Days_total = (Dropoff - Pickup).days
            return Days_total
        except ValueError:
            return 1
    
    def Update_cart(self):
        Days_total = self.Days_duration()
        Cart_items = {i["id"]: i for i in Store_items}

        Cart_lines = []
        Subtotal = 0.0
        for Item_id, Amount in self.Cart.items():
            Item = Cart_items[Item_id]
            Line_cost = Item["dayprice"] * Amount * Days_total
            Subtotal += Line_cost
            Cart_lines.append(f"{Item['name']} x{Amount}  ${Line_cost}")

        Taxtotal = Subtotal * GST
        Total = Subtotal + Taxtotal

        self.Cart_text.config(state="normal")
        self.Cart_text.delete("1.0", tk.END)
        
        if Cart_lines:
            header = f"{'Item'} Amount  {'Cost'}\n" + "─" * 38 + "\n"
            self.Cart_text.insert(tk.END, header + "\n".join(Cart_lines))
        else:
            self.Cart_text.insert(tk.END, "  No items in cart.")
            
        self.Cart_text.config(state="disabled")

        self.Days_hired.config(text=f"{Days_total} day{'s' if Days_total != 1 else ''}")
        self.Price_subtotal.config(text=f"${Subtotal:.2f}")
        self.Sales_tax.config(text=f"${Taxtotal:.2f}")
        self.Total_price.config(text=f"${Total:.2f}")
        
    def checkout(self):
        Checkout_Name = self.Name_entry.get()
        if Checkout_Name == "":
          messagebox.showwarning("Name Field is empty"," Please enter a Name.")
          return
        if not self.Cart:
           messagebox.showwarning("Cart is empty", "Please add items to cart to proceed.")
           return

        Days_total = self.Days_duration()
        Checkout_items = {i["id"]: i for i in Store_items}
        Ordered_items = []
        Subtotal = 0.0
        for Item_id, Amount in self.Cart.items():
            Item = Checkout_items[Item_id]
            Line_cost = Item["dayprice"] * Amount * Days_total
            Subtotal += Line_cost
            Ordered_items.append({
                "Id": Item_id,
                "Name": Item["name"],
                "Amount": Amount,
                "Cost": Line_cost
            })
        Taxtotal = Subtotal * GST
        Total = Subtotal + Taxtotal 
        Receipt_id = str(uuid.uuid4())[:8].upper()
        
        record = {
            "receipt_id": Receipt_id,
            "customer_name": Checkout_Name,
            "pickup_date": self.Pickup_date.get().strip(),
            "dropoff_date": self.Dropoff_date.get().strip(),
            "days_hired": Days_total,
            "items": Ordered_items,
            "subtotal": Subtotal,
            "tax": Taxtotal,
            "total": Total,
            "timestamp": datetime.datetime.now().isoformat(),
            "Has_Returned": False
        }
        self.data["user_data"][Receipt_id] = record
        save_data(self.data)
        
        for Item_id in self.Cart.keys():
            self.Item_amount[Item_id].config(text="0")
            
        self.Cart.clear()
        
        self.Update_cart()
        
        self.Name_entry.set("")

        self.Record_refresh()
        
        self.Checkout_bill(record)
        
        return record
        
    def Checkout_bill(self, record):
        Bill_window = tk.Toplevel(self.root)
        Bill_window.title("Rental Receipt")
        Bill_window.geometry("400x500")
        
        Bill_title = ttk.Label(Bill_window, text="Bolt & Byte Tech Hire", font=("Helvetica", 16, "bold"))
        Bill_title.pack(pady=10)
        
        Bill_receiptID =ttk.Label(Bill_window, text=f"Receipt ID: {record['receipt_id']}")
        Bill_receiptID.pack()
        
        Bill_timestamp = ttk.Label(Bill_window, text=f"Date: {record['timestamp'][:10]}")
        Bill_timestamp.pack()
        
        Bill_linebreak = ttk.Label(Bill_window, text="------------------------------")
        Bill_linebreak.pack(pady=5)
        
        Bill_C_name = ttk.Label(Bill_window, text=f"Customer: {record['customer_name']}")
        Bill_C_name.pack()
        
        Bill_P_date = ttk.Label(Bill_window, text=f"Pickup Date: {record['pickup_date']}")
        Bill_P_date.pack()
        
        Bill_D_date = ttk.Label(Bill_window, text=f"Dropoff Date: {record['dropoff_date']}")
        Bill_D_date.pack()
        
        Bill_items_header = ttk.Label(Bill_window, text="Items Rented:", font=("Helvetica", 12, "bold"))
        Bill_items_header.pack(pady=10)

        for item in record["items"]:
            Bill_items = ttk.Label(Bill_window, text=f"{item['name']} x{item['quantity']} - ${item['line_cost']}")
            Bill_items.pack(anchor="center", padx=20)

        Bill_subtotal = ttk.Label(Bill_window, text=f"Subtotal: ${record['subtotal']}")
        Bill_subtotal.pack(pady=5)
        
        Bill_Tax = ttk.Label(Bill_window, text=f"Tax ({int(GST*100)}%): ${record['tax']}")
        Bill_Tax.pack(pady=5)
        
        Bill_total = ttk.Label(Bill_window, text=f"Total: ${record['total']}", font=("Helvetica", 12, "bold"))
        Bill_total.pack(pady=10)
        
        Bill_close = ttk.Button(Bill_window, text="Close", command=Bill_window.destroy)
        Bill_close.pack(pady=10)
        
    def Returns_UI(self):
        Receipt_frame = ttk.LabelFrame(self.Returns, text="Search Rental Receipt")
        Receipt_frame.pack(anchor="n" ,fill="x",padx=6, pady=4)
        
        Receipt_ID_frame = ttk.Frame(Receipt_frame)
        Receipt_ID_frame.pack(fill="x")
        
        self.Receipt_ID_entry = ttk.Entry(Receipt_ID_frame, font=("Helvetica", 10), width=36)
        self.Receipt_ID_entry.pack(side="left", padx=6, pady=2, expand=True, fill="x")
        
        ttk.Button(Receipt_ID_frame, text="Search", command=self.Search_receipt).pack(side="right", padx=6, pady=2)
        
        Receipt_forget_frame = ttk.LabelFrame(self.Returns, text="Forgot your Receipt? Use your Name or Pickup/Dropoff Date")
        Receipt_forget_frame.pack(expand=True, anchor="center",fill="x",padx=6, pady=4)
        
        Receipt_name = ttk.LabelFrame(Receipt_forget_frame, text="Remeber the Name you used? Use this Box!",)
        Receipt_name.pack(expand=True, anchor="n",fill="x",padx=6, pady=4)
        
        self.Receipt_name_entry = ttk.Entry(Receipt_name, font=("Helvetica", 10), width=36)
        self.Receipt_name_entry.pack(expand=True, side="left", padx=5, pady=2, fill="x")
        
        ttk.Button(Receipt_name, text="Search", command=self.Search_name,).pack(side="right", padx=6, pady=2)
        
        Receipts_dates = ttk.LabelFrame(Receipt_forget_frame, text="Remember your Pickup/Dropoff Date? Use this Box!",)
        Receipts_dates.pack(expand=True, anchor="n",fill="x",padx=6, pady=4)
        
        self.Receipts_dates_pickup = ttk.Entry(Receipts_dates, font=("Helvetica", 10), width=36)
        self.Receipts_dates_pickup.pack(side="left", padx=5, pady=20, expand=True, fill="x")
        
        self.Receipts_dates_dropoff = ttk.Entry(Receipts_dates, font=("Helvetica", 10), width=36)
        self.Receipts_dates_dropoff.pack(side="left", padx=5, pady=30, expand=True, fill="x")
        
        ttk.Button(Receipts_dates, text="Search", command=self.Search_dates).pack(side="left", padx=6, pady=2)
        return
    
    def Search_receipt(self):
        Receipt_id = self.Receipt_ID_entry.get().strip()
        if Receipt_id in self.data["user_data"] and self.data["user_data"]["Has_Returned"] == "false":
                record = self.data["user_data"][Receipt_id]
                self.Checkout_bill(record)
                self.data["user_data"]["Has_Returned"] = "true"
                save_data(self.data)
        elif Receipt_id not in self.data["user_data"]:
            messagebox.showerror("Not Found", "No receipt found with that Receipt ID.")
        elif self.data["user_data"][Receipt_id]["Has_Returned"] == "true":
            messagebox.showerror("This Receipt has already been returned")
        else:
            messagebox.showerror("Unknown or Unexpected Error","Contact your administrator for support")
        
    def Search_name(self):
        Name_search = self.Receipt_name_entry.get().strip()
        for record in self.data["user_data"].values():
            if record["customer_name"] == Name_search:
                self.Checkout_bill(record)
                self.data["user_data"]["Has_Returned"] = True
                save_data(self.data)
                return
        else:
            messagebox.showerror("Not Found", "No receipt found with that customer name.")
        
    def Search_dates(self):
        Date_search_pickup = self.Receipts_dates_pickup.get()
        Date_search_dropoff = self.Receipts_dates_dropoff.get()
        for record in self.data["user_data"].values():
            if record["pickup_date"] == Date_search_pickup and record["dropoff_date"] == Date_search_dropoff:
                self.Checkout_bill(record)
                self.data["user_data"]["Has_Returned"] = True
                save_data(self.data)
                return
        else:
            messagebox.showerror("Not Found", "No product hire with those dates")
    def Admin_UI(self):

        # Password code Commented Out
        # Python doesn't respond well to tbis kind of password frame.
        # If I come back to this It'd be better to have a login page as the base frame that everything else parrents off
        # and for an admin login instead of a user login give access to this page.
        #I do not have enough time to implement this
        #self.Staff_login_window = tk.Frame(self.Admin)
        #self.Staff_login_window.place(relx=0, rely=0, relheight=1, relwidth=1)
        #
        #self.Login_label = tk.Label(self.Staff_login_window,text="Input Password Here \n Authorised Users Only",font=("Helvetica", 12, "bold"),bg="gray",fg="black")
        #self.Login_label.place(relx=0.5,rely=0.35,anchor="center")
        #
        #self.Login_password_check = tk.StringVar()
        #
        #self.Login_entry = tk.Entry(self.Staff_login_window, textvariable=self.Login_password_check, bg="gray",fg="black")
        #self.Login_entry.place(relx=0.5,rely=0.45,anchor="center")
        #
        #self.Login_button = tk.Button(self.Staff_login_window, text="Confirm Password", command=self.Login_process)
        #self.Login_button.place(relx=0.5,rely=0.50,anchor="center")

        self.Admin_UI_outer = ttk.Frame(self.Admin)
        self.Admin_UI_outer.pack(expand=True, fill="both", padx=10, pady=10)
        
        Admin_UI_left = ttk.Frame(self.Admin_UI_outer, width=350,)
        Admin_UI_left.pack(side="left", fill="y")
        Admin_UI_left.pack_propagate(False)
        
        ttk.Label(Admin_UI_left, text="Rental Records", font=("Helvetica", 15, "bold")).pack(pady=6)
        
        Admin_record_listbox = ttk.Frame(Admin_UI_left)
        Admin_record_listbox.pack(expand=True, fill="both", padx=6, pady=6)
        
        Admin_scrollbar = ttk.Scrollbar(Admin_record_listbox)
        Admin_scrollbar.pack(side="right", fill="y")
        
        self.Admin_record_list = tk.Listbox(Admin_record_listbox, font=("Helvetica", 12), yscrollcommand=Admin_scrollbar.set)
        self.Admin_record_list.pack(side="left", expand=True, fill="both")
        
        Admin_scrollbar.configure(command=self.Admin_record_list.yview)
        self.Admin_record_list.bind("<<ListboxSelect>>", self.Record_show)
        
        Admin_right = ttk.Frame(self.Admin_UI_outer)
        Admin_right.pack(side="right", fill="both", expand=True, padx=(12,0))
        
        self.Admin_record_title = ttk.Label(Admin_right, text="Receipt details", font=("Helvetica", 10))
        self.Admin_record_title.pack(anchor="w")
        
        self.Admin_record_details = ttk.Label(Admin_right,text="",font=("Helvetica", 10),relief="solid")
        self.Admin_record_details.pack(anchor="w", expand=True, fill="both", padx=6, pady=6)
        
        Admin_item_hired = ttk.Label(Admin_right, text="Items Hired", font=("Helvetica", 12))
        Admin_item_hired.pack(pady=10)
        
        Admin_item_frame = ttk.Frame(Admin_right, relief="solid")
        Admin_item_frame.pack(expand=True, fill="both", padx=6, pady=6)
        
        Admin_item_scrollbar = ttk.Scrollbar(Admin_item_frame)
        Admin_item_scrollbar.pack(side="right", fill="y")
        
        self.Admin_item_list = tk.Listbox(Admin_item_frame, font=("Helvetica", 10), yscrollcommand=Admin_item_scrollbar.set)
        self.Admin_item_list.pack(side="left", expand=True, fill="both")
        
        Admin_item_scrollbar.configure(command=self.Admin_item_list.yview)
        
        Admin_totals = ttk.Label(Admin_right, text="", font=("Helvetica", 12, "bold"),)
        Admin_totals.pack(anchor="w", pady=8)
        
        ttk.Button(Admin_right, text="Copy record to Clipboard", command=self.Copy_record).pack(pady=4)
        ttk.Button(Admin_right, text="Delete Record", command=self.Delete_record).pack(pady=4)
        
        # self.Staff_login_window.tkraise()
        # Part of the commented out Login page.
        self.Selected_receipt_ID = ""
        self.Record_refresh()
    
    def Record_refresh(self):
        self.Admin_record_list.delete(0, tk.END)
        self.Selected_receipt_ID = []
        for receipt_id, record in self.data["user_data"].items():
            self.Admin_record_list.insert(tk.END, f" #{receipt_id} {record['customer_name']} \n {record['pickup_date']}")
            self.Selected_receipt_ID.append(receipt_id)
        return
    def Delete_record(self):
        delete_id = self.Selected_receipt_ID[self.Admin_record_list.curselection()[0]]
        delete_confirm = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this record? This action cannot be undone.")
        if delete_confirm:
            self.data["user_data"].pop(delete_id, None)
            save_data(self.data)
            self.Record_refresh()
        return
    def Copy_record(self):
        if self.Selected_receipt_ID:
            Selected_record = self.Admin_record_list.curselection()
            if Selected_record:
                receipt_id = self.Selected_receipt_ID[Selected_record[0]]
                record = self.data["user_data"][receipt_id]
                record_text = json.dumps(record, indent=4)
                self.root.clipboard_clear()
                self.root.clipboard_append(record_text)
                messagebox.showinfo("Copied", "Record copied to clipboard.")
            else:
                messagebox.showwarning("No Selection", "Please select a record to copy.")
        else:
            messagebox.showwarning("No Records", "There are no records to copy.")
            
    def Record_show(self, event):
        
        Selected_record = self.Admin_record_list.curselection()
        if Selected_record:
            receipt_id = self.Selected_receipt_ID[Selected_record[0]]
            record = self.data["user_data"][receipt_id]
            Details_text = f"Customer: {record['customer_name']}\nPickup Date: {record['pickup_date']}\nDropoff Date: {record['dropoff_date']}\nDays Hired: {record['days_hired']}\nSubtotal: ${record['subtotal']:.2f}\nTax: ${record['tax']:.2f}\nTotal: ${record['total']:.2f}\nReturned: {'Yes' if record.get('Has_Returned', False) else 'No'}"
            self.Admin_record_details.config(text=Details_text)
            
            self.Admin_item_list.delete(0, tk.END)
            for item in record["items"]:
                self.Admin_item_list.insert(tk.END, f"{item['name']} x{item['quantity']} - ${item['line_cost']:.2f}")
    # This def was the underlying logic for the password login, the place_forget() does not update the elements under it thus leading to a page refresh needed, this seemed unideal and was scrapped.    
    #def Login_process(self):
    #    if self.Login_password_check.get() == adminpassword:
    #        self.Staff_login_window.place_forget()
    #        self.Login_label.place_forget()
    #        self.Login_entry.place_forget()
    #        self.Login_button.place_forget()
    #        self.Admin_UI_outer.update_idletasks()
    #        self.Record_refresh()
    #        return
    #    else:
    #        messagebox.showerror(title="Incorrect Password",message="The Password is Incorrect")

if __name__ == "__main__":
    root = tk.Tk()
    app = boltbyteproject(root)
    root.mainloop()
    