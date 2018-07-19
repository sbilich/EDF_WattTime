from Tkinter import *
import ttk, login_util, WattTime_Util, Query

import Tkinter as tk

class LogIn(tk.Frame):

    def LogInCheck(self):
        global usrEntry
        global passEntry

        usrNum = usrEntry.get()
        passNum = passEntry.get()

        response = login_util.login(WattTime_Util.WATT_TOK, usrNum, passNum)

        if not (type(response) is NoneType):
            print "Response code: " + str(response.getcode())

        print("LOGIN FUNCTION")
        if not (type(response) is NoneType) and response.getcode() == 200:
            print("CORRECT")
            self.controller.show_frame(Query.Query)
        else:
            print("INCORRECT")
            loginLabel = ttk.Label(self, text = "invalid username/password", font = WattTime_Util.SMALL_FONT, foreground="red")
            loginLabel.grid(row=4, column=2) #.pack(side = BOTTOM, anchor = S, expand = YES)
            self.controller.show_frame(LogIn)

    def __init__(self, parent, controller):

        global usrEntry
        global passEntry
        self.controller = controller

        print parent.grid_size()

        tk.Frame.__init__(self, parent)

        introLabel = ttk.Label(self, text = "Welcome To The EDF WattTime Tool.\nLogin With Your Username and Password", font = WattTime_Util.LARGE_FONT)
        introLabel.grid(row=2, column=1) #.pack(side = TOP, anchor = N, expand = YES)

        usrLabel = Label(self, text = 'Username:')
        usrEntry = Entry(self)


        passLabel = Label(self, text = 'Password: ')
        passEntry = Entry(self, show ="*")

        usrLabel.grid(row=3, column=0) #.pack(pady =10, padx = 50, side = LEFT, anchor = N)
        usrEntry.grid(row=3, column=1) #.pack(pady =10, padx = 50, side = LEFT, anchor = N)

        passLabel.grid(row=4, column=0) #.pack(pady =100, padx = 10, side = LEFT, anchor  = S)
        passEntry.grid(row=4, column=1) #pack(pady =100, padx = 10, side = LEFT, anchor  = S)

        #  runs the 'LoginCheck' function

        logInButton = tk.Button(self, text = "Login",
                                 command = self.LogInCheck)
        logInButton.grid(row=3, column=2) #.pack(side = LEFT)#, anchor = N)

        quitButton = tk.Button(self, text = "Quit", command = quit)
        quitButton.grid(row=5, column=1) #.pack(side = BOTTOM, anchor = S)
