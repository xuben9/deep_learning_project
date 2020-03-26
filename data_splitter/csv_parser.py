import os
import csv

csv_path = "csv_files/"
special_path = "special/"

train_w = open('train_file.csv', 'w', newline='')
test_w = open('test_file.csv', 'w', newline='')
test_file = csv.writer(test_w, delimiter=',')
train_file = csv.writer(train_w, delimiter=',')

test_rows = 0
for file in os.listdir(csv_path):
    skipped = 0
    with open(csv_path + file, newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            if not row[-1]:
                continue

            if test_rows < 1300:
                test_file.writerow([row[0], str(int(row[-1]) - 1)])
                test_rows += 1
            else:
                train_file.writerow([row[0], str(int(row[-1]) - 1)])


texts = []
labels = []

with open(special_path+'text.txt', 'r') as f:
    for line in f.readlines():
        texts.append(line.strip())

with open(special_path+'label.txt', 'r') as f:
    for line in f.readlines():
        labels.append(int(line.strip())-1)


for text, label in zip(texts, labels):
    train_file.writerow([text, label])


test_w.close()
train_w.close()
