class Geological_Place:
    def __init__(self):
        self.Temperature = 0
        self.Continent = 0


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

    def knowledge_check(self):
        return [self.Temperature, self.Continent]


    def print_knowledge_check(self):
        Data = self.knowledge_check()
        Temperature_Data = ["Cold", "Moderate", "Hot"]
        Continent_Data = ["Unknown", "Africa", "Asia", "Europe", "North America", "South America", "Antarctica", "Australia"]
        print()
        print("--- Gathered Information so far ---")
        print(f"Temperature: {Temperature_Data[Data[0]+1]}\nContinent: {Continent_Data[Data[1]]}")
        print("-----------------------------------")


if __name__ == "__main__":
    print("This program isn't meant to be run as the main program! Please use main.py!")