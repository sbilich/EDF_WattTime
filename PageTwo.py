from Tkinter import *
import ttk, login_util, WattTime_Util, Query, PageFive

import Tkinter as tk

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        # global WattTime_Util.current_tariff
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Current Tariff", font=WattTime_Util.LARGE_FONT)
        label.pack(pady=10,padx=10)

        sublabel = tk.Label(self, text="Your current tariff is "+str(WattTime_Util.current_tariff), font=WattTime_Util.SMALL_FONT)
        sublabel.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Change Tariff",
                            command=lambda: controller.show_frame(PageFive.PageFive))
        button1.pack()

        button2 = tk.Button(self, text="Back to Home",
                           command=lambda: controller.show_frame(Query.Query))
        button2.pack()
