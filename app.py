from tkinter import *
import api


class App:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("400x400")

        # ===== Widgets Declaration Area ===== #
        self.select_frame = Frame(self.root)
        self.select_frame.pack(fill=BOTH)

        self.display_frame = Frame(self.root)
        self.display_frame.pack(fill=BOTH)

        # ===== Variables Area ===== #
        self.value_inside = StringVar()

        # ===== API Area ===== #
        self.api = api
        self.my_api = api.MyApi()
        self.my_api.load_api()

    def main_window(self):
        """
        Main Window Of the App.
        :return: nothing.
        """
        # ===== First Frame Area =====#
        # Create Label.
        label1 = Label(self.select_frame, text="Select Options")
        label1.configure(width=10)
        label1.grid(row=0, column=0, ipadx=10)

        # Create Entry Combo box.
        select_list = self.my_api.get_local_authorities()

        self.value_inside.set("Select an Option")

        entry_combobox = OptionMenu(self.select_frame, self.value_inside, *select_list)
        entry_combobox.configure(width=23)
        entry_combobox.grid(row=0, column=1, pady=10)

        # Create Buttons.
        submit_button = Button(self.select_frame, text="Submit", command=self.show_air_quality)
        submit_button.grid(row=1, column=0, padx=5, pady=20, ipadx=10, sticky=W+E)
        submit_button.configure(width=20)

        clear_button = Button(self.select_frame, text="Clear", command=self.clear_all)
        clear_button.grid(row=1, column=1, padx=24, ipadx=10, sticky=W)
        clear_button.configure(width=20)

    def show_air_quality(self):
        self.clear_all()
        if self.value_inside.get() == "Select an Option":
            pass
        else:
            label2 = Label(self.display_frame, text=self.value_inside.get())
            label2.grid(row=0, column=0, columnspan=2)

    def clear_all(self):
        label3 = Label(self.display_frame, text="")
        label3.grid(row=0, column=0, columnspan=2, sticky=W+E)

    def run_window(self):
        self.root.mainloop()


MyApp = App()
MyApp.main_window()
MyApp.run_window()
