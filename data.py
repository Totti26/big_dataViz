import csv
import matplotlib.pyplot as plot

stations = []

class stationInfo():
    def __init__(self, name):
        self.name = name
        self.averageMax, self.averageMin, self.maxTemp, self.minTemp = 0, 0, 0, 0
        self.info = {
            "Max" : [],
            "Min" : [],
            "Humidity" : [],
            "WindMax" : [],
            "WindMin" : [],
            "Rain" : [],
        }
        self.months = []

    def firstData(self, value, limits):
        if value > limits[1] or value < limits[0]:
            return False
        else:
            return True

    def addData(self, infoName, data, limits):
        if self.firstData(data, limits):
            self.info[infoName].append(data)
        else:
            self.info[infoName].append("")

    def calcMax(self, infoName):
        Max = 0 
        for data in self.info[infoName]:
            if data != "":
                if Max == 0 or data > Max:
                    Max = data
        return Max
    
    def calcMin(self, infoName):
        Min = 0
        for data in self.info[infoName]:
            if data != "":
                if Min == 0 or data < Min:
                    Min = data
        return Min

    def printInfo(self):
        print(f"The highest temp for {self.name} station was {round(self.maxTemp, 2)}. ")
        print(f"The lowest temp for {self.name} station was {round(self.maxTemp, 2)}. ")
        print(f"The average highest temp for {self.name} station was {round(self.averageMax, 2)}. ")
        print(f"The average lowest temp for {self.name} station was {round(self.averageMin, 2)}. ")
        print("")

with open('2016VizData.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        max = float(row["TMAX"])
        min = float(row["TMIN"])
        humidity = float(row["HAVG"])
        windMax = float(row["WSMX"])
        windMin = float(row["WSMN"])
        rain = float(row["RAIN"])

        currentStation = row["STID"]
        i = 0
        if len(stations) == 0:
            stations.append(stationInfo(currentStation))
        for station in stations:
            i += 1
            if station.name == currentStation:
                break
            else:
                if i >= len(stations):
                    stations.append(stationInfo(currentStation))
        for station in stations:
            if station.name == currentStation:
                station.addData("Max", max, (-80, 120))
                station.addData("Min", min, (-80, 120))
                station.addData("Humidity", humidity, (-80, 120))
                station.addData("WindMax", windMax, (-80, 120))
                station.addData("WindMin", windMin, (-80, 120))
                station.addData("Rain", rain, (-80, 120))
                station.months.append(row["MONTH"])
                
