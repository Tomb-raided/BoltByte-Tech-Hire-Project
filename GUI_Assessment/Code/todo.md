

PRIORITY 1 - Fix Existing Bugs:

    (x)Initialize self.data = load_data() in __init__()
    ()Remove or implement self.refresh_admin() call in checkout()
    (x)Fix self.name_entry.set() call (should be self.name_entry.delete(0, tk.END) since it's a StringVar on Entry widget)
    ()Generate receipt ID display after successful checkout (show to customer)
PRIORITY 2 - Returns UI (Your Task 1):

    ()Add search fields: Receipt ID (primary), Customer Name, Phone/Email (fallback)
    ()Implement search function to retrieve rental records from self.data["rentals"]
    ()Display matched rental order details in readonly text widget
    ()Add item quantity selectors for partial returns
    ()Calculate refund amount (prorated based on return date vs. dropoff date)
    ()Validate GST calculation on refunds
    ()Add "Confirm Return" button to update self.data["returns"], delete from rentals
    ()Generate return receipt with refund amount
PRIORITY 3 - Admin UI (Your Task 2):

    ()Password Gate: Add login dialog on tab switch to admin tab
    ()Store hashed password (or plain for now: "admin123")
    ()Block access if wrong password
    ()Item Management Section:
    ()Table/list showing all items with: ID, Name, Price, Colour
    ()"Add Item" button to form to create new item (ID, Name, Price, Colour picker)
    ()"Edit Item" button to modify existing item details
    ()"Delete Item" button to remove item from storeitems (warn about active rentals)
    ()User Records Section:
    ()Table showing all rentals: Order ID, Customer, Items, Total, Status
    ()Search/filter by customer name or date range
    ()View individual order details
    ()Mark order as "Returned", "Pending", "Overdue"
    ()Data Persistence:
    ()Save item changes to JSON file (extend boltbyte_data.json schema)
    ()Reload main rentals tab after item list changes
PRIORITY 4 - Polish:

    ()Prevent duplicate item IDs when adding new items
    ()Add data validation (dates, prices, names)
    ()Error handling for file I/O failures
    ()Confirm dialogs before deleting items/records
    ()Dark theme consistency across all tabs