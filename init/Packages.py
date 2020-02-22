import csv
from data import MyHash
from model.Package import Package

# Big-O time complexity of O(n^2)
def build():
    with open('./data/package_data.txt', 'r') as file:
        reader = csv.reader(file)
        i = 1
        for row in reader:
            j = 1
            MyHash.insert(i, Package(row))
            # if we have more values include them in special notes
            for column in row:
                if j > 7:
                    try:
                        MyHash.get(i).package_special_notes = row[7] + row[j]
                    except IndexError:
                        pass
                j += 1
            i += 1
