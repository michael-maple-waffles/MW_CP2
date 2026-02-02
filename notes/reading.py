

import csv

try:
    with open("notes/reading.txt", "r") as file:
        #everything tabbed over, the file is open
        content = []
        for line in file:
            content.append(line.strip())
except:
	print("cant find that file")
else:
    for line in content:
        print(f"hello {line}")


try:
    with open("notes\\Class CSV sample - Sheet1.csv", mode = "r") as sample:
        reader = csv.reader(sample)
        header = next(reader)
        users = []
        for line in reader:
            users.append(
                {
                header[0]: line[0],
                header[1]: line[1]
                }
            )
except:
    print("csv doesnt exist")
else:
    for user in users:
        print(user)
