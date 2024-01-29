from tkinter import *
import api


class App:
    def __init__(self):
        self.root = Tk()
        self.root.title("London Air Quality Monitoring")
        self.root.geometry("500x820")
        self.root.resizable(False, False)

        # ===== Widgets Declaration Area ===== #
        self.select_frame = Frame(self.root)
        self.select_frame.pack(fill=BOTH)

        self.display_frame = Frame(self.root)
        self.display_frame.pack(fill=BOTH)

        self.label2 = Label(self.display_frame)

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
        label1.configure(width=30)
        label1.grid(row=0, column=0, ipadx=10)

        # Create Entry Combo box.
        select_list = self.my_api.get_local_authorities()

        self.value_inside.set("Select an Option")

        entry_combobox = OptionMenu(self.select_frame, self.value_inside, *select_list)
        entry_combobox.configure(width=29)
        entry_combobox.grid(row=0, column=1, pady=10)

        # Create Buttons.
        submit_button = Button(self.select_frame, text="Submit", command=self.show_air_quality)
        submit_button.grid(row=1, column=0, padx=5, pady=20, ipadx=10, sticky=W+E)
        submit_button.configure(width=20)

        clear_button = Button(self.select_frame, text="Clear", command=self.clear_all)
        clear_button.grid(row=1, column=1, padx=24, ipadx=10, sticky=W)
        clear_button.configure(width=27)

    def show_air_quality(self):
        self.clear_all()

        if self.value_inside.get() == "Select an Option":
            pass
        else:
            api_values_list = self.my_api.get_air_quality_data(self.value_inside.get())

            for index, values in enumerate(api_values_list):
                if isinstance(values[1], dict):
                    my_label = Label(self.display_frame, text=f"""{values[0]}: \
{values[1]['@SpeciesDescription']} ({values[1]['@SpeciesCode']}) - \
{values[1]['@AirQualityIndex']} AQI {values[1]['@AirQualityBand']}.""", anchor=W)
                    my_label.pack(fill=BOTH, side=BOTTOM)
                else:
                    for value in values[1]:
                        my_label = Label(self.display_frame, text=f"""{values[0]}: \
{value['@SpeciesDescription']} ({value['@SpeciesCode']}) - \
{value['@AirQualityIndex']} AQI {value['@AirQualityBand']}.""", anchor=W)
                        my_label.pack(fill=BOTH, side=BOTTOM)

    def clear_all(self):
        for widgets in self.display_frame.winfo_children():
            widgets.destroy()

    def run_window(self):
        self.root.mainloop()


MyApp = App()
MyApp.main_window()
MyApp.run_window()
