#The Tkinter library is used to create the UI elements of the program, it is imported as tk to shorten the length of some lines of code
import tkinter as tk
#I specifically import the messagebox and ttk modules because...
#The ttk module is because certain elements in ttk have a module name of TButton while tk has them as button.
#Aswell as this ttk theming isn't compatible with tk modules which make each tk module need individual themeing.
#messagebox was imported because when looking for why it wouldn't work with tk.messagebox i found i could,
#Just import the specific module from tk without having to use and additial declarations.
from tkinter import ttk, messagebox
#I use the datetime library to check the date and have the dropoff date and pickup date automatically fill for one day
#I also use the library to make sure the user cannot input a dropoff date into the past, giving a negative dayprice.
import datetime
#The json library contains the functions I needed to add storing and reading data in a json file
import json
#I imported the os library because when looking at ways to have a flexible filepath it kept coming up
#As a library that has this function.
import os
#The uuid library allows for my program to generate a random string of charactors to be used as an individual
#Identifier for receipts, allowing for users of the same name but differnet hire dates to be stored.
import uuid

#This STORE_ITEMS constant is a list of the items on the store/rentals page of the program.
#An indefinite amount of items can be added as long as they follow the following template
#{"id": "000", "name": "ITEM_NAME", "colour": "COLOURHEXCODE", "dayprice": 0.00},
STORE_ITEMS = [
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
#This GST constant is 0.15 to act as 15% when calculating the taxed amount and the total
GST = 0.15
#The BOLTBYTEFILE constant is a file path for the boltbyte_data.json file.
BOLTBYTEFILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "boltbyte_data.json")
#adminpassword = str("TestPassword")
def load_data():
    '''When called the def will attempt to call the boltbyte_data.json file, and if it doesn't exist it will create a new file named such.'''
    if os.path.exists(BOLTBYTEFILE):
        #This will try to run the code below, and if it encounters the specified error it will run the statement.
        try:
            #This attempts to open the boltbyte_data.json in read mode, under the utf-8 encoding as a variable called file. we can tell its read mode as the "r" means read.
            with open(BOLTBYTEFILE,"r",encoding="utf-8" ) as file:
                #then it attempts to load the json file which is now assigned a local variable called file.
                return json.load(file)
        #This error is specificly for if the file is missing.
        except FileNotFoundError:
            #When the execpt is pulled the code will pass and reach the return statement
            pass
    #when this return statement is run it creates a file nammed boltbyte_data.json with an initial container called user_data
    return {"user_data": {}}

def save_data(data):
    '''This def upon being called will attempt to save any data feed into it to the Boltbyte_data.json file according to its formatting'''
    #This attempts to open the boltbyte_data.json in write mode, under the utf-8 encoding as a variable called file. we can tell its write mode as the "w" means write.
    with open(BOLTBYTEFILE, "w", encoding="utf-8") as file:
        #when this line is run it dumps the data stored in the data parameter (Which is set where ever the def is called)
        #and writes it to the file parameter which is the filepath to boltbyte_data.json file
        json.dump(data,file, indent=4)
class BoltByteProject():
    '''This Class contains every other Def, as to be able to run and rerun certain defs upon the need.'''
    #This def, __init__ is used to declare the self. parameter as to allow other defs with the BoltByteProject class 
    #To use certain variables from other defs when the program is running.
    #it also allows for root to be delcared within it to be used within tkinter modules.
    def __init__(self,root):
        #This loads the json file into the data dict
        self.data = load_data()
        #This declares that the root parameter is the root varaible 
        self.root = root
        #This gives the program a name that can be seen just above the title
        self.root.title("Bolt & Byte Tech Hire Interface")
        #This sizes the progam to 935 pixels by 900 pixels, this is done to fit the amount of items
        self.root.geometry("935x900")
        #This creates an empty cart dict that is used to store the items the user adds
        self.cart = {}
        #this also creates an empty dict, though it is used to store the number of items
        #A user has selected in the items row, its a dict because I use a for loop to generate
        #Each item row
        self.item_amount = {}
        #This creates the main frame every other defs tkinter widgets are stored under
        main_frame = ttk.Frame(root)
        #This makes the frame fill the X axis and Y axis of the program
        main_frame.pack(fill="both")
        #This creates a title on the main frame with the name of the operating company.
        main_title = ttk.Label(main_frame, text="Bolt & Byte Tech Hire",font=("Helvetica", 25))
        #The .pack statement is empty as does not require any changes
        main_title.pack()
        #this style
        style = ttk.Style()

        style.configure("TNotebook",borderwith="0")

        style.theme_use("clam")
        
        self.note_book = ttk.Notebook(root)

        self.note_book.pack(expand = True, fill= 'both', padx=10, pady=10)

        self.rentals = ttk.Frame(self.note_book)
        
        self.returns = ttk.Frame(self.note_book)
        
        self.admin = ttk.Frame(self.note_book)
        
        self.note_book.add(self.rentals, text="Rentals")
        
        self.note_book.add(self.returns, text="Returns")
        
        self.note_book.add(self.admin, text="Staff Access")
        
        self.rentals_ui()
        
        self.returns_ui()
        
        self.admin_ui()
        
    def rentals_ui(self):
        '''This controlls and places everything within the Rentals Notebook page'''
        rentals_outer = ttk.Frame(self.rentals)
        
        rentals_outer.pack(expand=True, fill="both", padx=10, pady=10)
        
        rentals_left = ttk.Frame(rentals_outer,width=500)
        
        rentals_left.pack(side="left", fill="y")
        
        rentals_left.pack_propagate(False)
        
        item_rows_title = ttk.Label(rentals_left, text="Hireable Equipment",font=("Helvetica", 15, "bold"))
        item_rows_title.pack(pady=6)
        
        for item in STORE_ITEMS:
            self.item_rows(rentals_left, item)
            
        rentals_right = ttk.Frame(rentals_outer)
        rentals_right.pack(side="right", fill="y", expand=True, padx=(12,0))
        
        dates = ttk.Labelframe(rentals_right,text="Rental Dates")
        dates.pack(fill="x", padx=(0,6))
        
        self.pickup_date = tk.StringVar(value=datetime.date.today().strftime("%d/%m/%Y"))
        self.dropoff_date = tk.StringVar(value=(datetime.date.today() + datetime.timedelta(days=1)).strftime("%d/%m/%Y"))
        
        self.date_row(dates, "Pickup Date", self.pickup_date,0)
        self.date_row(dates, "Dropoff Date", self.dropoff_date,1)
        
        customer_name = ttk.LabelFrame(rentals_right, name="customer Name")
        customer_name.pack(fill="x", padx=(0,6))
        
        self.name_entry = tk.StringVar()
        rentals_name_entry = ttk.Entry(customer_name, textvariable=self.name_entry, font=("Helvetica", 12), width=24)
        rentals_name_entry.pack(fill="x")
        
        item_cart = ttk.LabelFrame(rentals_right, text="Cart")
        item_cart.pack(fill="x", padx=6)
        
        self.cart_text = tk.Text(item_cart,font=("Courier", 10), relief="solid", bd=1, height=8,bg="#dcdad5",fg="#000000")
        self.cart_text.pack(expand=True, fill="both")
        
        total_price_frame = ttk.Frame(rentals_right)
        total_price_frame.pack(fill="x")
        
        self.days_hired = self.row_totals(total_price_frame, "Duration:", "0 Days", 0)
        self.price_subtotal = self.row_totals(total_price_frame, "Subtotal:", "$0.00", 1)
        self.sales_tax = self.row_totals(total_price_frame,"Sales Tax(15%):","$0.00",2)
        self.total_price = self.row_totals(total_price_frame,"Total Price:","$0.00",3)
        
        rentals_checkout = ttk.Button(rentals_right, text="Checkout",command=self.checkout)
        rentals_checkout.pack(fill="both",padx=(0,6))
        
        self.update_cart()
    
    def item_rows(self, parent, item):
        '''This def creates the all the elements needed to create rows based off of the parameters in STORE_ITEMS'''
        item_rows_frame = tk.Frame(parent, bg=item["colour"], height=60)
        item_rows_frame.pack(fill="x", pady=3, padx=3)
        item_rows_frame.propagate(False)
        
        item_rows_colour = tk.Frame(item_rows_frame, bg=item["colour"])
        item_rows_colour.pack(side="left", fill="both", expand=True, padx=5, pady=3)
        
        item_rows_name = tk.Label(item_rows_colour, text=item["name"], font=("Helvetica", 12, "bold"), bg=item["colour"])
        item_rows_name.pack(anchor="w")
        
        item_rows_price = tk.Label(item_rows_colour, text=f"${item["dayprice"]}/day", font=("Helvetica", 10), bg=item["colour"])
        item_rows_price.pack(anchor="w")
        
        item_rows_button = tk.Frame(item_rows_frame, bg=item["colour"], )
        item_rows_button.pack(side="right", padx=8, pady=3)
        
        item_rows_label = tk.Label(item_rows_button, text="0", font=("Helvetica", 12, "bold"), fg="black", bg=item["colour"], width=2, anchor="center")
        item_rows_label.grid(row=0, column=1, pady=2)
        self.item_amount[item["id"]] = item_rows_label
        
        item_rows_add = tk.Button(item_rows_button, text="+", width=2, font=("Helvetica", 9, "bold"), relief="flat", bg=item["colour"], fg="black", command=lambda i=item: self.cart_change(i, 1))
        item_rows_add.grid(row=0, column=2, padx=(2, 0))
        
        item_rows_minus = tk.Button(item_rows_button, text="−", width=2, font=("Helvetica", 9, "bold"), relief="flat", bg=item["colour"], fg="black", command=lambda i=item: self.cart_change(i, -1))
        item_rows_minus.grid(row=0, column=0, padx=(0, 2))
        
    def date_row(self, parent, label,var, row):
        '''this def creates the rows which are used to enter the pickup and dropoff dates'''
        
        date_row_title = ttk.Label(parent, text=label, font=("Helvetica", 10), width=12, anchor="w")
        date_row_title.grid(row=row, column=0, padx=6, pady=2)
        
        date_row_entry = ttk.Entry(parent,textvariable=var, font=("Helvetica", 10),width=12,)
        date_row_entry.grid(row=row, column=1, padx=6, pady=2)
        
        date_row_entry.bind("<FocusOut>", lambda run: self.update_cart())
        
    def row_totals(self, parent, item, value,row):
        '''This def creates the rows which are assigned to Tax, Subtotal, Total, and the total Rental length'''
        row_totals_title = ttk.Label(parent, text=item, font=("Helvetica", 10), anchor="w")
        row_totals_title.grid(row=row, column=0, sticky="e")
        
        row_totals_value = ttk.Label(parent, text=value, font=("Helvetica", 10), anchor="w")
        row_totals_value.grid(row=row, column=1, sticky="e")
        
        return row_totals_value
        
    def cart_change(self, item, delta):
        '''This def is used to add items to the "Cart" when an user presses the + button in an item rows button'''
        current_cart = self.cart.get(item["id"], 0)
        new_cart = max(0, current_cart + delta)
        if new_cart == 0:
            self.cart.pop(item["id"], None)
        else:
            self.cart[item["id"]] = new_cart
        self.item_amount[item["id"]].config(text=str(new_cart))
        self.update_cart()
    def days_duration(self):
        '''This def calculates the total amount of days the user has hired their items for, it will always default to 1 unless specified by the user'''
        try:
            pickup = datetime.datetime.strptime(self.pickup_date.get().strip(), "%d/%m/%Y").date()
            dropoff = datetime.datetime.strptime(self.dropoff_date.get().strip(), "%d/%m/%Y").date()
            days_total = (dropoff - pickup).days
            return days_total
        except ValueError:
            return 1
    
    def update_cart(self):
        '''This def displays the items in the cart when they are added'''
        days_total = self.days_duration()
        items_in_cart = {i["id"]: i for i in STORE_ITEMS}

        cart_lines = []
        sub_total = 0.0
        for item_id, amount in self.cart.items():
            item = items_in_cart[item_id]
            line_cost = item["dayprice"] * amount * days_total
            sub_total += line_cost
            cart_lines.append(f"{item['name']} x{amount}  ${line_cost}")

        tax_total = sub_total * GST
        total = sub_total + tax_total

        self.cart_text.config(state="normal")
        self.cart_text.delete("1.0", tk.END)
        
        if cart_lines:
            header = f"{'Item'} Amount  {'Cost'}\n" + "─" * 38 + "\n"
            self.cart_text.insert(tk.END, header + "\n".join(cart_lines))
        else:
            self.cart_text.insert(tk.END, "  No items in cart.")
            
        self.cart_text.config(state="disabled")

        self.days_hired.config(text=f"{days_total} day{'s' if days_total != 1 else ''}")
        self.price_subtotal.config(text=f"${sub_total:.2f}")
        self.sales_tax.config(text=f"${tax_total:.2f}")
        self.total_price.config(text=f"${total:.2f}")
        
    def checkout(self):
        '''This def handles the checkout process when the checkout button is pressed, and the saving of the data generated by the process.'''
        checkout_name = self.name_entry.get()
        checkout_name_check = False
        while checkout_name_check is False:
            checkout_name = checkout_name.strip()
            checkout_name_check = checkout_name.isalpha()
            if checkout_name_check is True:
                pass
            else:
                messagebox.showerror(title="Name Error",message="Username must not contain any non alphabet charactors.\n Please reenter your name")
                return
        checkout_date_check_p = False
        checkout_date_check_d = False
        while checkout_date_check_d is False and checkout_date_check_p is False:
            try:
                pickup = datetime.datetime.strptime(self.pickup_date.get().strip(), "%d/%m/%Y").date()
                dropoff = datetime.datetime.strptime(self.dropoff_date.get().strip(), "%d/%m/%Y").date()
                checkout_date_check_p = True
                checkout_date_check_d = True
            except ValueError:
                messagebox.showwarning(title="Date Error: Incorrect Format",message="The Format of the Hire dates is incorrect \n please reenter your start and end hire dates")
                return
            if checkout_date_check_p is True and checkout_date_check_d is True:
                if pickup > dropoff:
                    messagebox.showinfo(title="Date Time Error",message="Pickup date is greater than dropoff date, \n please reenter your Hire dates.")
                    return
                elif pickup < dropoff:
                    pass
                else:
                    messagebox.showerror(title="Unknown error",message="Unknown error within Dates, reenter your start and end hire dates.")
                    return
            else:
                messagebox.showerror(title="Date Error",message="Please do not input any alphabet charactors in the date fields. \n Please reenter your the Dates")
                return
                
            
        if not self.cart:
            messagebox.showwarning("Cart is empty", "Please add items to cart to proceed.")
            return

        days_total = self.days_duration()
        checkout_items = {i["id"]: i for i in STORE_ITEMS}
        ordered_items = []
        sub_total = 0.0
        for item_id, amount in self.cart.items():
            item = checkout_items[item_id]
            line_cost = item["dayprice"] * amount * days_total
            sub_total += line_cost
            ordered_items.append({"Id": item_id,"Name": item["name"],"Amount": amount,"Cost": line_cost})

        tax_total = sub_total * GST
        total = sub_total + tax_total 
        receipt_id = str(uuid.uuid4())[:8].upper()
        times_returned = int(0)
        #Refer to why Has_Returned is commented out to the search_dates def
        record = {
            "receipt_id": receipt_id,
            "customer_name": checkout_name,
            "pickup_date": self.pickup_date.get().strip(),
            "dropoff_date": self.dropoff_date.get().strip(),
            "days_hired": days_total,
            "items": ordered_items,
            "subtotal": sub_total,
            "tax": tax_total,
            "total": total,
            "timestamp": datetime.datetime.now().isoformat(),
            "Returned": times_returned, # 0 is not returned 1 is returned
            #"Has_Returned": False
        }

        self.data["user_data"][receipt_id] = record
        save_data(self.data)
        
        for item_id in self.cart:
            self.item_amount[item_id].config(text="0")
            
        self.cart.clear()
        
        self.update_cart()
        
        self.name_entry.set("")

        self.record_refresh()
        
        self.checkout_bill(record)
        
        return record
        
    def checkout_bill(self, record):
        '''5'''
        bill_window = tk.Toplevel(self.root)
        bill_window.title("Rental Receipt")
        bill_window.geometry("400x500")
        
        bill_title = ttk.Label(bill_window, text="Bolt & Byte Tech Hire", font=("Helvetica", 16, "bold"))
        bill_title.pack(pady=10)
        
        bill_receipt_id =ttk.Label(bill_window, text=f"Receipt ID: {record['receipt_id']}")
        bill_receipt_id.pack()
        
        bill_timestamp = ttk.Label(bill_window, text=f"Date: {record['timestamp'][:10]}")
        bill_timestamp.pack()
        
        bill_linebreak = ttk.Label(bill_window, text="------------------------------")
        bill_linebreak.pack(pady=5)
        
        bill_customer_name = ttk.Label(bill_window, text=f"Customer: {record['customer_name']}")
        bill_customer_name.pack()
        
        bill_pickup_date = ttk.Label(bill_window, text=f"Pickup Date: {record['pickup_date']}")
        bill_pickup_date.pack()
        
        bill_dropoff_date = ttk.Label(bill_window, text=f"Dropoff Date: {record['dropoff_date']}")
        bill_dropoff_date.pack()
        
        bill_items_header = ttk.Label(bill_window, text="Items Rented:", font=("Helvetica", 12, "bold"))
        bill_items_header.pack(pady=10)

        for items in record["items"]:
            bill_items = ttk.Label(bill_window, text=f"{items['Name']} x{items['Amount']} - ${items['Cost']}")
            bill_items.pack(anchor="center", padx=20)

        bill_subtotal = ttk.Label(bill_window, text=f"Subtotal: ${record['subtotal']}")
        bill_subtotal.pack(pady=5)
        
        bill_tax = ttk.Label(bill_window, text=f"Tax ({int(GST*100)}%): ${record['tax']}")
        bill_tax.pack(pady=5)
        
        bill_total = ttk.Label(bill_window, text=f"Total: ${record['total']}", font=("Helvetica", 12, "bold"))
        bill_total.pack(pady=10)
        
        bill_close = ttk.Button(bill_window, text="Close", command=bill_window.destroy)
        bill_close.pack(pady=10)
        
    def returns_ui(self):
        '''6'''
        receipt_frame = ttk.LabelFrame(self.returns, text="Search Rental Receipt")
        receipt_frame.pack(anchor="n" ,fill="x",padx=6, pady=4)
        
        receipt_id_frame = ttk.Frame(receipt_frame)
        receipt_id_frame.pack(fill="x")
        
        self.receipt_id_entry = ttk.Entry(receipt_id_frame, font=("Helvetica", 10), width=36)
        self.receipt_id_entry.pack(side="left", padx=6, pady=2, expand=True, fill="x")
        
        ttk.Button(receipt_id_frame, text="Search", command=self.search_receipt).pack(side="right", padx=6, pady=2)
        
        receipt_forget_frame = ttk.LabelFrame(self.returns, text="Forgot your Receipt? Use your Name or Pickup/Dropoff Date")
        receipt_forget_frame.pack(expand=True, anchor="center",fill="x",padx=6, pady=4)
        
        receipt_name = ttk.LabelFrame(receipt_forget_frame, text="Remeber the Name you used? Use this Box!",)
        receipt_name.pack(expand=True, anchor="n",fill="x",padx=6, pady=4)
        
        self.receipt_name_entry = ttk.Entry(receipt_name, font=("Helvetica", 10), width=36)
        self.receipt_name_entry.pack(expand=True, side="left", padx=5, pady=2, fill="x")
        
        ttk.Button(receipt_name, text="Search", command=self.search_name,).pack(side="right", padx=6, pady=2)
        
        receipts_dates = ttk.LabelFrame(receipt_forget_frame, text="Remember your Pickup/Dropoff Date? Use this Box!",)
        receipts_dates.pack(expand=True, anchor="n",fill="x",padx=6, pady=4)

        
        receipt_dates_pickup_label = ttk.Labelframe(receipts_dates, text="Date of Pickup")
        receipt_dates_pickup_label.pack(side="left", padx=5, pady=20, expand=True, fill="x")
        self.receipts_dates_pickup = ttk.Entry(receipt_dates_pickup_label, font=("Helvetica", 10), width=36)
        self.receipts_dates_pickup.pack(side="left", padx=5, pady=20, expand=True, fill="x")
        
        receipt_dates_dropoff_label = ttk.Labelframe(receipts_dates, text="Date of Dropoff")
        receipt_dates_dropoff_label.pack(side="left", padx=5, pady=20, expand=True, fill="x")
        self.receipts_dates_dropoff = ttk.Entry(receipt_dates_dropoff_label, font=("Helvetica", 10), width=36)
        self.receipts_dates_dropoff.pack(side="left", padx=5, pady=20, expand=True, fill="x")
        
        ttk.Button(receipts_dates, text="Search", command=self.search_dates).pack(side="left", padx=6, pady=2)
        return
    
    def search_receipt(self):
        '''7'''
        #commented out any section that included "Has_Returned", I cannot understand why it will not play nicely with
        #bool values in reading from json files and am not willing to use this method to counteract dupelicate returns
        receipt_id = self.receipt_id_entry.get().strip()
        if receipt_id in self.data["user_data"] and self.data["user_data"][receipt_id]["Returned"] == 0:
        #and self.data["user_data"][receipt_id]["Has_Returned"] == "false":
            record = self.data["user_data"][receipt_id]
            self.checkout_bill(record)
            #self.data["user_data"]["Has_Returned"] = True
            self.data["user_data"][receipt_id]["Returned"] = 1
            save_data(self.data)
        elif receipt_id not in self.data["user_data"]:
            messagebox.showerror("Not Found", "No receipt found with that Receipt ID.")
        #elif self.data["user_data"][receipt_id]["Has_Returned"] == "true":
        #    messagebox.showerror("This Receipt has already been returned")
        elif self.data["user_data"][receipt_id]["Returned"] > 0:
            messagebox.showerror(title="This receipt has already been returned",message="Contact your local Bolt & Byte Tech staff for support")
        else:
            messagebox.showerror(title="Unknown or Unexpected Error", message="Contact your administrator for support")
        
    def search_name(self):
        '''7'''
        name_search = self.receipt_name_entry.get().strip()
        for record_id, record in self.data["user_data"].items():
            if record["customer_name"] == name_search:
                if record.get("Returned",0) == 0:
                    self.checkout_bill(record)
                    #self.data["user_data"]["Has_Returned"] = True
                    record["Returned"] = 1
                    save_data(self.data)
                    return
                else:
                    messagebox.showerror(title="This receipt has already been returned",message="Contact your local Bolt & Byte Tech staff for support")
                    return

        messagebox.showerror(title="Not Found",message="No receipt found with that customer name.")
        
    def search_dates(self):
        '''9'''
        date_search_pickup = self.receipts_dates_pickup.get()
        date_search_dropoff = self.receipts_dates_dropoff.get()
        for record_id, record in self.data["user_data"].items():
            if record["pickup_date"] == date_search_pickup and record["dropoff_date"] == date_search_dropoff:
                if record.get("Returned",0) == 0:
                    self.checkout_bill(record)
                    #self.data["user_data"]["Has_Returned"] = True
                    record["Returned"] = 1
                    save_data(self.data)
                    return
                else:
                    messagebox.showerror(title="This receipt has already been returned",message="Contact your local Bolt & Byte Tech staff for support")
                    return
            else:
                messagebox.showerror(title="Not Found", message="No product hire with those dates")
                return
        messagebox.showerror(title="Unknown or Unexpected Error", message="Contact your administrator for support")
        
    def admin_ui(self):
        '''10'''
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

        admin_ui_outer = ttk.Frame(self.admin)
        admin_ui_outer.pack(expand=True, fill="both", padx=10, pady=10)
        
        admin_ui_left = ttk.Frame(admin_ui_outer, width=350,)
        admin_ui_left.pack(side="left", fill="y")
        admin_ui_left.pack_propagate(False)
        
        ttk.Label(admin_ui_left, text="Rental Records", font=("Helvetica", 15, "bold")).pack(pady=6)
        
        admin_record_listbox = ttk.Frame(admin_ui_left)
        admin_record_listbox.pack(expand=True, fill="both", padx=6, pady=6)        
        admin_scrollbar = ttk.Scrollbar(admin_record_listbox)
        admin_scrollbar.pack(side="right", fill="y")
        
        self.admin_record_list = tk.Listbox(admin_record_listbox, font=("Helvetica", 12),bg="#DCDAD5",fg="black", yscrollcommand=admin_scrollbar.set)
        self.admin_record_list.pack(side="left", expand=True, fill="both")        
        admin_scrollbar.configure(command=self.admin_record_list.yview)
        self.admin_record_list.bind("<<ListboxSelect>>", self.record_show)
        
        admin_right = ttk.Frame(admin_ui_outer)
        admin_right.pack(side="right", fill="both", expand=True, padx=(12,0))        
        self.admin_record_title = ttk.Label(admin_right, text="Receipt details", font=("Helvetica", 10))
        self.admin_record_title.pack(anchor="w")
        
        self.admin_record_details = ttk.Label(admin_right,text="",font=("Helvetica", 10),relief="solid")
        self.admin_record_details.pack(anchor="w", expand=True, fill="both", padx=6, pady=6)
        
        admin_item_hired = ttk.Label(admin_right, text="Items Hired", font=("Helvetica", 12))
        admin_item_hired.pack(pady=10)
        
        admin_item_hired = ttk.Frame(admin_right, relief="solid")
        admin_item_hired.pack(expand=True, fill="both", padx=6, pady=6)
        
        admin_item_scrollbar = ttk.Scrollbar(admin_item_hired)
        admin_item_scrollbar.pack(side="right", fill="y")
        
        self.admin_item_list = tk.Listbox(admin_item_hired,font=("Helvetica", 10) ,bg="#DCDAD5" ,fg="black" , yscrollcommand=admin_item_scrollbar.set)
        self.admin_item_list.pack(side="left", expand=True, fill="both")
        
        admin_item_scrollbar.configure(command=self.admin_item_list.yview)
        
        admin_totals = ttk.Label(admin_right, text="", font=("Helvetica", 12, "bold"),)
        admin_totals.pack(anchor="w", pady=8)
        
        ttk.Button(admin_right, text="Copy record to Clipboard", command=self.copy_record).pack(pady=4)
        ttk.Button(admin_right, text="Delete Record", command=self.delete_record).pack(pady=4)
        
        # self.Staff_login_window.tkraise()
        # Part of the commented out Login page.

        self.selected_receipt_id = ""

        self.record_refresh()
    
    def record_refresh(self):
        '''11'''
        self.admin_record_list.delete(0, tk.END)
        self.selected_receipt_id = []
        for receipt_id, record in self.data["user_data"].items():
            self.admin_record_list.insert(tk.END, f" #{receipt_id} {record['customer_name']} \n {record['pickup_date']}")
            self.selected_receipt_id.append(receipt_id)
    def delete_record(self):
        '''12'''
        delete_id = self.selected_receipt_id[self.admin_record_list.curselection()[0]]
        delete_confirm = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this record? This action cannot be undone.")
        if delete_confirm:
            self.data["user_data"].pop(delete_id, None)
            save_data(self.data)
            self.record_refresh()
    def copy_record(self):
        '''13'''
        if self.selected_receipt_id:
            selected_record = self.admin_record_list.curselection()
            if selected_record:
                receipt_id = self.selected_receipt_id[selected_record[0]]
                record = self.data["user_data"][receipt_id]
                record_text = json.dumps(record, indent=4)
                self.root.clipboard_clear()
                self.root.clipboard_append(record_text)
                messagebox.showinfo("Copied", "Record copied to clipboard.")
            else:
                messagebox.showwarning("No Selection", "Please select a record to copy.")
        else:
            messagebox.showwarning("No Records", "There are no records to copy.")
            
    def record_show(self,event):
        '''13'''
        selected_record = self.admin_record_list.curselection()
        if selected_record:
            receipt_id = self.selected_receipt_id[selected_record[0]]
            record = self.data["user_data"][receipt_id]
            details_text = f"Customer: {record['customer_name']}\nPickup Date: {record['pickup_date']}\nDropoff Date: {record['dropoff_date']}\nDays Hired: {record['days_hired']}\nSubtotal: ${record['subtotal']:.2f}\nTax: ${record['tax']:.2f}\nTotal: ${record['total']:.2f}\nReturned: {'Yes' if record.get('Returned', 1) else 'No'}"
            self.admin_record_details.config(text=details_text)
            
            self.admin_item_list.delete(0, tk.END)
            for item in record["items"]:
                self.admin_item_list.insert(tk.END, f"{item['Name']} x{item['Amount']} - ${item['Cost']:.2f}")
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
    app = BoltByteProject(root)
    root.mainloop()
    