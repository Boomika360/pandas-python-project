import pandas

data = pandas.read_csv("census.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
print(grey_squirrels_count)
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(red_squirrels_count)
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(black_squirrels_count)

data_dict = {
    "squirrel_color": ["grey", "red", "black"],
    "squirrel_count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

dictionary = pandas.DataFrame(data_dict)
print(dictionary)
dictionary.to_csv("squirrel_color_count.txt")
