from Tkinter import *
import ttk, login_util, WattTime_Util, Query

import Tkinter as tk

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Tariff Rates", font=WattTime_Util.LARGE_FONT)
        label.pack(pady=10,padx=10)

        sublabel = tk.Label(self, text="Peak Rates: A: 0.30 | B: 0.10 | C: 0.90", anchor="w", font=WattTime_Util.SMALL_FONT)
        sublabel.pack(pady=10,padx=10)

        sublabel2 = tk.Label(self, text="Off Peak: A: 0.05 | B: 0.02 | C: -", anchor="w", font=WattTime_Util.SMALL_FONT)
        sublabel2.pack(pady=10,padx=10)

        sublabel3 = tk.Label(self, text="Line Rental: A: 15.00 | B: 20.00 | C: 30.00", anchor="w", font=WattTime_Util.SMALL_FONT)
        sublabel3.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                           command=lambda: controller.show_frame(Query.Query))
        button1.pack()
