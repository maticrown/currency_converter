import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk


class CurrencyConverter():
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

        # self.geometry("500x200")
        #
        # # Adding a label
        # self.intro_label = Label(self, text="This is a currency converter", fg="blue", relief=tk.RAISED, borderwidth=3)
        # self.intro_label.config(font=("Courier", 15, "bold"))
        #
        # self.date_label = Label(self,
        #                        text=f"1 Israeli shekel equals = {self.currency_converter.convert('ILS', 'USD')} USD \n Date: {self.currency_converter.data['date']}",
        #                         relief=tk.GROOVE, borderwidhth=5)
        #
        # self.intro_label.place(x=10, y=5)
        # self.date_label.place(x=170, y=50)

        print(self.currencies)

    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        # convert to USD first since that is the base in the json file of the API
        if from_currency != "USD":
            amount = amount / self.currencies[from_currency]

        # limit prescision to 4 decimals
        amount = round(amount * self.currencies[to_currency], 4)
        return amount


# class CurrencyConverterUI():
#     def __init__(self, converter):
#         tk.Tk.__init__(self)
#         self.title = "currency converter"
#         self.currency_converter = converter


if __name__ == "__main__":
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    converter = CurrencyConverter(url)

    places = []

    with open("F://python_currency/currency.txt", "r+") as file:
        filecontents = file.readlines()
        for line in filecontents:
            current_place = line[:-1]
            print(current_place)
            places.append(current_place)
            #places = [current_place.rstrip() for current_place in file.readlines()]
            for i in range (len(places)):
                print(places[i])

    print(places[2])
    count = 0

    # for line in file.readlines():
    #     # print(line)
    #     count+=1
    #     lin = file.readline()
    #     print("{}".format(count, lin.strip()))
    #     # line=lines

    print("\nThe amount of 100 in ILS is:")

    print(converter.convert(places[0], places[1], int(places[2])))

    file.close()
