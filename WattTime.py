from Tkinter import *
import ttk, login_util, WattTime_Util, LogIn, Query
import PageOne, PageTwo, PageThree, PageFour, PageFive

import Tkinter as tk

WATT_TOK = "WATT_TOK"

class WattTime(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)#, height=650, width=800)

        # container.pack(side="top", fill="both", expand = True)
        container.grid(row=0, column=0)
        # width = 4
        # for i in range(width+1):
        #     container.grid_columnconfigure(i, weight=1, uniform="foo")
        # height = 4
        # for i in range(height+1):
        #     container.grid_rowconfigure(i, weight=1, uniform="foo")

        self.frames = {}

        for F in (Query.Query, PageOne.PageOne, PageTwo.PageTwo, PageThree.PageThree,
         PageFour.PageFour, PageFive.PageFive, LogIn.LogIn):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LogIn.LogIn)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

if __name__ == "__main__":
    app = WattTime()
    app.lift()
    app.attributes('-topmost',True)
    app.after_idle(app.attributes,'-topmost',False)

    # w = 800 # width for the Tk root
    # h = 650 # height for the Tk root
    #
    # # get screen width and height
    # ws = app.winfo_screenwidth() # width of the screen
    # hs = app.winfo_screenheight() # height of the screen
    #
    # # calculate x and y coordinates for the Tk root window
    # x = (ws/2) - (w/2)
    # y = (hs/2) - (h/2)
    #
    # # set the dimensions of the screen
    # # and where it is placed
    # app.geometry('%dx%d+%d+%d' % (w, h, x, y))

    app.mainloop()
