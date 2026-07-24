<<<<<<< HEAD
# The Tkinter library is used to create the UI elements of the program, it is imported as tk to shorten the length of some lines of code.
import tkinter as tk
# I specifically import the messagebox and ttk modules because...
# The ttk module is because certain elements in ttk have a module name of TButton while tk has them as button.
# Aswell as this ttk theming isn't compatible with tk modules which make each tk module need individual themeing.
# Messagebox was imported because when looking for why it wouldn't work with tk.messagebox i found i could,.
# Just import the specific module from tk without having to use and additial declarations.
from tkinter import ttk, messagebox
# I use the datetime library to check the date and have the dropoff date and pickup date automatically fill for one day.
# I also use the library to make sure the user cannot input a dropoff date into the past, giving a negative dayprice.
import datetime
# The json library contains the functions I needed to add storing and reading data in a json file.
import json
# I imported the os library because when looking at ways to have a flexible filepath it kept coming up.
# As a library that has this function.
import os
# The uuid library allows for my program to generate a random string of charactors to be used as an individual.
# Identifier for receipts, allowing for users of the same name but differnet hire dates to be stored.
import uuid

# This STORE_ITEMS constant is a list of the items on the store/rentals page of the program.
# An indefinite amount of items can be added as long as they follow the following template.
# {"id": "000", "name": "ITEM_NAME", "colour": "COLOURHEXCODE", "dayprice": 0.00},.
=======
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
>>>>>>> 4e0745e (Commenting Code, Penultimate Commit)
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
<<<<<<< HEAD
# This GST constant is 0.15 to act as 15% when calculating the taxed amount and the total.
GST = 0.15
# The BOLTBYTEFILE constant is a file path for the boltbyte_data.json file.
BOLTBYTEFILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "boltbyte_data.json")
# Adminpassword = str("TestPassword").
def load_data():
    '''When called the def will attempt to call the boltbyte_data.json file, and if it doesn't exist it will create a new file named such.'''
    if os.path.exists(BOLTBYTEFILE):
        # This will try to run the code below, and if it encounters the specified error it will run the statement.
        try:
            # This attempts to open the boltbyte_data.json in read mode, under the utf-8 encoding as a variable called file. we can tell its read mode as the "r" means read.
            with open(BOLTBYTEFILE,"r",encoding="utf-8" ) as file:
                # Then it attempts to load the json file which is now assigned a local variable called file.
                return json.load(file)
        # This error is specificly for if the file is missing.
        except FileNotFoundError:
            # When the execpt is pulled the code will pass and reach the return statement.
            pass
    # When this return statement is run it creates a file nammed boltbyte_data.json with an initial container called user_data.
=======
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
>>>>>>> 4e0745e (Commenting Code, Penultimate Commit)
    return {"user_data": {}}

def save_data(data):
    '''This def upon being called will attempt to save any data feed into it to the Boltbyte_data.json file according to its formatting'''
<<<<<<< HEAD
    # This attempts to open the boltbyte_data.json in write mode, under the utf-8 encoding as a variable called file. we can tell its write mode as the "w" means write.
    with open(BOLTBYTEFILE, "w", encoding="utf-8") as file:
        # When this line is run it dumps the data stored in the data parameter (Which is set where ever the def is called).
        # And writes it to the file parameter which is the filepath to boltbyte_data.json file.
        json.dump(data,file, indent=4)
class BoltByteProject():
    '''This Class contains every other Def, as to be able to run and rerun certain defs upon the need.'''
    # This def, __init__ is used to declare the self. parameter as to allow other defs with the BoltByteProject class .
    # To use certain variables from other defs when the program is running.
    # It also allows for root to be delcared within it to be used within tkinter modules.
    def __init__(self,root):
        # This loads the json file into the data dict.
        self.data = load_data()
        # This declares that the root parameter is the root varaible .
        self.root = root
        # This gives the program a name that can be seen just above the title.
        self.root.title("Bolt & Byte Tech Hire Interface")
        # This sizes the progam to 935 pixels by 900 pixels, this is done to fit the amount of items.
        self.root.geometry("935x900")
        # This creates an empty cart dict that is used to store the items the user adds.
        self.cart = {}
        # This also creates an empty dict, though it is used to store the number of items.
        # A user has selected in the items row, its a dict because I use a for loop to generate.
        # Each item row.
        self.item_amount = {}
        # This creates the main frame every other defs tkinter widgets are stored under.
        main_frame = ttk.Frame(root)
        # This makes the frame fill the X axis and Y axis of the program.
        main_frame.pack(fill="both")
        # This creates a title on the main frame with the name of the operating company.
        main_title = ttk.Label(main_frame, text="Bolt & Byte Tech Hire",font=("Helvetica", 25))
        # The .pack statement is empty as does not require any changes.
        main_title.pack()
        # This style variable is used to implement the theme styles from ttk.
        style = ttk.Style()
        # This uses the styling from ttk to change the borderwidth of the Notebook buttons to not show.
        style.configure("TNotebook",borderwidth="0")
        # This uses the style componet to theme every widget and unifiy the styles,.
        # This was done to ensure cross compatability with MacOS in styles as MacOS does not respect certain tk componets.
        style.theme_use("clam")
        # Creates a notebook to hold the three main tabs.
        self.note_book = ttk.Notebook(root)
        # Makes the notebook expand when the program resizes, and the x and y axis when created.
        # Gives it a 10 pixel spacing from the edge of the main frame.
        self.note_book.pack(expand=True, fill='both', padx=10, pady=10)
        # Creates a Notebook Frame for to be used for the notebook.
        self.rentals = ttk.Frame(self.note_book)
        # Creates a Notebook Frame for to be used for the notebook.
        self.returns = ttk.Frame(self.note_book)
        # Creates a Notebook Frame for to be used for the notebook.
        self.admin = ttk.Frame(self.note_book)
        # This connects the rentals frame to the actual notebook, and gives it a title.
        self.note_book.add(self.rentals, text="Rentals")
        # This connects the returns frame to the actual notebook, and gives it a title.
        self.note_book.add(self.returns, text="Returns")
        # This connects the admin frame to the actual notebook, and gives it a title.
        self.note_book.add(self.admin, text="Staff Access")
        # This runs the rentals def which loads everything actually in the rentals tab into memory.
        self.rentals_ui()
        # This runs the returns def which loads everything actually in the returns tab into memory.
        self.returns_ui()
        # This runs the admin def which loads everything actually in the admin tab into memory.
        self.admin_ui()
        
    def rentals_ui(self):
        '''This controlls and places everything within the Rentals Notebook page'''
        # This Frame is the frame that links the widgets inside the rentals tab to the actual tab itself.
        # This is done by calling self.rentals instead of calling root as the master/parrent of this frame.
        rentals_main = ttk.Frame(self.rentals)
        # This .pack makes the frame expand when the program resizes, and fill the x and y axis when created.
        # Gives it a 10 pixel spacing from the edge of the main frame.
        rentals_main.pack(expand=True, fill="both", padx=10, pady=10)
        # This creates the left frame, which contains the item rows.
        rentals_left = ttk.Frame(rentals_main,width=500)
        # Makes the left frame stay to the left side...
        # Fills from the top to the bottom of main frame.
        rentals_left.pack(side="left", fill="y")
        # Disables the frames autofitting to fit the widgits it contains.
        # This essentially locks the frame to its specified size.
        rentals_left.pack_propagate(False)
        # Puts a title at the top of the rentals_left frame.
        item_rows_title = ttk.Label(rentals_left, text="Hireable Equipment",font=("Helvetica", 15, "bold"))
        # Spaces the title label 6 pixels from the top of the rentals_left frame.
        item_rows_title.pack(pady=6)
        # For each entry in STORE_ITEMS runs the item_rows def.
        for item in STORE_ITEMS:
            # Calls item_rows, assigns it to rentals_left and uses data within STORE_ITEMS to fit parameters within the item_rows def.
            self.item_rows(rentals_left, item)
        # Creates a rentals frame for the right side of the tab.
        rentals_right = ttk.Frame(rentals_main)
        # Makes the frame stay to the east side, fills to the top and bottom of the rentals_main frame.
        # Expends when the frame resizes, and is spaced 12 pixels from the west.
        rentals_right.pack(side="right", fill="y", expand=True, padx=(12,0))
        # Creates frame with the title "Rental Dates" under the rentals_right frame.
        dates = ttk.Labelframe(rentals_right,text="Rental Dates")
        # Makes the dates frame fill the x-axis with a 6 pixel spacing to the east.
        dates.pack(fill="x", padx=(0,6))
        # Creates a stringvar that stores the current days date which is pulled from datetime.
        self.pickup_date = tk.StringVar(value=datetime.date.today().strftime("%d/%m/%Y"))
        # Creates a stringvar that stores the current days date which is pulled from datetime.
        # Then adds that date to the change in time by one day, which sets the stringvar.
        # To tomorrows date.
        self.dropoff_date = tk.StringVar(value=(datetime.date.today() + datetime.timedelta(days=1)).strftime("%d/%m/%Y"))
        # These two statements create a row of widgets following the rules set within the date_row def.
        # This statement creates the row of elements, parrented off the dates labelframe.
        # It uses "Pickup Date" as the "item" parameter for dates_row.
        # The pickup_date stringvar is used for the value parameter and the 0 is used as the value for the row parameter.
        self.date_row(dates, "Pickup Date", self.pickup_date,0)
        # This statement creates the row of elements, parrented off the dates labelframe.
        # It uses "Dropoff Date" as the "item" parameter for dates_row.
        # The dropoff_date stringvar is used for the value parameter and the 1 is used as the value for the row parameter.
        self.date_row(dates, "Dropoff Date", self.dropoff_date,1)
        # Creates a LabelFrame with the title "customer Name" under the rentals_right frame.
        customer_name = ttk.LabelFrame(rentals_right, text="Customer Name")
        # Adjusts the frame to fill the x axis and with a spacing of six pixels to the east.
        customer_name.pack(fill="x", padx=(0,6))
        # Creates a stringvar to hold the user's name when input.
        self.name_entry = tk.StringVar()
        # Creates an Entry box under the customer_name labelframe using the name_entry stringvar.
        rentals_name_entry = ttk.Entry(customer_name, textvariable=self.name_entry, font=("Helvetica", 12), width=24)
        # Makes the entry box fill on the x axis.
        rentals_name_entry.pack(fill="x")
        # Creates a labelframe titled cart under the rentals_right frame.
        item_cart = ttk.LabelFrame(rentals_right, text="Cart")
        # Makes the item_cart label frame fill the x axis with padding to the west and east of 6 pixels.
        item_cart.pack(fill="x", padx=6)
        # Creates a text widget parrented to the item_cart labelframe.
        self.cart_text = tk.Text(item_cart,font=("Courier", 10), relief="solid", bd=1, height=8,bg="#dcdad5",fg="#000000")
        # Makes the text widget auto expand on program resize and fill the x and y axis.
        self.cart_text.pack(expand=True, fill="both")
        # Creates a frame to hold the totals values parrented to rentals_right.
        total_price_frame = ttk.Frame(rentals_right)
        # Makes the frame fill on the x axis.
        total_price_frame.pack(fill="x")

        # Creates four rows of widgets following the rules set within the row_totals def.
        # The first parameter is the frame it parrents off, used to fill the parrent parameter.
        # The second parameter is the title/name of the row, used to fill the item parameter.
        # The third parameter is the specifc value of the row, used to fill the row parameter.
        # The forth parameter is used to indicate which row the row should be placed on.
        
        # Creates a row to indicate the amount of days the rental will cover.
        # Days are found by finding the difference between pickup and dropoff dates.
        self.days_hired = self.row_totals(total_price_frame, "Duration:", "0 Days", 0)
        # Creates a row to indicate the subtotal price, before tax.
        # Found by multiplying item costs in STORE_ITEMS  by duration of hire.
        self.price_subtotal = self.row_totals(total_price_frame, "Subtotal:", "$0.00", 1)
        # Creates a row to indicate amount of tax the order will cost.
        # Found by multiplying subtotal by GST and using that value.
        self.sales_tax = self.row_totals(total_price_frame,"Sales Tax(15%):","$0.00",2)
        # Creates a row that shows the total cost of the hire.
        # Value is found by adding sales tax to subtotal.
        self.total_price = self.row_totals(total_price_frame,"Total Price:","$0.00",3)
        # Creates a button titled checkout that called the checkout def, parrented to rentals_right.
        rentals_checkout = ttk.Button(rentals_right, text="Checkout",command=self.checkout)
        # Fills the x and y axis, with padding of 6 pixels to the east.
        rentals_checkout.pack(fill="both",padx=(0,6))
        # Calls the update_cart def when the rentals_ui def is called.
=======
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
        
>>>>>>> 4e0745e (Commenting Code, Penultimate Commit)
        self.update_cart()
    
    def item_rows(self, parent, item):
        '''This def creates the all the elements needed to create rows based off of the parameters in STORE_ITEMS'''
<<<<<<< HEAD
        # Parameters: parent, item. the parent parameter is provided when the def item_rows is called, the item parameter is pulled from STORE_ITEMS.
        # Creates a frame parrented off the parrent parameter, coloured to the colour attached to the item parameter.
        item_rows_frame = tk.Frame(parent, bg=item["colour"], height=60)
        # Makes the frame fill the x axis, with a padding of 3 pixels on the x and y axis.
        item_rows_frame.pack(fill="x", pady=3, padx=3)
        # Disables the frames autofitting to fit the widgits it contains.
        # This essentially locks the frame to its specified size.
        item_rows_frame.propagate(False)
        # This creates a frame parreted of the item_rows_frame frame.
        item_rows_colour = tk.Frame(item_rows_frame, bg=item["colour"])
        # #makes the frame fill the both axes, with a padding of 3 pixels on the x axis and 5 pixels on the y axis.
        item_rows_colour.pack(side="left", fill="both", expand=True, padx=5, pady=3)
        # Adds a label to the the item_rows_colour that parrents its text off the name of the item in STORE_ITEMS and its colour off the same item.
        item_rows_name = tk.Label(item_rows_colour, text=item["name"], font=("Helvetica", 12, "bold"), bg=item["colour"])
        # Anchors the widget to the west(left).
        item_rows_name.pack(anchor="w")
        # Adds a label under the name label that states the price of the item per day, pulls that value from the dayprice field in STORE_ITEMS.
        item_rows_price = tk.Label(item_rows_colour, text=f"${item["dayprice"]}/day", font=("Helvetica", 10), bg=item["colour"])
        # Anchors the widget to the west(left).
        item_rows_price.pack(anchor="w")
        # Creates a frame that contains the add/remove item buttons and the counter that counts how many of the item there are in the cart.
        item_rows_button_frame = tk.Frame(item_rows_frame, bg=item["colour"], )
        # Attaches the button frame to the rightside of the item_rows frame, has 8 pixels of padding on the x axis and 3 on the y axis.
        item_rows_button_frame.pack(side="right", padx=8, pady=3)
        # Creates a label that displays the amount of the item is in the cart.
        item_rows_amount = tk.Label(item_rows_button_frame, text="0", font=("Helvetica", 12, "bold"), fg="black", bg=item["colour"], width=2, anchor="center")
        # Uses the .grid to align the widget on the row 0 in the column, with 2 pixels of padding on the y axis.
        item_rows_amount.grid(row=0, column=1, pady=2)
        # Controls the number in the text of item_rows amount by checking the item_amount of the item id.
        self.item_amount[item["id"]] = item_rows_amount
        # Creates a button that reduces the amount of items in the cart. this is done by calling cart_change, with the information of the item parameter, and adjusts it by 1.
        item_rows_add = tk.Button(item_rows_button_frame, text="+", width=2, font=("Helvetica", 9, "bold"), relief="flat", bg=item["colour"], fg="black", command=lambda: self.cart_change(item, 1))
        # Uses the .grid to align the widget on the row 0 in column 2, with 2 pixels of padding on the x axis from the west.
        item_rows_add.grid(row=0, column=2, padx=(2, 0))
        # Creates a button that reduces the amount of items in the cart. this is done by calling cart_change, with the information of the item parameter, and adjusts it by -1.
        item_rows_minus = tk.Button(item_rows_button_frame, text="−", width=2, font=("Helvetica", 9, "bold"), relief="flat", bg=item["colour"], fg="black", command=lambda: self.cart_change(item, -1))
        # Uses the .grid to align the widget on the row 0 in column 0, with 2 pixels of padding on the x axis from the east.
        item_rows_minus.grid(row=0, column=0, padx=(0, 2))
        
    def date_row(self, parent, label,var, row_num):
        '''this def creates the rows which are used to enter the pickup and dropoff dates'''
        # Parameters: parent, label, var, row_num. all these parameters are provided when the def is called.
        # Creates a label, using the parameters specified when date_row was called. .
        date_row_title = ttk.Label(parent, text=label, font=("Helvetica", 10), width=12, anchor="w")
        # Places the title label on the row the row parameter provides, in column 0 and gives the widget padding 6 pixels of padding on the x axis and 2 on the y axis.
        date_row_title.grid(row=row_num, column=0, padx=6, pady=2)
        # Creates an entrybox using the parameters provided, parent as the parent, var as the txtvar.
        date_row_entry = ttk.Entry(parent,textvariable=var, font=("Helvetica", 10),width=12,)
        # Places the date_row entry on the row the row parameter provides, in column 1 and gives the widget padding 6 pixels of padding on the x axis and 2 on the y axis.
        date_row_entry.grid(row=row_num, column=1, padx=6, pady=2)
        # When the date_row_entry value is edited, this statement is run and updates the cart.
        # Lambda is required in this statement because update_cart requires it to be able to constantly update the prices.(also to not throw an error).
        date_row_entry.bind("<FocusOut>", lambda: self.update_cart())
        
    def row_totals(self, parent, item, value,row_num):
        '''This def creates the rows which are assigned to Tax, Subtotal, Total, and the total Rental length'''
        # Parameters: parent, label, value, row_num. all these parameters are provided when the def is called.
        # Creates a title using the parameters provided, parrent as the parrent, item as the text.
        row_totals_title = ttk.Label(parent, text=item, font=("Helvetica", 10), anchor="w")
        # Places the title label on the row the row parameter provides, in column 0. attaches the widget to the east side.
        row_totals_title.grid(row=row_num, column=0, sticky="e")
        # Creates a title using the parameters provided, parrent as the parrent, item as the text.
        row_totals_value = ttk.Label(parent, text=value, font=("Helvetica", 10), anchor="w")
        # Places the value label on the row the row parameter provides, in column 1. attaches the widget to the east side.
        row_totals_value.grid(row=row_num, column=1, sticky="e")
        # When called returns the row_totals_value which updates the number part of value with the value provided eg:( Total Days: 0 to Total Days: 12 ).
        return row_totals_value
        
    def cart_change(self, item, delta):
        '''This def is used to add items to the "Cart" when an user presses the + button in an item rows button'''
        # Parameters: item, delta. item is the item in cart dict and delta is the change from item_rows(± 1).
        # If the delta is not a negative or removal of an item the code below runs.
        if delta > 0:
            # Gets the current amount in the cart of an item.
            current_cart = self.cart.get(item["id"], 0)
            # Runs if the amount of an item in cart is above 20.
            if current_cart >= 20:
                # Displays a messagebox with a warning symbol, stating the text. .
                messagebox.showwarning("Amount error","You may only order 20 of an item at once \n we are sorry for this inconvenience")
                # Exits the def with a null var.
                return
        # Gets the amount of an item currently in the cart dict and adds it to a local var called current_cart.
        # 0 is in .get's parameters to ensure when an item isn't selected it can be added properly when the add buttn is pressed.
        current_cart = self.cart.get(item["id"], 0)
        # The local var new_cart is used to prevent the user from adding -1 items to the cart dict.
        # It does this by using the max def with a minimum parameter of 0, and the var being current_cart + delta.
        # Delta will be ±1, and with the minimun it cannot go below zero.
        new_cart = max(0, current_cart + delta)
        # An if statement to check the value of new_cart and act acording to the parameters.
        # If new_cart is equal to zero it runs the code with this statement.
        if new_cart == 0:
            # This statement calls the cart and removes the item which has its amount being item within the cart dict.
            self.cart.pop(item["id"], None)
        # If new_cart is equal to anything else it runs the code within this statement.
        else:
            # This statement calls the cart and increases the amount value of the item in the cart dict.
            self.cart[item["id"]] = new_cart
        # Updates the item_amount's text to the var new_cart as a string.
        self.item_amount[item["id"]].config(text=str(new_cart))
        # Calls the update_cart def to update the cart to the amount changes.
        self.update_cart()
    def days_duration(self):
        '''This def calculates the total amount of days the user has hired their items for, it will always default to 1 unless specified by the user'''
        # This try statement is used to get the delta or days_total between the pickup value and dropoff value.
        # Trys to call pickup_date and dropoff_date, strip them from their format, then find the difference.
        try: 
            pickup = datetime.datetime.strptime(self.pickup_date.get().strip(), "%d/%m/%Y").date()
            dropoff = datetime.datetime.strptime(self.dropoff_date.get().strip(), "%d/%m/%Y").date()
            days_total = (dropoff - pickup).days
            # Returns days_total which is used to calculate the daycost.
            return days_total
        # If for some reason one of the statements throws a value error returns days_total as one day.
=======
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
>>>>>>> 4e0745e (Commenting Code, Penultimate Commit)
        except ValueError:
            # Sets days_total to 1.
            days_total = 1
            # Returns days_total to whereever the def was called.
            return days_total
    
    def update_cart(self):
        '''This def displays the items in the cart when they are added'''
<<<<<<< HEAD
        # Fetches days_total by calling days_duration.
        days_total = self.days_duration()
        # Creates a local dict which contains each item in STORE_ITEMS by looping through each item ID and storing the information under the ID.
        items_in_cart = {item["id"]: item for item in STORE_ITEMS}
        # Creates a list that is used to store an items name, the amount of the item, and the total price.
        ordered_items = []
        # Sub_total is created in this def as a local var, as the += statement needs two int vars to work as needed.
        sub_total = 0.0
        # For each item in the cart runs the code within the statement below.
        for item_id, amount in self.cart.items():
            # Checks item_id in cart against the item_id in items_in_cart and if its there assigns the items information to the item var.
            item = items_in_cart[item_id]
            # Finds the line_cost by using the item var's dayprice and multiplying it by the amount in the cart and the days_total.
            line_cost = item["dayprice"] * amount * days_total
            # The line_cost is added to sub_total.
            sub_total += line_cost
            # Adds the item to the ordered_items list with its name, amount and the line_cost.
            ordered_items.append(f"{item['name']} x{amount}  ${line_cost}")
        # Calculates the tax_total int by multiplying GST by the sub_total.
        tax_total = sub_total * GST
        # Calculates the total int by adding the tax_total to the sub_total.
        total = sub_total + tax_total
        # Configs cart_text to be editable.
        self.cart_text.config(state="normal")
        # Clears cart_text.
        self.cart_text.delete("1.0", tk.END)
        # If the ordered_items list contains any items this if statement is run.
        if ordered_items:
            # Creates a header string which has a header for the item; name, amount, and, cost.
            # Then breaks to the next line, and puts 40 ─ to reinforce the item of the header var being a header.
            header = f"{'Item'}, Amount,  {'Cost'},\n" + "─" * 40 + "\n"
            # Adds the header to cart text, then adds each item in ordered_items after a linebreak.
            self.cart_text.insert(tk.END, header + "\n".join(ordered_items))
        # If the ordered_items doesn't contain anything this else statement is run.
        else:
            # Adds text to cart_text that says " No items in cart".
            self.cart_text.insert(tk.END, "No items in cart.")
        # Configx cart_text to not be editable.
        self.cart_text.config(state="disabled")


        # Changes each value to contain the corasponding value within this def.
=======
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

>>>>>>> 4e0745e (Commenting Code, Penultimate Commit)
        self.days_hired.config(text=f"{days_total} day{'s' if days_total != 1 else ''}")
        self.price_subtotal.config(text=f"${sub_total:.2f}")
        self.sales_tax.config(text=f"${tax_total:.2f}")
        self.total_price.config(text=f"${total:.2f}")
        
    def checkout(self):
        '''This def handles the checkout process when the checkout button is pressed, and the saving of the data generated by the process.'''
<<<<<<< HEAD
        # Gets the value of name_entry and assigns it to a newly created checkout_name.
        checkout_name = self.name_entry.get()
        # Creates a bool called checkout_name_check set to false.
        checkout_name_check = False
        # Creates a while loop that runs while the checkout_name_check bool is false.
        while checkout_name_check is False:
            # Removes any whitespace from the checkout_name var.
            checkout_name = checkout_name.strip()
            # Returns a true or false bool to checkout_name_check if checkout_name is not only alphabet chars.
            checkout_name_check = checkout_name.isalpha()
            # If the checkout_name_check bool is true the if statement runs.
            if checkout_name_check is True:
                # Exists the while loop and continues on.
                pass
            # If the checkout_name_check bool isn't true this else statement runs.
            else:
                # Displays a messagebox with an error sign explaining why the user's input name is not valid.
                messagebox.showerror(title="Name Error",message="Username must only contain alphabet charactors.\n Please reenter your name")
                # Returns nothing, exiting the def.
                return
        # Creates a bool called checkout_date_check_p set to false, the p is for pickup.
        checkout_date_check_p = False
        # Creates a bool called checkout_date_check_d set to false, the d is for dropoff.
        checkout_date_check_d = False
        # Creates a while loop that runs while the checkout_date_check_p bool and checkout_date_check_d bool is false.
        while checkout_date_check_d is False and checkout_date_check_p is False:
            # Trys to get the pickup/drop off dates and remove its formating, according to datetime.
            # For some reason I couldn't get datetime to work without calling it twice(also happens in the days_duration def).
            try:
                # Calls the pickup_date var and strips the formating with the strptime def.
                pickup = datetime.datetime.strptime(self.pickup_date.get().strip(), "%d/%m/%Y").date()
                # Calls the dropoff_date var and strips the formating with the strptime def.
                dropoff = datetime.datetime.strptime(self.dropoff_date.get().strip(), "%d/%m/%Y").date()
                # Sets the checkout_date_check_p bool to true.
                checkout_date_check_p = True
                # Sets the checkout_date_check_d bool to true.
                checkout_date_check_d = True
            # Runs if there is an error with the formating, like unexpected charactors in the date input runs the code below, displays why, and resets the dates.
            except ValueError:
                # Displays a messagebox with an error sign explaining that user's date format is not valid and that the dates will be reset.
                messagebox.showwarning(title="Date Error: Incorrect Format",message="The Format of the Hire dates is incorrect \n Dates will be reset, please re-enter your Hire dates")
                # Resets the dropoff date to the day after the current day.
                self.dropoff_date = tk.StringVar(value=(datetime.date.today() + datetime.timedelta(days=1)).strftime("%d/%m/%Y"))
                # Resets the pickup date to the current day.
                self.pickup_date = tk.StringVar(value=datetime.date.today().strftime("%d/%m/%Y"))
                # Returns nothing, exiting the def.
                return
            # Compairs the pickup and dropoff vars if checkout_date_check_p is True and checkout_date_check_d is True.
            if checkout_date_check_p is True and checkout_date_check_d is True:
                # Runs if the pickup date is greater than the dropoff date, which would result in negative price values.
                if pickup > dropoff:
                    messagebox.showinfo(title="Date Time Error",message="Pickup date is greater than dropoff date, \n please re-enter your Hire dates.")
                    # Returns nothing, exiting the def
                    return
                # Runs if the pickup date is equal to the dropoff date, which would result in price values of zero.
                elif pickup == dropoff:
                    messagebox.showinfo(title="Date Time Error",message="Pickup date is the same as dropoff date, \n please re-enter your Hire dates.")
                    # Returns nothing, exiting the def
                    return
                # Exits the while loop if pickup is lesser than the dropoff value(Expected behavour).
                elif pickup < dropoff:
                    pass
                # Runs if somthing unexplained happens(I have no idea how to trigger this but its always good to be carful).
                else:
                    messagebox.showerror(title="Unknown error",message="Unknown error within Dates, re-enter your start and end hire dates.")
                    # Returns nothing, exiting the def
                    return
            # Another check if the code somehow encounters an unexplainable error.
            else:
                messagebox.showerror(title="Unknown error",message="Unknown error within Dates, re-enter your start and end hire dates.")
                # Returns nothing, exiting the def
                return
                
        # If the cart dict is empty this if statement runs.
        if not self.cart:
            # Asks the user to input items to the cart.
            messagebox.showwarning("Cart is empty", "Please add items to cart to proceed.")
            # Returns nothing, exiting the def
            return
        # Gets days_total from the days_duration def.
        days_total = self.days_duration()
        # This section up to the end of the for statement is esstentially the same as the code from lines 333 to 347.
        checkout_items = {item["id"]: item for item in STORE_ITEMS}
=======
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
>>>>>>> 4e0745e (Commenting Code, Penultimate Commit)
        ordered_items = []
        sub_total = 0.0
        for item_id, amount in self.cart.items():
            item = checkout_items[item_id]
            line_cost = item["dayprice"] * amount * days_total
            sub_total += line_cost
<<<<<<< HEAD
            # This one part is diffent, as it includes the items ID which is used to be more specific when writing to the json file.
            ordered_items.append({"Id": item_id,"Name": item["name"],"Amount": amount,"Cost": line_cost})
        # Calculates the tax_total by multiplying the sub_total by GST.
        tax_total = sub_total * GST
        # Calculates the total by adding the tax_total to the subtotal.
        total = sub_total + tax_total 
        # Creates receipt_id as a string of charactors generated by the uuid library.
        # This generated string is limited to 8 charactors of all uppercase where possible.
        receipt_id = str(uuid.uuid4())[:8].upper()
        # Creates an int with the value of zero, to act as the counter to prevent multiple returns.
        times_returned = int(0)
        # Refer to why Has_Returned is commented out to the search_dates def.
        # Uses all the previous values within this def or outside this def(the pickup/dropoff dates) and stores it in a dict record.
=======
            ordered_items.append({"Id": item_id,"Name": item["name"],"Amount": amount,"Cost": line_cost})

        tax_total = sub_total * GST
        total = sub_total + tax_total 
        receipt_id = str(uuid.uuid4())[:8].upper()
        times_returned = int(0)
        #Refer to why Has_Returned is commented out to the search_dates def
>>>>>>> 4e0745e (Commenting Code, Penultimate Commit)
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
<<<<<<< HEAD
            # "Has_Returned": False.
        }
        # Saves all the information in record to the data dict under the user_data and receipt_id catagories.
        # Receipt_id is saved twice to allow for redundency and to allow multiple users if they have similar data.
        # Without this there could also only be one record stored at a time.
        self.data["user_data"][receipt_id] = record
        # Writes all the formated data within the data dict to the boltbyte_data.json file.
        save_data(self.data)
        # For each item in the cart sets the item id to 0.
        for item_id in self.cart:
            self.item_amount[item_id].config(text="0")
        # Clears the cart.
        self.cart.clear()
        # Runs update_cart to ensure the cart_text is cleared.
        self.update_cart()
        # Clears the name_entry field.
        self.name_entry.set("")
        # Runs record_refresh which is used in the admin/staff access notebook tab.
        self.record_refresh()
        # Runs the checkout_bill def which creates a bill.
        self.checkout_bill(record)
        # Calls the pickup_date var and strips the formating with the strptime def.
        pickup = datetime.datetime.strptime(self.pickup_date.get().strip(), "%d/%m/%Y").date()
        # Calls the dropoff_date var and strips the formating with the strptime def.
        dropoff = datetime.datetime.strptime(self.dropoff_date.get().strip(), "%d/%m/%Y").date()
        # Returns the record dict allowing it to be used in the checkout_bill.
=======
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
        
>>>>>>> 4e0745e (Commenting Code, Penultimate Commit)
        return record
        
    def checkout_bill(self, record):
        '''5'''
<<<<<<< HEAD
        # This creates a window parented to the main root window for the bill.
        bill_window = tk.Toplevel(self.root)
        # Sets the title of the bill_window.
        bill_window.title("Rental Receipt")
        # Sizes the receipt window to 400 pixels wide by 500 pixels tall.
        bill_window.geometry("400x500")
        
        # Creates a title label with the store name at the top of the receipt.
        bill_title = tk.Label(bill_window, text="Bolt & Byte Tech Hire", font=("Helvetica", 16, "bold"))
        # Packs the title and adds a 10 pixel padding on the y-axis.
        bill_title.pack(pady=10)
        
        # Creates a label to display the receipt_id passed in from the record parameter.
        bill_receipt_id =tk.Label(bill_window, text=f"Receipt ID: {record['receipt_id']}")
        # Packs the receipt ID label into the window.
        bill_receipt_id.pack()
        
        # Creates a label displaying the date the record was created, showing the first 10 characters for just the date.
        bill_timestamp = tk.Label(bill_window, text=f"Date: {record['timestamp'][:10]}")
        # Packs the timestamp label into the window.
        bill_timestamp.pack()
        
        # Creates a visual line break using dashes to separate the header from customer details.
        bill_linebreak = tk.Label(bill_window, text="------------------------------")
        # Packs the line break with a 5 pixel vertical padding.
        bill_linebreak.pack(pady=5)
        
        # Creates a label showing the customer's name from the record.
        bill_customer_name = tk.Label(bill_window, text=f"Customer: {record['customer_name']}")
        # Packs the customer name label into the window.
        bill_customer_name.pack()
        
        # Creates a label showing the pickup date from the record.
        bill_pickup_date = tk.Label(bill_window, text=f"Pickup Date: {record['pickup_date']}")
        # Packs the pickup date label into the window.
        bill_pickup_date.pack()
        
        # Creates a label showing the dropoff date from the record.
        bill_dropoff_date = tk.Label(bill_window, text=f"Dropoff Date: {record['dropoff_date']}")
        # Packs the dropoff date label into the window.
        bill_dropoff_date.pack()
        
        # Creates a bold header label for the list of rented items.
        bill_items_header = tk.Label(bill_window, text="Items Rented:", font=("Helvetica", 12, "bold"))
        # Packs the items header with 10 pixel vertical padding.
        bill_items_header.pack(pady=10)

        # Loops through each item stored within the items list of the record.
        for items in record["items"]:
            # Creates a label for each item showing its name, amount, and total cost rouned to 2 significant figures.
            bill_items = tk.Label(bill_window, text=f"{items['Name']} x{items['Amount']} - ${items['Cost']:.2f}")
            # Packs each item label anchored to the center with 20 pixels of padding on the x-axis.
            bill_items.pack(anchor="center", padx=20)

        # Creates a label displaying the subtotal cost rounded to 2 significant.
        bill_subtotal = tk.Label(bill_window, text=f"Subtotal: ${record['subtotal']:.2f}")
        # Packs the subtotal label with a padding of 5 pixels on the y axis.
        bill_subtotal.pack(pady=5)
        
        # Creates a label displaying the tax amount,rounded to 2 significant figures.
        bill_tax = tk.Label(bill_window, text=f"Tax ({int(GST*100)}%): ${record['tax']:.2f}")
        # Packs the tax label with a padding of 5 pixels on the y axis.
        bill_tax.pack(pady=5)
        
        # Creates a bold label displaying the final total price.
        bill_total = tk.Label(bill_window, text=f"Total: ${record['total']:.2f}", font=("Helvetica", 12, "bold"))
        # Packs the bill_total label with a padding of 10 pixels on the y axis.
        bill_total.pack(pady=10)
        
        # Creates a  button that runs the window's destroy command to close the receipt when clicked.
        bill_close = tk.Button(bill_window, text="Close", command=bill_window.destroy)
        # Adjusts the bill_close button with a padding of 10 pixels on the y axis.
=======
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
>>>>>>> 4e0745e (Commenting Code, Penultimate Commit)
        bill_close.pack(pady=10)
        
    def returns_ui(self):
        '''6'''
<<<<<<< HEAD
        # Creates a LabelFrame for the receipt ID search section parented to the returns tab.
        receipt_frame = ttk.LabelFrame(self.returns, text="Search Rental Receipt")
        # Packs the frame anchoring it to the north, expanding it to fill the x-axis, with padding.
        receipt_frame.pack(anchor="n" ,fill="x",padx=6, pady=4)
        
        # Creates an inner frame to hold the receipt ID entry box and search button.
        receipt_id_frame = ttk.Frame(receipt_frame)
        # Makes the inner frame fill the x-axis.
        receipt_id_frame.pack(fill="x")
        
        # Creates an entry box for the user to type in a receipt ID.
        self.receipt_id_entry = ttk.Entry(receipt_id_frame, font=("Helvetica", 10), width=36)
        # Packs the entry box to the left, setting it to expand and fill the x-axis.
        self.receipt_id_entry.pack(side="left", padx=6, pady=2, expand=True, fill="x")
        
        # Creates a search button that calls the search_receipt def when pressed, packed to the right.
        ttk.Button(receipt_id_frame, text="Search", command=self.search_receipt).pack(side="right", padx=6, pady=2)
        
        # Creates a larger LabelFrame for users who forgot their receipt ID.
        receipt_forget_frame = ttk.LabelFrame(self.returns, text="Forgot your Receipt? Use your Name or Pickup/Dropoff Date")
        # Packs the frame to expand and fill the x-axis in the center with padding.
        receipt_forget_frame.pack(expand=True, anchor="center",fill="x",padx=6, pady=4)
        
        # Creates a sub-LabelFrame specifically for searching by customer name.
        receipt_name = ttk.LabelFrame(receipt_forget_frame, text="Remeber the Name you used? Use this Box!",)
        # Packs the name LabelFrame to expand and fill the x-axis, anchoring north.
        receipt_name.pack(expand=True, anchor="n",fill="x",padx=6, pady=4)
        
        # Creates an entry box for the user to type their name.
        self.receipt_name_entry = ttk.Entry(receipt_name, font=("Helvetica", 10), width=36)
        # Packs the entry box to the left, setting it to expand and fill the x-axis.
        self.receipt_name_entry.pack(expand=True, side="left", padx=5, pady=2, fill="x")
        
        # Creates a search button that calls the search_name def when pressed, packed to the right.
        ttk.Button(receipt_name, text="Search", command=self.search_name,).pack(side="right", padx=6, pady=2)
        
        # Creates a sub-LabelFrame specifically for searching by pickup and dropoff dates.
        receipts_dates = ttk.LabelFrame(receipt_forget_frame, text="Remember your Pickup/Dropoff Date? Use this Box!",)
        # Packs the dates LabelFrame to expand and fill the x-axis, anchoring north.
        receipts_dates.pack(expand=True, anchor="n",fill="x",padx=6, pady=4)

        # Creates a LabelFrame to label the pickup date entry.
        receipt_dates_pickup_label = ttk.Labelframe(receipts_dates, text="Date of Pickup")
        # Packs the pickup label frame to the left to share the line, filling the x-axis.
        receipt_dates_pickup_label.pack(side="left", padx=5, pady=20, expand=True, fill="x")
        # Creates the entry box for the pickup date search.
        self.receipts_dates_pickup = ttk.Entry(receipt_dates_pickup_label, font=("Helvetica", 10), width=36)
        # Packs the pickup entry box into its parent label frame, allowing expansion.
        self.receipts_dates_pickup.pack(side="left", padx=5, pady=20, expand=True, fill="x")
        
        # Creates a LabelFrame to label the dropoff date entry.
        receipt_dates_dropoff_label = ttk.Labelframe(receipts_dates, text="Date of Dropoff")
        # Packs the dropoff label frame to the left, continuing the horizontal layout.
        receipt_dates_dropoff_label.pack(side="left", padx=5, pady=20, expand=True, fill="x")
        # Creates the entry box for the dropoff date search.
        self.receipts_dates_dropoff = ttk.Entry(receipt_dates_dropoff_label, font=("Helvetica", 10), width=36)
        # Packs the dropoff entry box into its parent label frame, allowing expansion.
        self.receipts_dates_dropoff.pack(side="left", padx=5, pady=20, expand=True, fill="x")
        
        # Creates a search button that calls the search_dates def when pressed, packed to the left at the end of the row.
        ttk.Button(receipts_dates, text="Search", command=self.search_dates).pack(side="left", padx=6, pady=2)
        # Returns nothing, essentially exiting the def.
=======
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
>>>>>>> 4e0745e (Commenting Code, Penultimate Commit)
        return
    
    def search_receipt(self):
        '''7'''
<<<<<<< HEAD
        # Commented out any section that included "Has_Returned", I cannot understand why it will not play nicely with.
        # Bool values in reading from json files and am not willing to use this method to counteract dupelicate returns.
        
        # Gets the inputted receipt ID and strips leading or trailing whitespace.
        receipt_id = self.receipt_id_entry.get().strip()
        # Checks if the receipt ID exists in the saved data and if its 'Returned' status is exactly 0 (not returned).
        if receipt_id in self.data["user_data"] and self.data["user_data"][receipt_id]["Returned"] == 0:
        # And self.data["user_data"][receipt_id]["Has_Returned"] == "false":.
            # Assigns the specific matched record to a local variable.
            record = self.data["user_data"][receipt_id]
            # Calls the checkout_bill def to visually display the receipt.
            self.checkout_bill(record)
            # Self.data["user_data"]["Has_Returned"] = True.
            # Sets the 'Returned' value for this receipt in the data to 1, updating its status to returned.
            self.data["user_data"][receipt_id]["Returned"] = 1
            # Saves the updated data back to the JSON file.
            save_data(self.data)
        # Checks if the input receipt ID is completely missing from the user_data dict.
        elif receipt_id not in self.data["user_data"]:
            # Shows an error box stating the receipt ID cannot be found.
            messagebox.showerror("Not Found", "No receipt found with that Receipt ID.")
        # Elif self.data["user_data"][receipt_id]["Has_Returned"] == "true":.
        #    messagebox.showerror("This Receipt has already been returned").
        # Runs if the receipt ID is found but the 'Returned' value is greater than 0.
        elif self.data["user_data"][receipt_id]["Returned"] > 0:
            # Shows an error indicating the user should contact staff as it's already marked as returned.
            messagebox.showerror(title="This receipt has already been returned",message="Contact your local Bolt & Byte Tech staff for support")
        # A fallback else statement to catch any bizarre or unexpected errors.
=======
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
>>>>>>> 4e0745e (Commenting Code, Penultimate Commit)
        else:
            # Throws a general unexpected error popup.
            messagebox.showerror(title="Unknown or Unexpected Error", message="Contact your administrator for support")
        
    def search_name(self):
        '''7'''
        # Gets the inputted search name and strips trailing or leading whitespace.
        name_search = self.receipt_name_entry.get().strip()
        # Loops through every record ID and record dictionary inside user_data.
        for record_id, record in self.data["user_data"].items():
            # Checks if the customer's name in the current record exactly matches the search input.
            if record["customer_name"] == name_search:
                # Uses .get() to check the 'Returned' status, defaulting to 0 if missing, and validates it is 0.
                if record.get("Returned",0) == 0:
                    # Calls checkout_bill to display the receipt.
                    self.checkout_bill(record)
                    # Self.data["user_data"]["Has_Returned"] = True.
                    # Changes the 'Returned' value within the record to 1.
                    record["Returned"] = 1
                    # Saves the updated user_data back to the JSON file.
                    save_data(self.data)
                    # Returns to cleanly exit the function.
                    return
                # Executes if the name matches but the item is already returned.
                else:
                    # Shows an error indicating the return has already happened.
                    messagebox.showerror(title="This receipt has already been returned",message="Contact your local Bolt & Byte Tech staff for support")
                    # Returns to cleanly exit the function.
                    return

        # If the loop fully completes without finding a name match, it displays a Not Found error.
        messagebox.showerror(title="Not Found",message="No receipt found with that customer name.")
        
    def search_dates(self):
        '''9'''
        # Assigns the user's input from the pickup date entry to a variable.
        date_search_pickup = self.receipts_dates_pickup.get()
        # Assigns the user's input from the dropoff date entry to a variable.
        date_search_dropoff = self.receipts_dates_dropoff.get()
        # Loops through all items in the user_data JSON dict.
        for record_id, record in self.data["user_data"].items():
            # Checks if both the pickup date and the dropoff date on the record match the inputted search criteria.
            if record["pickup_date"] == date_search_pickup and record["dropoff_date"] == date_search_dropoff:
                # Checks if the returned status is equal to 0 (meaning it has not been returned).
                if record.get("Returned",0) == 0:
                    # Calls checkout_bill to open and display the receipt window.
                    self.checkout_bill(record)
                    # Self.data["user_data"]["Has_Returned"] = True.
                    # Updates the return status to 1.
                    record["Returned"] = 1
                    # Saves the newly updated dictionary to the JSON file.
                    save_data(self.data)
                    # Returns to conclude the function safely.
                    return
                # Runs if the dates match but the 'Returned' value is higher than 0.
                else:
                    # Shows an error stating the receipt is already returned.
                    messagebox.showerror(title="This receipt has already been returned",message="Contact your local Bolt & Byte Tech staff for support")
                    # Returns to conclude the function.
                    return
            # Runs if the current loop iteration does not match the search dates.
            else:
                # Shows a Not Found error indicating the dates didn't match a record.
                messagebox.showerror(title="Not Found", message="No product hire with those dates")
                # Returns to conclude the function.
                return
        # Catches any unforeseen issues after the loop.
        messagebox.showerror(title="Unknown or Unexpected Error", message="Contact your administrator for support")
        
    def admin_ui(self):
        '''10'''
        # Password code Commented Out.
        # Python doesn't respond well to tbis kind of password frame. not this, its the z leveling that it doesn't respond well to.
        # If I come back to this It'd be better to have a login page as the base frame that everything else parrents off.
        # And for an admin login instead of a user login give access to this page.
        # I do not have enough time to implement this.
        # Self.Staff_login_window = tk.Frame(self.Admin).
        # Self.Staff_login_window.place(relx=0, rely=0, relheight=1, relwidth=1).
        #
        # Self.Login_label = tk.Label(self.Staff_login_window,text="Input Password Here \n Authorised Users Only",font=("Helvetica", 12, "bold"),bg="gray",fg="black").
        # Self.Login_label.place(relx=0.5,rely=0.35,anchor="center").
        #
        # Self.Login_password_check = tk.StringVar().
        #
        # Self.Login_entry = tk.Entry(self.Staff_login_window, textvariable=self.Login_password_check, bg="gray",fg="black").
        # Self.Login_entry.place(relx=0.5,rely=0.45,anchor="center").
        #
        # Self.Login_button = tk.Button(self.Staff_login_window, text="Confirm Password", command=self.Login_process).
        # Self.Login_button.place(relx=0.5,rely=0.50,anchor="center").

        # Creates an outer frame parented to the admin notebook tab to hold all UI elements.
        admin_ui_outer = ttk.Frame(self.admin)
        # Packs the outer frame to expand and fill the available area with 10 pixel padding.
        admin_ui_outer.pack(expand=True, fill="both", padx=10, pady=10)
        
        # Creates a frame for the left side of the screen with a specific fixed width of 350.
        admin_ui_left = ttk.Frame(admin_ui_outer, width=350,)
        # Packs the left frame strictly to the left, allowing it to fill the y-axis.
        admin_ui_left.pack(side="left", fill="y")
        # Disables pack propagation so the frame stays strictly at its 350 width and doesn't auto-resize to its children.
        admin_ui_left.pack_propagate(False)
        
        # Creates a bold title label reading "Rental Records" and packs it with y-axis padding.
        ttk.Label(admin_ui_left, text="Rental Records", font=("Helvetica", 15, "bold")).pack(pady=6)
        
        # Creates a frame exclusively to hold the listbox widget that displays all records.
        admin_record_listbox = ttk.Frame(admin_ui_left)
        # Packs the listbox frame to expand and fill with 6 pixels of padding.
        admin_record_listbox.pack(expand=True, fill="both", padx=6, pady=6)        
        # Creates a vertical scrollbar widget assigned to the listbox frame.
        admin_scrollbar = ttk.Scrollbar(admin_record_listbox)
        # Packs the scrollbar to the far right side and fills the y-axis.
        admin_scrollbar.pack(side="right", fill="y")
        
        # Creates a Listbox widget to actually hold the records text, styled with specific background/foreground colors.
        self.admin_record_list = tk.Listbox(admin_record_listbox, font=("Helvetica", 12),bg="#DCDAD5",fg="black", yscrollcommand=admin_scrollbar.set)
        # Packs the Listbox to the left side and makes it fill out and expand to the rest of its frame.
        self.admin_record_list.pack(side="left", expand=True, fill="both")        
        # Configures the scrollbar to actually control the y-axis view of the admin_record_list.
        admin_scrollbar.configure(command=self.admin_record_list.yview)
        # Binds a left-click selection event in the listbox to trigger the record_show def.
        self.admin_record_list.bind("<<ListboxSelect>>", self.record_show)
        
        # Creates a frame for the right side of the admin tab to show full record details.
        admin_right = ttk.Frame(admin_ui_outer)
        # Packs the right frame to the right side, forcing it to expand and fill with left-side padding of 12 pixels.
        admin_right.pack(side="right", fill="both", expand=True, padx=(12,0))        
        # Creates a standard label title for the selected receipt's details.
        self.admin_record_title = ttk.Label(admin_right, text="Receipt details", font=("Helvetica", 10))
        # Packs the title anchoring it to the west (left).
        self.admin_record_title.pack(anchor="w")
        
        # Creates a blank label with a solid border that will dynamically hold a text string showing the selected record's data.
        self.admin_record_details = ttk.Label(admin_right,text="",font=("Helvetica", 10),relief="solid")
        # Packs the details label to expand and fill with 6 pixels of padding.
        self.admin_record_details.pack(anchor="w", expand=True, fill="both", padx=6, pady=6)
        
        # Creates a label titling the "Items Hired" section.
        admin_item_hired = ttk.Label(admin_right, text="Items Hired", font=("Helvetica", 12))
        # Packs the item hired title with 10 pixel vertical padding.
        admin_item_hired.pack(pady=10)
        
        # Creates a solid bordered frame to hold a listbox of the individual items a user hired.
        admin_item_hired = ttk.Frame(admin_right, relief="solid")
        # Packs the items frame to expand and fill the available area.
        admin_item_hired.pack(expand=True, fill="both", padx=6, pady=6)
        
        # Creates a vertical scrollbar specifically for the items listbox.
        admin_item_scrollbar = ttk.Scrollbar(admin_item_hired)
        # Packs the items scrollbar to the right side.
        admin_item_scrollbar.pack(side="right", fill="y")
        
        # Creates the Listbox that will show each hired item's name, quantity, and cost.
        self.admin_item_list = tk.Listbox(admin_item_hired,font=("Helvetica", 10) ,bg="#DCDAD5" ,fg="black" , yscrollcommand=admin_item_scrollbar.set)
        # Packs the item listbox to the left and makes it expand and fill.
        self.admin_item_list.pack(side="left", expand=True, fill="both")
        
        # Configures the items scrollbar to control the y-axis view of the item listbox.
        admin_item_scrollbar.configure(command=self.admin_item_list.yview)
        
        # Creates an initially empty bold label intended to hold totals (if needed).
        admin_totals = ttk.Label(admin_right, text="", font=("Helvetica", 12, "bold"),)
        # Packs the totals label anchoring it west with vertical padding.
        admin_totals.pack(anchor="w", pady=8)
        
        # Creates a button that triggers the copy_record def to copy the selected record's raw JSON text.
        ttk.Button(admin_right, text="Copy record to Clipboard", command=self.copy_record).pack(pady=4)
        # Creates a button that triggers the delete_record def to completely delete a selected record.
        ttk.Button(admin_right, text="Delete Record", command=self.delete_record).pack(pady=4)
        
        # Self.Staff_login_window.tkraise().
        # Part of the commented out Login page.

        # Initializes an empty string variable designed to keep track of the currently selected record's ID.
        self.selected_receipt_id = ""

        # Calls record_refresh when the admin tab loads to populate the listbox with the initial data.
        self.record_refresh()
    
    def record_refresh(self):
        '''11'''
        # Clears all text lines in the admin_record_list listbox from index 0 to the very end.
        self.admin_record_list.delete(0, tk.END)
        # Resets the selected receipt ID variable as an empty list to track indices.
        self.selected_receipt_id = []
        # Loops through all keys and values in the user_data JSON dictionary.
        for receipt_id, record in self.data["user_data"].items():
            # Inserts a formatted text string of the receipt ID, name, and pickup date to the end of the listbox.
            self.admin_record_list.insert(tk.END, f" #{receipt_id} {record['customer_name']} \n {record['pickup_date']}")
            # Appends the receipt ID to the tracker list, aligning its index perfectly with the listbox index.
            self.selected_receipt_id.append(receipt_id)
            
    def delete_record(self):
        '''12'''
        if self.selected_receipt_id:
            # Gets the exact ID of the record currently selected by grabbing the listbox's active index and pulling from the tracker list.
            delete_id = self.selected_receipt_id[self.admin_record_list.curselection()[0]]
            # Generates a warning popup requiring the user to explicitly say yes or no to deletion.
            delete_confirm = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this record? This action cannot be undone.")
            # Checks if the user clicked the 'yes' button.
            if delete_confirm:
                # Removes the specific record from the data dictionary using its ID.
                self.data["user_data"].pop(delete_id, None)
                # Saves the updated dictionary (now missing the record) back to the JSON file.
                save_data(self.data)
                # Calls the record_refresh def to update the listbox and visually remove the record.
                self.record_refresh()
            else:
                # Shows a warning prompting the user to pick a record.
                messagebox.showwarning("No Selection", "Please select a record to delete.")
        else:
            # Shows a warning saying there are no records.
            messagebox.showwarning("No Records", "There are no records to delete.")
            
    def copy_record(self):
        '''13'''
        # Checks to see if the selected receipt ID tracker list is currently populated.
        if self.selected_receipt_id:
            # Retrieves the current selection index from the listbox.
            selected_record = self.admin_record_list.curselection()
            # Verifies that the user actually has a valid line selected.
            if selected_record:
                # Gets the exact receipt ID from the tracker list matching the listbox index.
                receipt_id = self.selected_receipt_id[selected_record[0]]
                # Pulls all the data of that specific record into a local variable.
                record = self.data["user_data"][receipt_id]
                # Uses json.dumps to format the raw dictionary into a nice indented JSON text string.
                record_text = json.dumps(record, indent=4)
                # Clears the clipboard.
                self.root.clipboard_clear()
                # Saves the JSON record to the clipboard.
                self.root.clipboard_append(record_text)
                # Shows an messagebox telling the user that the data was copied.
                messagebox.showinfo("Copied", "Record copied to clipboard.")
            # Executes if the user hit the copy button without selecting a record first.
            else:
                # Shows a warning prompting the user to pick a record.
                messagebox.showwarning("No Selection", "Please select a record to copy.")
        # Executes if there are simply no records loaded to copy at all.
        else:
            # Shows a warning saying there are no records.
            messagebox.showwarning("No Records", "There are no records to copy.")
            
    def record_show(self,event):
        '''13'''
<<<<<<< HEAD
        # Retrieves the index of the line that was clicked/selected in the listbox.
        selected_record = self.admin_record_list.curselection()
        # Verifies a selection has actually been made.
        if selected_record:
            # Retrieves the matching receipt ID from the tracker list.
            receipt_id = self.selected_receipt_id[selected_record[0]]
            # Pulls the dictionary data attached to that specific receipt ID.
            record = self.data["user_data"][receipt_id]
            # Creates a multi-line formatted string detailing customer info, dates, costs, and returned status.
            details_text = f"Customer: {record['customer_name']}\nPickup Date: {record['pickup_date']}\nDropoff Date: {record['dropoff_date']}\nDays Hired: {record['days_hired']}\nSubtotal: ${record['subtotal']:.2f}\nTax: ${record['tax']:.2f}\nTotal: ${record['total']:.2f}\nReturned: {'Yes' if record.get('Returned', 1) else 'No'}"
            # Updates the blank record details label to now display the multi-line string.
            self.admin_record_details.config(text=details_text)
            
            # Clears the items listbox to prepare for new data.
            self.admin_item_list.delete(0, tk.END)
            # Loops through each item saved within this specific record's items list.
            for item in record["items"]:
                # Inserts the item's name, quantity, and cost into the items listbox at the bottom.
                self.admin_item_list.insert(tk.END, f"{item['Name']} x{item['Amount']} - ${item['Cost']:.2f}")
    # This def was the underlying logic for the password login, the place_forget() does not update the elements under it thus leading to a page refresh needed, this seemed unideal and was scrapped.    .
    # Def Login_process(self):.
    #    if self.Login_password_check.get() == adminpassword:.
    #        self.Staff_login_window.place_forget().
    #        self.Login_label.place_forget().
    #        self.Login_entry.place_forget().
    #        self.Login_button.place_forget().
    #        self.Admin_UI_outer.update_idletasks().
    #        self.Record_refresh().
    #        return.
    #    else:.
    #        messagebox.showerror(title="Incorrect Password",message="The Password is Incorrect").
=======
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
>>>>>>> 4e0745e (Commenting Code, Penultimate Commit)

if __name__ == "__main__":
    root = tk.Tk()
    app = BoltByteProject(root)
    root.mainloop()
