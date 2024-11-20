from tkinter import *
import os


# More than one frame/one tab
# At least one image
# customer class, stores info about customer; at least 3 pieces of info X
# standard contrusctor methods(?), method write customers info into txt. file X
# store information of customer into txt X
# read and access customer data from the .txt File X
# add/remove customers from you list/program X
# create a dropdown menu that allows you to select, display, and edit info about your customer

def update_customers(customers_list):      #updates customer_data.txt. file --> replaces with list inputted as a parameter
    file = open('customer_data.txt','w')
    file.write(categories+"\n")
    for item in customers_list:
        file.write(item+"\n")
    file.close()
    with open("customer_data.txt", "r") as source_file:
        with open("../stored_data/stored_data.txt", "w") as destination_file:
            destination_file.write(source_file.read())  #updates personal data file
    with open("customer_data.txt", "w") as f:
        pass  # This will clear the program file


def remove_customer(customers_list, customer):    #removes specified customer from customer list and calls update_customer method
    customers_list.remove(customer)
    update_customers(customers_list)

customers = ["blank"]
try:
    with open("../stored_data/stored_data.txt", "r") as f:
        customers = f.readlines()
        print(customers)

    for i in range(0, len(customers)):
        customers[i] = customers[i].strip("\n")
    categories = "name, age, email"
    customers.pop(0)
except:
    user_home = os.path.expanduser("~")  # Get the user's home directory
    folder_path = os.path.join(user_home, "stored_data")  # Define the folder path
    file_path = os.path.join(folder_path, "stored_data.txt") #Define the file path
    os.makedirs(folder_path, exist_ok=True)
    with open(file_path, 'w') as f: #creates a folder containing a .txt file in the user's directory
        print("Stored_data folder created in user directory")
    categories = "name, age, email"
    customers.pop(0)
    print(customers)

root = Tk()
root.geometry("400x400")
root.title("Select Customer")

# different windows

def show():
    myLabel = Label(root, text=customer_button.get()).pack()


def update_root():
    print(customers)
    global customer_button
    global drop
    drop.children["menu"].delete(0,"end")
    for c in customers:
        drop.children["menu"].add_command(label=c, command=lambda cus = c: customer_button.set(cus))
    customer_button.set("Customers")
    

def open_remove_window():
    def remove():
        customer = customer_button.get()
        print(customer)
        remove_customer(customers, customer)
        top.destroy()
        update_root()

    top = Toplevel()
    top.title("Remove Customer")
    top.geometry("400x400")
    top_label = Label(top, text = "Remove Customer\nWill remove customer selected in 'Select Customer' window").pack()
    removed_customer_label = Label(top, text= "This Willl Remove " + customer_button.get()).pack()
    remove_button = Button(top, text="Remove Customer", command=remove).pack()
    close_button = Button(top, text="Close Window", command=top.destroy).pack()

def open_add_window():
    def add():
        new_customer = name_entry.get() + ", " + age_entry.get() + ", " + email_entry.get()
        customers.append(new_customer)
        update_customers(customers)
        name_entry.delete(0,"end")
        age_entry.delete(0,"end")
        email_entry.delete(0,"end")
        name_entry.insert(0,"Enter Your Name")
        age_entry.insert(0,"Enter Your Age")
        email_entry.insert(0,"Enter Your Email")
        update_root()

    top = Toplevel()
    top.title("Add Customer")
    top.geometry("400x400")
    top_label = Label(top, text="Add Customer").pack()

    name_entry = Entry(top)
    name_entry.pack()
    name_entry.insert(0,"Enter Your Name")

    age_entry = Entry(top)
    age_entry.pack()
    age_entry.insert(0,"Enter Your Age")

    email_entry = Entry(top)
    email_entry.pack()
    email_entry.insert(0,"Enter Your Email")

    add_button = Button(top, text="Add Customer to database", command=add).pack()   #add command
    close_button = Button(top, text="Close Window", command=top.destroy).pack()

def open_edit_window():
    def apply_edit():
        new_customer = name_entry.get() + ", " + age_entry.get() + ", " + email_entry.get()
        customers.remove(customer_button.get())
        customers.append(new_customer)
        update_customers(customers)
        name_entry.delete(0,"end")
        age_entry.delete(0,"end")
        email_entry.delete(0,"end")
        top.destroy()
        update_root()

    top = Toplevel()
    top.title("Edit Customer")
    top.geometry("400x400")
    top_label = Label(top, text="Edit Customer").pack()

    customer_list = customer_button.get().split(", ")
    print(customer_list)

    name_entry = Entry(top)
    name_entry.pack()
    name_entry.insert(0, customer_list[0])

    age_entry = Entry(top)
    age_entry.pack()
    age_entry.insert(0, customer_list[1])

    email_entry = Entry(top)
    email_entry.pack()
    email_entry.insert(0, customer_list[2])

    edit_button = Button(top, text="Apply Changes", command=apply_edit).pack()
    close_button = Button(top, text="Close Window", command=top.destroy).pack()

global customer_button
customer_button = StringVar()
customer_button.set("Customers")
global drop

try:
    drop = OptionMenu(root, customer_button, *customers)
    drop.pack()
except:
    blank = ["blank"]
    drop = OptionMenu(root, customer_button, *blank)
    drop.pack()

show_data_button = Button(root, text="Show Customer", command=show).pack()

remove_customer_window = Button(root, text="Remove Customer", command=open_remove_window).pack()
add_customer_window = Button(root, text="Add Customer", command=open_add_window).pack()
edit_customer_window = Button(root, text="Edit Customer", command=open_edit_window).pack()

print(customers)
f.close()
root.mainloop()