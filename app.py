import customtkinter as tk
from customtkinter import filedialog
import csv

def check_zip_code(dataset):
    with open("zcodes.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        list_of_valid_zips = list(reader)
    for row in dataset:
        if(row[7] == 'ZIPCODE'):
            continue
        if(row[7] not in list_of_valid_zips or len(row[0]) == 0):
            row[7] = "78542"
    return dataset

def remove_2nd_address(dataset):
    default_address = "W Schunior St"
    for row in dataset:
        if(row[2] == 'The University Of Texas Rio'):
            row[2] = default_address
            row[3] = ""
    return dataset    
    

def check_state(dataset):
    default_state = 'TX'
    default_city = "Edinburg"
    for row in dataset:
        if (row[6] == 'STATE'):
            continue
        if(row[6] != default_state):
            row[6] = default_state
            row[5] = default_city
    return dataset

def check_phone_number(dataset):
    default_phone = '9565555555'
    for row in dataset:
        if(row[8]== 'CELLPHONE'):
            continue
        if(len(row[8]) != 10 or len(row[9]) != 10):
            row[8] = default_phone
            row[9] = default_phone
    return dataset
    
def select_file():
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        with open(file_path, "r") as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)

            dataset = remove_2nd_address(rows)
            dataset = check_state(rows)
            dataset = check_phone_number(rows)
            dataset = check_zip_code(rows)
            



# Custom Tkinter Portion
tk.set_appearance_mode("System")
tk.set_default_color_theme("blue")
    
app = tk.CTk()    
app.geometry("1024x768")
app.title("UTRGV UREC Banner Fix")
header = tk.CTkLabel(app, text="UTRGV UREC Banner Fix", font=tk.CTkFont(size=50, weight='bold'))
header.place(relx= 0.5, rely=0.3, anchor=tk.CENTER)
text =tk.CTkLabel(app, text= "Please Choose A CSV File", font=tk.CTkFont(size=15, weight="bold"))
text.place(relx = 0.5, rely = 0.4, anchor= tk.CENTER)
button = tk.CTkButton(app, height= 50, text="Choose CSV File", command=select_file)
button.place(relx = 0.5, rely = 0.5, anchor= tk.CENTER)
creator = tk.CTkLabel(app, text="Created by Jobey Farias") 
creator.place(relx=0.99, rely=0.99, anchor=tk.SE)

app.mainloop()

