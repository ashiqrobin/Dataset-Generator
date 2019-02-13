import csv
import cv2
import os

path = 'folder'  # specify the path to image folder
files = os.listdir(path)

fileData = []

for f in files:
    img = cv2.imread(path + '\\' + str(f), 0)
    img = cv2.resize(img, (28, 28))
    rows, cols = img.shape
    pixels = []

    for i in range(rows):
        row = []
        for j in range(cols):
            k = 255 - img[i, j]
            row.append(k)
        pixels.append(row)
    fileData.append(pixels)

my_data = []
temp = []
my_file = open('dataset.csv', 'w',newline='')
with my_file:
    writer = csv.writer(my_file)
    for f in fileData:
        for i in range(28):
            for j in range(28):
                temp.append(f[i][j])
        my_data.append(temp)
        temp = []
    writer.writerows(my_data)

with open('dataset.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(row)