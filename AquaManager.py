import csv
from datetime import date
import msvcrt as m
def wait():
    m.getch()

parameter_names = ["pH","Ammonia","NO2","NO3","Alkhalinity","Mg","Ca"]
parameter_dict={'Date': str(date.today().isoformat())}

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def welcome():
    a=input("\n1.Insert Parameters\n2.View Graphs\n3.Bye bye!\n")
    if is_number(a):
            return int(a)   
    else:
        print("Invalid input")
        wait()
        return welcome()

def insert_parameter():
    with open('AquaManager.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["Date"] == str(date.today().isoformat()):
                print("This date has already been inserted")
                wait()
                return
    for name in parameter_names:
        parameter = input("Please insert the " + name + "\n")
        while not is_number(parameter):
            wait()
            print("Not a number\n")
            parameter = input("Please insert the" + name + "\n")
        parameter_dict[name] = (parameter)


def insert_data():
    with open('AquaManager.csv', 'w',encoding='utf8', newline='') as csvfile:
        fieldnames = ["Date","pH","NO2","NO3","Ammonia","Alkhalinity","Ca","Mg"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
    with open('AquaManager.csv', 'a',encoding='utf8', newline='') as csvfile:
        fieldnames = ["Date","pH","NO2","NO3","Ammonia","Alkhalinity","Ca","Mg"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(parameter_dict)

        
def anything_else():
    a=input("\nDone!\nAnything else?\n")
    start()

def start():
    a = welcome()
    if a == 1:
        insert_parameter()
        insert_data()
        anything_else()
        return
    elif a == 2:
        print("This function isn't ready yet")
        return
    elif a == 3:
        print("\nBuh-Bye!\n")
        return

print(date.today().isoformat())
print("\n \n \n AquaManager \n \n \n")
start()