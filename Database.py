import datetime
from datetime import timedelta
import dateutil


class Geological_Place:
    def __init__(self):
        self.date = datetime.datetime.now()
        self.Temperature = 0
        self.Continent = 0
        self.desync_mode = False
        self.desync_way = None


    def ask_temp(self):
        while True:
            self.Temperature = input(
                "Are you Cold, Moderate or Hot (Assuming anything below 20°C is Cold, Moderate is 20°C ~ 25°C, Hot is 26°C+?\n")
            if self.Temperature == "Cold":
                self.Temperature = 1
                break
            elif self.Temperature == "Moderate":
                self.Temperature = 2
                break
            elif self.Temperature == "Hot":
                self.Temperature = 3
                break
            else:
                print("Please choose from Cold, Moderate or Hot. Just type them in lower case with the first letter capitalized and try again!")


    def ask_cont(self):
        while True:
            self.Continent = input(
                "Do you know which Continent you are in? (Africa, Asia, Europe, North America, South America, Antarctica, Australia). If not, just reply No.\n")
            if self.Continent == "No":
                self.Continent = 0
                break
            if self.Continent in ["Africa", "Asia", "Europe", "North America", "South America", "Antarctica", "Australia"]:
                if self.Continent == "Africa":
                    self.Continent = 1
                elif self.Continent == "Asia":
                    self.Continent = 2
                elif self.Continent == "Europe":
                    self.Continent = 3
                elif self.Continent == "North America":
                    self.Continent = 4
                elif self.Continent == "South America":
                    self.Continent = 5
                elif self.Continent == "Antarctica":
                    self.Continent = 6
                elif self.Continent == "Australia":
                    self.Continent = 7
                break
            print("Sorry, please choose from Africa, Asia, Europe, North America, South America, Antarctica, Australia. Capitalize the first letter and try again!")
            continue


    def sync_clock(self):
        self.date = datetime.datetime.now()
        while True:
            correctness = input(f"This is the last obtained date and time information: {datetime}\nIs this correct? (Yes/No)\n ")
            if correctness == "Yes":
                self.desync_mode = False
                break
            elif correctness == "No":
                time_knowledge = input("Do you know the current time? (Yes/No)\n")
                while True:
                    if time_knowledge == "Yes":
                        print("Please say how many years/days/hours/minutes/seconds/milliseconds is the current clock off?")
                        print("Also, please say it in the format years, days, hours, minutes, seconds, milliseconds (with \',\' in between")
                        print("E.g. 4,1,2,3,4,5")
                        desync = input()
                        time = list(map(int, desync.split(',')))
                        self.desync_mode = True
                        dateutil.relativedelta(years=time[0], days=time[1], hours=time[2], minutes=time[3], seconds=time[4], milliseconds=time[5])
                        while True:
                            forb = input("Is the system clock too early or late? (Early/Late)\n")
                            if forb == "early":
                                self.desync_way = 1
                                break
                            elif forb == "late":
                                self.desync_way = 0
                                break
                            else:
                                print("Sorry, please check your answer again.")
                    elif time_knowledge == "No":
                        print("Sorry, guess you need to work with the system's internal clock for now.")
                    else:
                        print("Sorry, please choose from one of the above.")


            else:
                print("Sorry, that answer doesn't seem valid. Please type Yes or No.")
                continue



    def knowledge_check(self):
        return [self.Temperature, self.Continent]


    def print_knowledge_check(self):
        Data = self.knowledge_check()
        Temperature_Data = ["Cold", "Moderate", "Hot"]
        Continent_Data = ["Unknown", "Africa", "Asia", "Europe", "North America", "South America", "Antarctica", "Australia"]
        print()
        print("--- Gathered Information so far ---")
        print(f"Temperature: {Temperature_Data[Data[0]-1]}\nContinent: {Continent_Data[Data[1]]}")
        print("-----------------------------------")


if __name__ == "__main__":
    print("This program isn't meant to be run as the main program! Please use main.py!")