import customtkinter as tk
from customtkinter import filedialog
from helper import *
from CTkMessagebox import CTkMessagebox

tk.set_appearance_mode("System")
tk.set_default_color_theme("blue")
class CSVUploader(tk.CTk):
      width = 900
      height = 600
      
      def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("UTRGV UREC Banner Fix")
        self.geometry(f'{self.width}x{self.height}')
        
        
        self.header = tk.CTkLabel(self, text="UTRGV UREC Banner Fix", font=tk.CTkFont(size=50, weight='bold'))
        self.header.place(relx= 0.5, rely=0.3, anchor=tk.CENTER)
        self.text =tk.CTkLabel(self, text= "Please Choose A CSV File", font=tk.CTkFont(size=15, weight="bold"))
        self.text.place(relx = 0.5, rely = 0.4, anchor= tk.CENTER)
        self.button = tk.CTkButton(self, height= 50, text="Choose CSV File", command=self.select_file)
        self.button.place(relx = 0.5, rely = 0.5, anchor= tk.CENTER)
        self.creator = tk.CTkLabel(self, text="Created by Jobey Farias") 
        self.creator.place(relx=0.99, rely=0.99, anchor=tk.SE)


      def select_file(self):
        try:        
          file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])            
          with open(file_path, "r") as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)

            dataset = remove_2nd_address(rows)
            dataset = check_state(rows)
            dataset = check_phone_number(rows)
            dataset = check_zip_code(rows)
            print(dataset)
        except FileNotFoundError:
          CTkMessagebox(title="Error", message="File Cannot Be Found Or File Not Chosen.", icon="cancel")



if __name__ == "__main__":
    app = CSVUploader()
    app.mainloop()
