from tkinter import *

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)
        
        main_menu = Menu(self.master)
        self.master.config(menu=main_menu)
        
        file = Menu(main_menu)
        file.add_command(label="Exit", command=self.client_exit)
        main_menu.add_cascade(label="File", menu=file)

        edit = Menu(main_menu)
        edit.add_command(label="Undo")
        edit.add_command(label="Redo")
        main_menu.add_cascade(label="Edit", menu=edit)



    def client_exit(self):
        exit()

root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()