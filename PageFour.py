from Tkinter import *
import ttk, login_util, WattTime_Util, Query

import Tkinter as tk

class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Latest Bill", font=WattTime_Util.LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                           command=lambda: controller.show_frame(Query.Query))
        button1.pack()
