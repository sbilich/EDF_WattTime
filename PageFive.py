from Tkinter import *
import ttk, login_util, WattTime_Util, Query

import Tkinter as tk

def tariff_A():
    # global current_tariff
    WattTime_Util.current_tariff= "A"

def tariff_B():
    # global current_tariff
    WattTime_Util.current_tariff= "B"

def tariff_C():
    # global current_tariff
    WattTime_Util.current_tariff= "C"


class PageFive(tk.Frame):

    def __init__(self, parent, controller):
        # global WattTime.current_tariff
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Change Tariff", font=WattTime_Util.LARGE_FONT)
        label.pack(pady=10,padx=10)

        sublabel = tk.Label(self, text="Select new tariff\nView list of tariff rates on the main menu to see the prices.", font=WattTime_Util.SMALL_FONT)
        sublabel.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="A",
                            command=lambda:[controller.show_frame(Query.Query),tariff_A])
        button1.pack()

        button2 = tk.Button(self, text="B",
                            command=lambda:[controller.show_frame(Query.Query),tariff_B])
        button2.pack()

        button3 = tk.Button(self, text="C",
                            command=lambda:[controller.show_frame(Query.Query),tariff_C])
        button3.pack()

        button4 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(Query.Query))
        button4.pack()
