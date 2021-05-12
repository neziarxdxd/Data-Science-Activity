import csv
import random
listOfWorks = ["Quality Assurance", "Software developer",
               "Quality Engineer", "Test engineer", "UI/UX design",
               "Java Developer", "Python Developer",
               "Frontend Developer", "Database Manager"
               ]
with open('dataset.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Gender", "Age", "Work", "College"])
    for i in range(100):
        gender = random.randint(0, 1)
        age = random.randint(18, 25)
        work = random.choice(listOfWorks)
        isCollege = random.randint(0, 1)
        writer.writerow([gender, age, work, isCollege])
    # end of the file
