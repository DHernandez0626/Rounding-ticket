#This program is strictly for use by HCA IT employees to automate the creation of rounding tickets.
#Unauthorized use of this program is prohibited and may result in disciplinary action.
#This program is provided "as is" without warranty of any kind.
#HCA IT expressly disclaims all implied warranties including, without limitation, the implied warranties of
#merchantability and fitness for a particular purpose. In no event shall HCA IT be liable for any damages
#arising out of the use of or inability to use this program, even if HCA IT has been advised of the possibility of such damages.

#Should any questions regarding the use or purpose of this program arise, please contact me personally at danny.hernandez9788@gmail.com and i will be glad to answer them.

import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from playwright.sync_api import sync_playwright
import pyautogui as pyauto
import time



SERVICE_WEBSITE = "https://hcaservicecentral.service-now.com/now/nav/ui/classic/params/target/incident.do%3Fsys_id%3D-1%26sysparm_query%3Dactive%3Dtrue%26sysparm_stack%3Dincident_list.do%3Fsysparm_query%3Dactive%3Dtrue"



class Mainframe():
    """
    Docstring for Mainframe:
    The main frame for the Rounding Ticket App GUI.
    Contains all input fields, labels, and buttons for ticket submission.
    Requires a main window as this is considered a child frame.
    main app should include a root that calls for this class 
    root = tk.Tk( )
    mainframe = ui.Mainframe(root)
    """
    
    def __init__(self, parent):
        self.mainframe = tk.Frame(parent)
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        
        
        # Define categories and subcategories for ticket types
        self.CATEGORY = ["PC", "Printer", "Tracker", "Laptop", "Scanner", "Mobile Phone"]
        self.HARDWARE_SUBCATEGORIES = ("Broken", "Consumables (Paper/Toner/Ink)", "Hardware Failure", "Hardware Installation/Setup")
        self.APPLICATION_SUBCATEGORIES = ("Configuration/Functionality", "Connectivity")
        self.NETWORK_SUBCATEGORIES = ("Connectivity – External", "Connectivity – Internal", "Hardware Failure", "Hardware Upgrade")
        self.STORAGE_SUBCATEGORIES = ("Capacity")
        self.subissue_type_var = StringVar()
        
        
        # def show_subcategories(*args):
        
        # Functions for adding and removing devices from the listbox
        def add_device():
            device = self.list_of_devices_entry.get()
            if device:
                self.list_of_devices.append(device)
                self.all_devices_listbox.insert(END, device)
        
        def remove_device():
            selected_indices = self.all_devices_listbox.curselection()
            for index in reversed(selected_indices):
                self.all_devices_listbox.delete(index)
                del self.list_of_devices[index]
        
        # Label and Entry for User reported by: section
        user_label = tk.Label(self.mainframe, text="User reported by: ")
        user_label.grid(column=0, row=0, sticky=W, padx=5, pady=5)
        self.user_entry_var = StringVar()
        self.user_entry = tk.Entry(self.mainframe, width=30, textvariable=self.user_entry_var)
        self.user_entry.grid(column=1, row=0, sticky=W, padx=5, pady=5)
    
        # Listbox and related widgets for List of Devices
        self.list_of_devices = []
        list_of_devices_label = tk.Label(self.mainframe, text="List of Devices (if applicable): ")
        list_of_devices_label.grid(column=3, row=0, sticky=E, padx=5, pady=5)
        self.location_entry_var = StringVar()
        self.list_of_devices_entry = tk.Entry(self.mainframe, width=20, textvariable=self.location_entry_var)
        self.list_of_devices_entry.grid(column=5, row=0, sticky=W, padx=5, pady=5)
        
        self.add_device_button = tk.Button(self.mainframe, text="Add", command=add_device)
        self.add_device_button.grid(column=6, row=0, sticky=W, padx=5, pady=5)
        self.remove_device_button = tk.Button(self.mainframe, text="Remove", command=remove_device)
        self.remove_device_button.grid(column=7, row=0, sticky=W, padx=5, pady=5)
        
        self.all_devices_listbox = tk.Listbox(self.mainframe, height=10, width=50)
        self.all_devices_listbox.grid(column=4,columnspan=3, row=1, rowspan=5, sticky=(N,S), padx=(15,0), pady=5)
        self.all_devices_listbox_scrollbar = tk.Scrollbar(self.mainframe, orient=VERTICAL, command=self.all_devices_listbox.yview)
        self.all_devices_listbox_scrollbar.grid(column=7, row=1, rowspan=5, sticky=(N,S,W), padx=(0,5), pady=5)
    
        
        # Label and Entry for Location
        location_label = tk.Label(self.mainframe, text="Location: ")
        location_label.grid(column=0, row=1, sticky=W, padx=5, pady=5)
        self.location_entry_var = StringVar()
        self.location_entry = tk.Entry(self.mainframe, width=30, textvariable=self.location_entry_var)
        self.location_entry.grid(column=1, row=1, sticky=W, padx=5, pady=5)
        
        
        
        # Label and Entry for Department
        department_label = tk.Label(self.mainframe, text="Department: ")
        department_label.grid(column=0, row=2, sticky=W, padx=5, pady=5)
        self.department_entry_var = StringVar()
        self.department_entry = tk.Entry(self.mainframe, width=30, textvariable=self.department_entry_var)
        self.department_entry.grid(column=1, row=2, sticky=W, padx=5, pady=5)
        
        
        
        # Label and Combobox for Issue Type
        self.issue_type_var = StringVar()
        self.issue_type_var.set("PC")
        self.issue_type_box = ttk.Combobox(self.mainframe, values=(self.CATEGORY), textvariable=self.issue_type_var, width=10)
        self.issue_type_box.grid(column=1, row=3, sticky=W, padx=5, pady=5)
        issue_type_label = tk.Label(self.mainframe, text="Issue Type: ")
        issue_type_label.grid(column=0, row=3, sticky=W, padx=5, pady=5)
        
        self.category_var = StringVar()
        self.category_var.set("Hardware")
        self.category_box = ttk.Combobox(self.mainframe, values=("Hardware", "Application", "Network", "Storage"), textvariable=self.category_var, width=10)
        self.category_box.grid(column=1, row=4, sticky=W, padx=5, pady=5)
        self.category_box.bind("<<ComboboxSelected>>", self.change_subcategories)
        category_label = tk.Label(self.mainframe, text="Category: ")
        category_label.grid(column=0, row=4, sticky=W, padx=5, pady=5)
        
        self.subissue_type_var.set("Hardware Failure")
        self.subissue_type_box = ttk.Combobox(self.mainframe, values=(self.HARDWARE_SUBCATEGORIES), textvariable=self.subissue_type_var, width=30)
        self.subissue_type_box.grid(column=1, row=5, sticky=W, padx=5, pady=5)
        subissue_type_label = tk.Label(self.mainframe, text="Subcategory: ")
        subissue_type_label.grid(column=0, row=5, sticky=W, padx=5, pady=5)
        
        
        # Label and Entry for Short description
        self.short_description_label_var = StringVar()
        short_description_label = tk.Label(self.mainframe, text="Short description of Issue: ")
        short_description_label.grid(column=0, row=6, sticky=W, padx=5, pady=5)
        self.short_description_entry = tk.Entry(self.mainframe, width=80, textvariable=self.short_description_label_var)
        self.short_description_entry.grid(column=1, columnspan=3, row=6, sticky=(W, E), padx=5, pady=5)
        
        
        
        # Label and Text for Detailed description
        self.detailed_description_label_var = StringVar()
        detailed_description_label = tk.Label(self.mainframe, text="Detailed description of Issue: ")
        detailed_description_label.grid(column=0, row=7, sticky=W, padx=5, pady=5)
        self.detailed_description_entry = tk.Text(self.mainframe, width=80, height=10)
        self.detailed_description_entry.grid(column=1, columnspan=3, row=7, sticky=(W, E), padx=5, pady=5)
        
        self.resolution_label_var = StringVar()
        resolution_label = tk.Label(self.mainframe, text="Resolution closing notes: ")
        resolution_label.grid(column=0, row=8, sticky=W, padx=8, pady=5)
        self.resolution_entry = tk.Text(self.mainframe, width=80, height=10)
        self.resolution_entry.grid(column=1, columnspan=3, row=8, sticky=(W, E), padx=5, pady=5)
        
        # Submit Tickets Button
        self.submit_button = tk.Button(self.mainframe, text="Submit Tickets", command=self.submit_tickets)
        self.submit_button.grid(column=8, row=7, sticky=(S, E), padx=5, pady=10)
        
        
        
    # Function to change subcategories based on selected category    
    def change_subcategories(self, *args):
        if self.category_var.get() == "Hardware":
            self.subissue_type_box.config(values=(self.HARDWARE_SUBCATEGORIES))
            self.subissue_type_var.set("Hardware Failure")
        elif self.category_var.get() == "Application":
            self.subissue_type_box.config(values=(self.APPLICATION_SUBCATEGORIES))
            self.subissue_type_var.set("Configuration/Functionality")
        elif self.category_var.get() == "Network":
            self.subissue_type_box.config(values=(self.NETWORK_SUBCATEGORIES))
            self.subissue_type_var.set("Connectivity – External")
        elif self.category_var.get() == "Storage":
            self.subissue_type_box.config(values=(self.STORAGE_SUBCATEGORIES))
            self.subissue_type_var.set("Capacity")
        
        
    # Function to gather ticket information and submit tickets after submit button is pressed
    def submit_tickets(self):
        try:
            # if any fields are empty, raise ValueError
            if self.user_entry_var.get() == "" or self.location_entry_var.get() == "" or self.department_entry_var.get() == "" or self.issue_type_var.get() == "" or self.short_description_label_var.get() == "" or self.detailed_description_entry.get("1.0", END).strip() == "" or self.resolution_entry.get("1.0", END).strip() == "":
                raise ValueError("All fields must be filled out before submitting tickets.")
        except ValueError:
            messagebox.showerror("Input Error", "All fields must be filled out before submitting tickets.")
            return
        
        playwright = sync_playwright().start()
        # Use playwright.chromium, playwright.firefox or playwright.webkit
        # Pass headless=False to launch() to see the browser UI
        
        for device in self.all_devices_listbox.get(0, END):
            browser = playwright.chromium.launch(headless=False, channel="msedge")
            page = browser.new_page()
            page.goto(SERVICE_WEBSITE, wait_until="networkidle")
            time.sleep(2)
            pyauto.PAUSE = 2
            pyauto.write(self.user_entry_var.get())
            pyauto.press("down")
            pyauto.press("enter")
            for _ in range(7):
                pyauto.press("tab")
            pyauto.write(self.location_entry_var.get())
            pyauto.press("down")
            pyauto.press("enter")
            for _ in range(3):
                pyauto.press("tab")
            pyauto.write(self.department_entry_var.get())
            for _ in range(4):
                pyauto.press("tab")
            pyauto.write(self.issue_type_var.get())
            pyauto.press("down")
            pyauto.press("enter")
            pyauto.press("tab")
            pyauto.write(self.category_var.get())
            pyauto.press("down")
            pyauto.press("enter")
            pyauto.press("tab")
            pyauto.write(self.subissue_type_var.get())
            
        
