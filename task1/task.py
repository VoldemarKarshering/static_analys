import csv

def read(data):
    with open(data[0], newline='') as file:
        reader = csv.reader(file, delimiter=";")
        count = int(data[1]) - 1
        for st in reader:
            if(count):
                count -= 1
                continue
            print(st[int(data[2]) - 1])
            break


if __name__ == "__main__":
    data = input().split()
    read(data)