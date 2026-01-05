import tkinter as tk
from tkinter import *
from tkinter import ttk

class Mainframe():
    def __init__(self, parent):
        self.mainframe = tk.Frame(parent)
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        
        
        def add_device():
            device = self.list_of_devices_entry.get()
            if device:
                list_of_devices.append(device)
                self.all_devices_listbox.insert(END, device)
        
        def remove_device():
            selected_indices = self.all_devices_listbox.curselection()
            for index in reversed(selected_indices):
                self.all_devices_listbox.delete(index)
                del list_of_devices[index]
        
        
        
        
        
        user_label = tk.Label(self.mainframe, text="User reported by: ")
        user_label.grid(column=0, row=0, sticky=W, padx=5, pady=5)
        self.user_entry_var = StringVar()
        self.user_entry = tk.Entry(self.mainframe, width=30, textvariable=self.user_entry_var)
        self.user_entry.grid(column=1, row=0, sticky=W, padx=5, pady=5)
    
        list_of_devices = []
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
        self.all_devices_listbox.grid(column=4,columnspan=3, row=1, rowspan=4, sticky=(N,S), padx=(15,0), pady=5)
        self.all_devices_listbox_scrollbar = tk.Scrollbar(self.mainframe, orient=VERTICAL, command=self.all_devices_listbox.yview)
        self.all_devices_listbox_scrollbar.grid(column=7, row=1, rowspan=4, sticky=(N,S,W), padx=(0,5), pady=5)
    
        
        
        location_label = tk.Label(self.mainframe, text="Location: ")
        location_label.grid(column=0, row=1, sticky=W, padx=5, pady=5)
        self.location_entry_var = StringVar()
        self.location_entry = tk.Entry(self.mainframe, width=30, textvariable=self.location_entry_var)
        self.location_entry.grid(column=1, row=1, sticky=W, padx=5, pady=5)
        
        
        
        
        department_label = tk.Label(self.mainframe, text="Department: ")
        department_label.grid(column=0, row=2, sticky=W, padx=5, pady=5)
        self.department_entry_var = StringVar()
        self.department_entry = tk.Entry(self.mainframe, width=30, textvariable=self.department_entry_var)
        self.department_entry.grid(column=1, row=2, sticky=W, padx=5, pady=5)
        
        
        
        
        self.issue_type_var = StringVar()
        self.issue_type_var.set("PC")
        self.issue_type_box = ttk.Combobox(self.mainframe, values=("PC", "Printer", "Tracker", "Laptop", "Scanner", "Mobile Phone"), textvariable=self.issue_type_var, width=10)
        self.issue_type_box.grid(column=1, row=3, sticky=W, padx=5, pady=5)
        issue_type_label = tk.Label(self.mainframe, text="Issue Type: ")
        issue_type_label.grid(column=0, row=3, sticky=W, padx=5, pady=5)
        
        
        
        self.short_description_label_var = StringVar()
        short_description_label = tk.Label(self.mainframe, text="Short description of Issue: ")
        short_description_label.grid(column=0, row=4, sticky=W, padx=5, pady=5)
        self.short_description_entry = tk.Entry(self.mainframe, width=80, textvariable=self.short_description_label_var)
        self.short_description_entry.grid(column=1, columnspan=3, row=4, sticky=(W, E), padx=5, pady=5)
        
        
        
        
        self.detailed_description_label_var = StringVar()
        detailed_description_label = tk.Label(self.mainframe, text="Detailed description of Issue: ")
        detailed_description_label.grid(column=0, row=5, sticky=W, padx=5, pady=5)
        self.detailed_description_entry = tk.Text(self.mainframe, width=80, height=10)
        self.detailed_description_entry.grid(column=1, columnspan=3, row=5, sticky=(W, E), padx=5, pady=5)
        
        
        self.submit_button = tk.Button(self.mainframe, text="Submit Tickets")
        self.submit_button.grid(column=7, row=5, sticky=(S, E), padx=5, pady=10)
