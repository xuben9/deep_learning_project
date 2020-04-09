import os
import csv
import pandas as pd

csv_path = "csv_files/"
special_path = "special/"

train_w = open('train_file.csv', 'w', newline='')
test_w = open('test_file.csv', 'w', newline='')
test_file = csv.writer(test_w, delimiter=',')
train_file = csv.writer(train_w, delimiter=',')

test_rows = 0
test_sentences = []
train_sentences = []
test_labels = []
train_labels = []
for file in os.listdir(csv_path):
    skipped = 0
    with open(csv_path + file, newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        print(csvfile)
        for row in csv_reader:
            if not row[-1]:
                continue

            if test_rows < 1300:
                test_file.writerow([row[0].replace('\ufeff', ''), str(int(row[-1].replace('\ufeff', '')) - 1)])
                test_sentences.append(row[0].replace('\ufeff', ''))
                test_labels.append(row[-1].replace('\ufeff', ''))
                test_rows += 1
            else:
                train_file.writerow([row[0].replace('\ufeff', ''), str(int(row[-1].replace('\ufeff', '')) - 1)])
                train_sentences.append(row[0].replace('\ufeff', ''))
                train_labels.append(row[-1].replace('\ufeff', ''))

texts = []
test_labels = []

with open(special_path+'text.txt', 'r') as f:
    for line in f.readlines():
        texts.append(line.strip())

with open(special_path+'label.txt', 'r') as f:
    for line in f.readlines():
        test_labels.append(int(line.strip()) - 1)


for text, label in zip(texts, test_labels):
    train_file.writerow([text, label])


test_w.close()
train_w.close()
