import csv
with open("D:/python/sjcet.csv",newline="") as csvfile:
  data=csv.reader(csvfile,delimiter=" ",quotechar="|")
  for row in data:
    print(",".join(row))