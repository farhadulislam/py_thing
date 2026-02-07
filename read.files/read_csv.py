import csv

with open("favourites.csv", "r") as file:
    #reader = csv.reader(file)
    reader = csv.DictReader(file)
    for row in reader:
        favourite = row['Language']
        print(favourite)
