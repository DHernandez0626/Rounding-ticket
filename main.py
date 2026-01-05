import ui
import tkinter as tk
from tkinter import *
from playwright.sync_api import sync_playwright
import pyautogui as pyauto


# playwright = sync_playwright().start()
# Use playwright.chromium, playwright.firefox or playwright.webkit
# Pass headless=False to launch() to see the browser UI

SERVICE_WEBSITE = "https://hcaservicecentral.service-now.com/now/nav/ui/classic/params/target/incident.do%3Fsys_id%3D-1%26sysparm_query%3Dactive%3Dtrue%26sysparm_stack%3Dincident_list.do%3Fsysparm_query%3Dactive%3Dtrue"

root = tk.Tk( )
root.title("Rounding Ticket App")
root.configure(padx=10, pady=10)
root. minsize(1300, 300)

mainframe = ui.Mainframe(root)





# browser = playwright.chromium.launch(headless=False, channel="msedge")
# page = browser.new_page()
# page.goto(SERVICE_WEBSITE, wait_until="networkidle")
# pyauto.PAUSE = 2

# pyauto.write("Danny Hernandez")

# page.pause()





root.mainloop()