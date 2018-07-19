from Tkinter import *
import ttk, login_util, WattTime_Util, PageOne, PageTwo, PageThree, PageFour

import Tkinter as tk

class Query(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="MENU", font=WattTime_Util.LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = tk.Button(self, text="",
                            command=lambda: controller.show_frame(PageOne.PageOne))
        button.pack()
        #
        # button2 = tk.Button(self, text="Display Current Tariff",
        #                     command=lambda: controller.show_frame(PageTwo.PageTwo))
        # button2.pack()
        #
        # button3 = tk.Button(self, text="View List of Rates",
        #                    command=lambda: controller.show_frame(PageThree.PageThree))
        # button3.pack()
        #
        # button4 = tk.Button(self, text="View Latest Bill",
        #                     command=lambda: controller.show_frame(PageFour.PageFour))
        # button4.pack()
