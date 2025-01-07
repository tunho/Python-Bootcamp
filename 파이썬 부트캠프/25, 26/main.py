import pandas as pd

dataset = pd.read_csv('weather_data.csv')
print(type(dataset))
print(dataset["temp"])
data_dict = dataset.to_dict()
print(data_dict)
data_list = dataset['temp'].to_list()
print(data_list)
print(sum(data_list)/len(data_list))
print(dataset['temp'].mean())
print(dataset['temp'].max())
print(dataset.condition)
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv 
# with open("weather_data.csv") as data_file: 
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp" : 
#          temperatures.append(row[1])

# get data in row 

# print(dataset[dataset.day == "Monday"])
# print(dataset[dataset['temp'] == dataset['temp'].max()])

monday = dataset[dataset.day == "Monday"]
print(monday.condition)
print(int(monday.temp*1.8+32))

# 데이터프레임 만들기

data_dict = {
    "students": ["amy", "james", "angela"],
    "score": [76, 56, 65]
}
data = pd.DataFrame(data_dict)

data.to_csv("new_data.csv")



import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250104.csv")

color_count = data["Primary Fur Color"].value_counts()

print(color_count)

gray_sq = len(data[data["Primary Fur Color"] == "Gray"])
print(gray_sq)

color_count.to_csv("color_count.csv")