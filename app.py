from tkinter import *


class App:
    def __init__(self, root):
        self.root = root
        self.root = Tk()
        self.root.geometry("400x400")

    def main_window(self):
        """
        Main Window Of the App.
        :return: nothing.
        """
        # ===== First Frame Area =====#
        # Create Frame.
        select_frame = Frame(self.root)
        select_frame.pack(fill=BOTH)

        # Create Label.
        label1 = Label(select_frame, text="Select Options")
        label1.configure(width=10)
        label1.grid(row=0, column=0, ipadx=10)

        # Create Entry Combo box.
        options_list = [1, 2, 3, 4, 5, "Hello", "World"]

        value_inside = StringVar(self.root)
        value_inside.set("Select an Option")

        entry_combobox_1 = OptionMenu(select_frame, value_inside, *options_list)
        entry_combobox_1.configure(width=21)
        entry_combobox_1.grid(row=0, column=1, pady=10)

        # Create Buttons.
        submit_button = Button(select_frame, text="Submit")
        submit_button.grid(row=1, column=0, padx=5, pady=20, ipadx=10, sticky=W+E)
        submit_button.configure(width=20)

        clear_button = Button(select_frame, text="Clear")
        clear_button.grid(row=1, column=1, padx=24, ipadx=10, sticky=W)
        clear_button.configure(width=20)

        # ===== Second Frame Area =====#
        display_frame = Frame(self.root)
        display_frame.pack(fill=BOTH)


    def run_window(self):
        self.root.mainloop()


window = None
app = App(window)
app.main_window()
app.run_window()
