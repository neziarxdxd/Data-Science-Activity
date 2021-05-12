import csv
import random

with open('innovators.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    for i in range(100):
        gender = random.randint(0, 1)
        age = random.randint(18, 25)
        writer.writerow([gender, age])
    # end of the file
