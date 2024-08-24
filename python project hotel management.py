import random
import datetime
import tkinter as tk
from tkinter import messagebox

# Global list declaration
name = []
phoneno = []
add = []
rc = []
p = []
checkin = []
price = []
checkout = []
room = []
custid = []
day = []

# Global variable declaration
i = 0

class HotelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Around The Village")
        self.root.configure(bg='#282c34')
        self.home()

    def home(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="WELCOME TO AROUND THE VILLAGE", font=("Helvetica", 20, "bold"), pady=20, bg='#282c34', fg='#61dafb').pack()
        self.create_button("Room Information", self.rooms_info)
        self.create_button("Booking", self.booking)
        self.create_button("Menu Card", self.rest)
        self.create_button("Payment", self.pay)
        self.create_button("Record", self.record)
        self.create_button("Exit", self.root.quit)

    def create_button(self, text, command):
        tk.Button(self.root, text=text, command=command, width=20, font=("Helvetica", 14), bg='#61dafb', fg='#282c34', activebackground='#282c34', activeforeground='#61dafb').pack(pady=5)

    def date(self, c):
        try:
            datetime.datetime(c[2], c[1], c[0])
            return True
        except ValueError:
            return False

    def booking(self):
        global i
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="BOOKING ROOMS", font=("Helvetica", 20, "bold"), pady=20, bg='#282c34', fg='#61dafb').pack()
        
        name_var = tk.StringVar()
        phoneno_var = tk.StringVar()
        address_var = tk.StringVar()
        checkin_var = tk.StringVar()
        checkout_var = tk.StringVar()
        room_type_var = tk.IntVar()
        p_var = tk.DoubleVar(value=0.0)

        def submit_booking():
            global i
            n = name_var.get()
            p1 = phoneno_var.get()
            a = address_var.get()
            cii = checkin_var.get()
            coo = checkout_var.get()
            rest_bill = p_var.get()

            if not n or not p1 or not a:
                messagebox.showerror("Error", "Name, phone number, and address cannot be empty.")
                return

            if len(p1) != 10 or not p1.isdigit():
                messagebox.showerror("Error", "Invalid phone number.")
                return

            try:
                ci = list(map(int, cii.split('/')))
                co = list(map(int, coo.split('/')))
            except ValueError:
                messagebox.showerror("Error", "Invalid date format.")
                return

            if not self.date(ci) or not self.date(co):
                messagebox.showerror("Error", "Invalid date.")
                return

            d1 = datetime.datetime(ci[2], ci[1], ci[0])
            d2 = datetime.datetime(co[2], co[1], co[0])
            d = (d2 - d1).days
            if d <= 0:
                messagebox.showerror("Error", "Check-out date must be after check-in date.")
                return

            name.append(n)
            phoneno.append(p1)
            add.append(a)
            checkin.append(cii)
            checkout.append(coo)
            day.append(d)
            p.append(rest_bill)

            room_type = room_type_var.get()
            if room_type == 1:
                room.append('Standard Non-ac')
                price.append(2000)
            elif room_type == 2:
                room.append('Standard ac')
                price.append(3500)
            elif room_type == 3:
                room.append('3-Bed Non-ac')
                price.append(3000)
            elif room_type == 4:
                room.append('3-Bed ac')
                price.append(4500)
            else:
                messagebox.showerror("Error", "Invalid room type.")
                return

            rn = random.randrange(60, 360)
            cid = random.randrange(40, 100)
            rc.append(rn)
            custid.append(cid)

            messagebox.showinfo("Success", f"Room booked successfully!\nRoom no: {rn}\nCustomer ID: {cid}")

            i += 1
            self.home()

        self.create_label("Name of Customer:")
        tk.Entry(self.root, textvariable=name_var, font=("Helvetica", 14)).pack()
        self.create_label("Phone No:")
        tk.Entry(self.root, textvariable=phoneno_var, font=("Helvetica", 14)).pack()
        self.create_label("Address:")
        tk.Entry(self.root, textvariable=address_var, font=("Helvetica", 14)).pack()
        self.create_label("Check-In (DD/MM/YYYY):")
        tk.Entry(self.root, textvariable=checkin_var, font=("Helvetica", 14)).pack()
        self.create_label("Check-Out (DD/MM/YYYY):")
        tk.Entry(self.root, textvariable=checkout_var, font=("Helvetica", 14)).pack()
        self.create_label("Restaurant Bill:")
        tk.Entry(self.root, textvariable=p_var, font=("Helvetica", 14)).pack()

        self.create_label("Select Room Type:")
        tk.Radiobutton(self.root, text="Standard Non-ac", variable=room_type_var, value=1, font=("Helvetica", 14), bg='#282c34', fg='#61dafb', selectcolor='#282c34').pack()
        tk.Radiobutton(self.root, text="Standard ac", variable=room_type_var, value=2, font=("Helvetica", 14), bg='#282c34', fg='#61dafb', selectcolor='#282c34').pack()
        tk.Radiobutton(self.root, text="3-Bed Non-ac", variable=room_type_var, value=3, font=("Helvetica", 14), bg='#282c34', fg='#61dafb', selectcolor='#282c34').pack()
        tk.Radiobutton(self.root, text="3-Bed ac", variable=room_type_var, value=4, font=("Helvetica", 14), bg='#282c34', fg='#61dafb', selectcolor='#282c34').pack()

        tk.Button(self.root, text="Submit", command=submit_booking, font=("Helvetica", 14), bg='#61dafb', fg='#282c34', activebackground='#282c34', activeforeground='#61dafb').pack(pady=10)
        tk.Button(self.root, text="Back", command=self.home, font=("Helvetica", 14), bg='#61dafb', fg='#282c34', activebackground='#282c34', activeforeground='#61dafb').pack(pady=5)

    def create_label(self, text):
        tk.Label(self.root, text=text, font=("Helvetica", 14), bg='#282c34', fg='#61dafb').pack()

    def rooms_info(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="HOTEL ROOMS INFO", font=("Helvetica", 20, "bold"), pady=20, bg='#282c34', fg='#61dafb').pack()
        info = """
STANDARD NON-AC
Room amenities include: 1 Double Bed, Television, Telephone,
Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and
an attached washroom with hot/cold water.

STANDARD AC
Room amenities include: 1 Double Bed, Television, Telephone,
Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and
an attached washroom with hot/cold water + Window/Split AC.

3-Bed NON-AC
Room amenities include: 1 Double Bed + 1 Single Bed, Television,
Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa, 1
Side table, Balcony with an Accent table with 2 Chair and an
attached washroom with hot/cold water.

3-Bed AC
Room amenities include: 1 Double Bed + 1 Single Bed, Television,
Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa,
1 Side table, Balcony with an Accent table with 2 Chair and an
attached washroom with hot/cold water + Window/Split AC.
"""
        tk.Label(self.root, text=info, justify="left", font=("Helvetica", 14), bg='#282c34', fg='#61dafb').pack(pady=10)
        tk.Button(self.root, text="Back", command=self.home, font=("Helvetica", 14), bg='#61dafb', fg='#282c34', activebackground='#282c34', activeforeground='#61dafb').pack(pady=10)

    def rest(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="RESTAURANT MENU", font=("Helvetica", 20, "bold"), pady=20, bg='#282c34', fg='#61dafb').pack()
        menu = """
------------------------------------------------------------------------- 
                            Hotel Around the Village
------------------------------------------------------------------------- 
                            Menu Card
------------------------------------------------------------------------- 
 BEVERAGES                              26 Dal Fry................ 140.00 
----------------------------------      27 Dal Makhani............ 150.00 
 1 Regular Tea............. 20.00       28 Dal Tadka.............. 150.00 
 2 Masala Tea.............. 25.00       ROTI 
 3 Coffee.................. 25.00       --------------------------------- 
 4 Cold Drink.............. 25.00       29 Plain Roti............... 15.00 
 5 Bread Butter............ 30.00       30 Butter Roti.............. 15.00 
 6 Bread Jam............... 30.00       31 Tandoori Roti............ 20.00 
 7 Veg. Sandwich........... 50.00       32 Butter Naan.............. 20.00 
 8 Veg. Toast Sandwich..... 50.00       RICE 
 9 Cheese Toast Sandwich... 70.00       --------------------------------- 
 10 Grilled Sandwich....... 70.00       33 Plain Rice.............. 90.00 
 SOUTH INDIAN                           34 Jeera Rice............. 110.00 
----------------------------------      35 Veg Pulao.............. 110.00 
 11 Plain Dosa............. 50.00       36 Peas Pulao............. 110.00 
 12 Onion Dosa............. 70.00       CHINESE 
 13 Masala Dosa............ 70.00       --------------------------------- 
 14 Paneer Dosa............ 70.00       37 Veg Fried Rice......... 110.00 
 15 Rice Plate............. 70.00       38 Veg Hakka Noodles...... 130.00 
 MAIN COURSE                            39 Veg. Manchurian......... 150.00 
----------------------------------      40 Chilli Paneer.......... 150.00 
 16 Shahi Paneer........... 110.00      41 Veg. Schezwan Noodles.. 150.00 
 17 Kadai Paneer........... 110.00      42 Veg. American Chop Suey 150.00 
 18 Handi Paneer........... 120.00      DESSERT 
 19 Palak Paneer........... 120.00      --------------------------------- 
 20 Chilli Paneer.......... 140.00      43 Vanilla Ice Cream....... 60.00 
 21 Matar Mushroom......... 140.00      44 Strawberry Ice Cream.... 60.00 
 22 Mix Veg................ 140.00      45 Pineapple Ice Cream..... 60.00 
 23 Jeera Aloo............. 140.00      46 Butter Scotch Ice Cream. 60.00 
 24 Malai Kofta............ 140.00      47 Black Forest............ 60.00 
 25 Aloo Matar............. 140.00      48 Gulab Jamun............. 30.00 
-------------------------------------------------------------------------
"""
        tk.Label(self.root, text=menu, justify="left", font=("Helvetica", 12), bg='#282c34', fg='#61dafb').pack(pady=10)
        tk.Button(self.root, text="Back", command=self.home, font=("Helvetica", 14), bg='#61dafb', fg='#282c34', activebackground='#282c34', activeforeground='#61dafb').pack(pady=10)

    def pay(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="PAYMENT", font=("Helvetica", 20, "bold"), pady=20, bg='#282c34', fg='#61dafb').pack()

        cust_id_var = tk.StringVar()

        def calculate_payment():
            cid = cust_id_var.get()
            try:
                cid = int(cid)
            except ValueError:
                messagebox.showerror("Error", "Invalid customer ID.")
                return

            if cid not in custid:
                messagebox.showerror("Error", "Customer ID not found.")
                return

            index = custid.index(cid)
            room_cost = price[index] * day[index]
            restaurant_bill = p[index]
            total_cost = room_cost + restaurant_bill

            details = f"""
Customer name: {name[index]}
Phone number: {phoneno[index]}
Address: {add[index]}
Check-in date: {checkin[index]}
Check-out date: {checkout[index]}
Room type: {room[index]}
Room cost: {room_cost}
Restaurant bill: {restaurant_bill}
Total cost: {total_cost}
"""
            messagebox.showinfo("Payment Details", details)

        self.create_label("Enter Customer ID:")
        tk.Entry(self.root, textvariable=cust_id_var, font=("Helvetica", 14)).pack()
        tk.Button(self.root, text="Calculate Payment", command=calculate_payment, font=("Helvetica", 14), bg='#61dafb', fg='#282c34', activebackground='#282c34', activeforeground='#61dafb').pack(pady=10)
        tk.Button(self.root, text="Back", command=self.home, font=("Helvetica", 14), bg='#61dafb', fg='#282c34', activebackground='#282c34', activeforeground='#61dafb').pack(pady=10)

    def record(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="RECORDS", font=("Helvetica", 20, "bold"), pady=20, bg='#282c34', fg='#61dafb').pack()

        if not name:
            tk.Label(self.root, text="No records found.", font=("Helvetica", 14), bg='#282c34', fg='#61dafb').pack(pady=10)
        else:
            for i in range(len(name)):
                record = f"""
Customer name: {name[i]}
Phone number: {phoneno[i]}
Address: {add[i]}
Check-in date: {checkin[i]}
Check-out date: {checkout[i]}
Room type: {room[i]}
Restaurant bill: {p[i]}
Customer ID: {custid[i]}
Room number: {rc[i]}
"""
                tk.Label(self.root, text=record, justify="left", font=("Helvetica", 12), bg='#282c34', fg='#61dafb').pack(pady=5)

        tk.Button(self.root, text="Back", command=self.home, font=("Helvetica", 14), bg='#61dafb', fg='#282c34', activebackground='#282c34', activeforeground='#61dafb').pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = HotelApp(root)
    root.mainloop()