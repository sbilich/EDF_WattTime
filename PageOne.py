from Tkinter import *
import ttk, login_util, WattTime_Util, Query

import Tkinter as tk

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Account Balance", font=WattTime_Util.LARGE_FONT)
        label.pack(pady=10,padx=10)

        sublabel = tk.Label(self, text="Your current account balance is 230", font=WattTime_Util.SMALL_FONT)
        sublabel.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Menu",
                           command=lambda: controller.show_frame(Query.Query))
        button1.pack()
