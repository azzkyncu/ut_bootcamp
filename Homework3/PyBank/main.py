import os
import csv

path = os.path.join("PyBank", "budget_data.csv")

# print(path)

total = 0
num_months = 0
net_change_values = []

with open(path) as f:
    reader =  csv.reader(f)
    # print(reader)
    next(reader)
    next_row = next(reader)
    prev = int(next_row[1])

    # print(prev)

    for row in reader:
        # print(row[1])
        total = total + int(row[1])
        num_months = num_months + 1

        net_change = int(row[1]) - prev
        prev = int(next_row[1])
        net_change_values = net_change_values + [net_change]


print(total)
print(num_months)
print(net_change_values)