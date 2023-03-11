import tkinter as tk
from tkinter import *
from tkinter import ttk

class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(width=400, height=300)
        self.title("Easy Home Search")
        
        # Create a label
        label1 = tk.Label(self, text="Welcome to the Easy Home Search application!")
        label1.pack()


        # Create a label to display instructions
        instructions_label = tk.Label(self, text="Minimum Price:")
        instructions_label.pack()

        # Create an entry widget for the user to enter the Minimum Price
        minPrice_entry = tk.Entry(self)
        minPrice_entry.pack()

        # Create a label to display instructions
        instructions_label = tk.Label(self, text="Maximum Price:")
        instructions_label.pack()

        # Create an entry widget for the user to enter the Maximum Price
        maxPrice_entry = tk.Entry(self)
        maxPrice_entry.pack()

        # Create a label to display instructions
        instructions_label = tk.Label(self, text="Minimum Bedrooms:")
        instructions_label.pack()

        # Create an entry widget for the user to enter the Minimum Bedrooms
        minBed_entry = tk.Entry(self)
        minBed_entry.pack()

        # Create a label to display instructions
        instructions_label = tk.Label(self, text="Maximum Bedrooms:")
        instructions_label.pack()

        # Create an entry widget for the user to enter the Maximum Bedrooms
        maxBeds_entry = tk.Entry(self)
        maxBeds_entry.pack()

        # Create a label to display instructions
        instructions_label = tk.Label(self, text="Minimum Baths:")
        instructions_label.pack()

        # Create an entry widget for the user to enter the Minimum Baths
        minBaths_entry = tk.Entry(self)
        minBaths_entry.pack()

        # Create a label to display instructions
        instructions_label = tk.Label(self, text="Maximum Baths:")
        instructions_label.pack()

        # Create an entry widget for the user to enter the Maximum Baths
        maxBaths_entry = tk.Entry(self)
        maxBaths_entry.pack()


        # Create a label to display instructions
        instructions_label = tk.Label(self, text="Zipcode:")
        instructions_label.pack()

        # Create an entry widget for the user to enter the Zipcode
        zipCode_entry = tk.Entry(self)
        zipCode_entry.pack()

        # Create a label to display instructions
        instructions_label = tk.Label(self, text="Radius:")
        instructions_label.pack()

        # Create an entry widget for the user to enter the Radius
        radius_entry = tk.Entry(self)
        radius_entry.pack()
        
        # Create a button that opens a secondary window
        button1 = tk.Button(self, text="Next", command=self.open_secondary_window)
        button1.pack()
        
        # Create a button that exits the application
        button2 = tk.Button(self, text="Exit", command=self.destroy)
        button2.pack()
        
    def open_secondary_window(self):
        # Create secondary (or popup) window.
        newWindow = tk.Toplevel()
        newWindow.title("Contact Information")
        newWindow.config(width=500, height=600)

        # Create a label
        label1 = tk.Label(newWindow, text="Please enter your contact information")
        label1.pack()

        # Create a label to display instructions
        instructions_label = tk.Label(newWindow, text="Name:")
        instructions_label.pack()

        # Create an entry widget for the user to enter name
        name_entry = tk.Entry(newWindow)
        name_entry.pack()

        # Create a label to display instructions
        instructions_label = tk.Label(newWindow, text="Email:")
        instructions_label.pack()

        # Create an entry widget for the user to enter email
        email_entry = tk.Entry(newWindow)
        email_entry.pack()

        # Create a label to display instructions
        instructions_label = tk.Label(newWindow, text="Phone:")
        instructions_label.pack()

        # Create an entry widget for the user to enter the phone
        phone_entry = tk.Entry(newWindow)
        phone_entry.pack()
        
        # Create a button for user to click submit
        convert_button = tk.Button(newWindow, text="Submit", command=self.show_result)
        convert_button.pack()

        # Create a button that exits the application
        button2 = tk.Button(newWindow, text="Exit", command=newWindow.destroy)
        button2.pack()
        
        newWindow.focus()
        newWindow.grab_set()
        
    def show_result(self):
        # Create third (or popup) window.
        lastWindow = tk.Toplevel()
        lastWindow.title("Thank you")
        lastWindow.config(width=300, height=200)
        
        # Create a label with the result
        result_label = tk.Label(lastWindow, text="Thank you for your information, a realtor will be contacting you shortly with a list of homes you may like.")
        result_label.pack()
        
        # Create a button to close (destroy) this window.
        convert_button = tk.Button(lastWindow, text="Close window", command=lastWindow.destroy)
        convert_button.pack()
        
        lastWindow.focus()
        lastWindow.grab_set()
        
if __name__ == "__main__":
    # Create the main window
    root = MainWindow()
    root.mainloop()
