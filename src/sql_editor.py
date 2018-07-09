import tkinter as tk               
from tkinter import font  as tkfont 
from sql_create_and_update import *

### AUTHOR: Davit Julakidze
### License: GNU PUBLIC V3
### 07/02/2018



class sqlEditor(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.frames["CreateEntry"] = CreateEntry(parent=container, controller=self)
        self.frames["UpdateEntry"] = UpdateEntry(parent=container, controller=self)

        self.frames["CreateEntry"].grid(row=0, column=0, sticky="nsew")
        self.frames["UpdateEntry"].grid(row=0, column=0, sticky="nsew")

        self.show_frame("CreateEntry")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class CreateEntry(tk.Frame):
    def __init__(self, parent, controller):
        newEntry_fields = 'First Name*', 'Last Name*', 'Location*', 'Title*', 'Office Phone', 'Mobile Phone', 'Ext', 'eMail*'
        entries = []
        warning_font = tkfont.Font(family='Helvetica', size=8, weight="bold")
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Create New Entry", font=controller.title_font)
        warning = tk.Label(self, text="Please Format all emails by capitalizing first and last initial\n E.g: Adam.Smith@structuretone.com", font= warning_font)
        label.pack(side="top", fill="x", pady=10)
        warning.pack()
        button1 = tk.Button(self, text="Go to Update entry",
                            command=lambda: controller.show_frame("UpdateEntry"))
        for field in newEntry_fields:
            row = tk.Frame(self)
            lab = tk.Label(row, width=15, text=field, anchor='w')
            ent = tk.Entry(row)
            row.pack(side="top", fill="x", padx=5, pady=5)
            lab.pack(side="left")
            ent.pack(side="right", expand="yes", fill="x")
            entries.append((field, ent))
        self.bind('<Return>', (lambda event, e=entries: fetch(e)))
        create_button = tk.Button(self, pady=15, padx= 15,text='Create',
            command=(lambda e=entries: fetch(e)))
        create_button.pack()
        button1.pack()

def fetch(entries):
    values = []
    for entry in entries:
        field = entry[0]
        values.append(entry[1].get())
        entry[1].delete(0, tk.END)
    popupmsg(make_new_entry(values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7]))



def popupmsg(msg):
    NORM_FONT = ("Helvetica", 10)
    popup = tk.Tk()
    popup.wm_title("!")
    label = tk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()




class UpdateEntry(tk.Frame):
    def __init__(self, parent, controller):
        update_font = tkfont.Font(family='Helvetica', size=12, weight="bold", slant="italic")
        warning_font = tkfont.Font(family='Helvetica', size=8, weight="bold")
        updateEntriesField = 'firstName*', 'lastName*', 'Location*', 'Title*', 'Office Phone', 'Mobile Phone', 'Ext', 'eMail*'
        whoToUpdate = ['eMail*']
        entries = []
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Update Entry", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        who = tk.Label(self, text="Enter the information of the person you want to update", font= update_font)
        warning = tk.Label(self, text="Please Format all emails by capitalizing first and last initial\n E.g: Adam.Smith@structuretone.com", font= warning_font)
        who.pack()
        warning.pack()
        for entry in whoToUpdate:
            row = tk.Frame(self)
            lab = tk.Label(row, width=15, text=entry, anchor='w')
            ent = tk.Entry(row)
            row.pack(side="top", fill="x", padx=5, pady=5)
            lab.pack(side="left")
            ent.pack(side="right", expand="yes", fill="x")
            entries.append((lab, ent))

        what = tk.Label(self, text="Fill out fields you want to update", font= update_font, pady = 15)
        note = tk.Label(self, text="Please note fields that are already up to date need to be enterred as well \n or they will be deleted", font= warning_font, pady = 15)
        what.pack()
        note.pack()

        button1 = tk.Button(self, text="Go to Create entry",
                            command=lambda: controller.show_frame("CreateEntry"), pady= 10)
        for field in updateEntriesField:
            row = tk.Frame(self)
            lab = tk.Label(row, width=15, text=field, anchor='w')
            ent = tk.Entry(row)
            row.pack(side="top", fill="x", padx=5, pady=5)
            lab.pack(side="left")
            ent.pack(side="right", expand="yes", fill="x")
            entries.append((field, ent))
        
        self.bind('<Return>', (lambda event, e=entries: fetch_update(e)))
        update_button = tk.Button(self, pady=15, padx= 15,text='Update',
            command=(lambda e=entries: fetch_update(e)))

        update_button.pack()
        button1.pack()
        

def fetch_update(entries):
    values = []
    for entry in entries:
        field = entry[0]
        values.append(entry[1].get())
        entry[1].delete(0, tk.END)
    popupmsg(update_entry(values[0], firstNameValue= values[1], LastNameValue= values[2], locationValue= values[3], TitleValue= values[4], OfficeValue=values[5], MobileValue=values[6], ExtValue=values[7], eMailValue=values[8]))

    
if __name__ == "__main__":
    app = sqlEditor()
    app.mainloop()