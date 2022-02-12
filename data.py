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

    def plotInfo(self, list):
        plot.plot(range(len(list)), list, label = station.name)

    def cleanInfo(self, infoName):
        newList = []
        for i in range(len(self.info[infoName])):
            if self.info[infoName][i] == "":
                forwardStep = 1
                while self.info[infoName][i + forwardStep] == "":
                    forwardStep += 1
                if i == 0:
                    info = self.info[infoName][i + forwardStep]
                elif i == len(self.info[infoName]) - 1:
                    info = newList[i - 1]
                else:
                    info = ((self.info[infoName][i + forwardStep] - info) / forwardStep + 1) + info
            else:
                info = self.info[infoName][i]
            newList.append(info)
        return newList

    def findMonth(self,month, list):
        newList = []
        g = 0
        for i in list:
            if int(self.months[g]) == int(month):
                newList.append(i)
            g += 1
        return newList

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

name = input('Hello! What is your name? ')
print(f'Hello {name}!')
while True:
    print(f'What weather data would you like to see? ')
    data = input('Max, Min, Humidity, WindMax, WindMin, Rain: ')
    time = input(f'For what time would you like to see that info (month #, year): ')

    for station in stations:
        dataList = station.cleanInfo(data)
        try:
            if int(time) in range(11):
                newDataList = station.findMonth(int(time) + 1, dataList)
                station.plotInfo(newDataList)
            else:
                station.plotInfo(dataList)
        except:
            station.plotInfo(dataList)
                
    plot.legend()
    plot.show()

    break
