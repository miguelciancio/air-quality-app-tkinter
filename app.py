from tkinter import *


class App:
    def __init__(self, root):
        self.root = root
        self.root = Tk()
        self.root.geometry("400x400")

    def main_window(self):
        # Create Frames.
        option_frame = Frame(self.root)
        option_frame.pack(fill=BOTH)

        # Create Labels.
        label1 = Label(option_frame, text="Select Options")
        label1.configure(width=10)
        label1.grid(row=0, column=0, ipadx=10, sticky=W)

        # Create Entry Combo boxes.
        options_list = [1, 2, 3, 4, 5, "Hello", "World"]

        value_inside = StringVar(self.root)
        value_inside.set("Select an Option")

        entry_combobox_1 = OptionMenu(option_frame, value_inside, *options_list)
        entry_combobox_1.configure(width=25)
        entry_combobox_1.grid(row=0, column=1, padx=20, pady=10, ipadx=20)

        # Create Buttons.


    def run_window(self):
        self.root.mainloop()


window = None
app = App(window)
app.main_window()
app.run_window()
