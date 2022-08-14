from __future__ import print_function
import csv
import string
import sys
from datetime import date
import msvcrt as m
def wait():
    m.getch()

parameter_names = ["pH","Ammonia","NO2","NO3","PO4","Alkalinity","Mg","Ca"]
parameter_dict={'Date': str(date.today().isoformat())}

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_null(s = string):
    if s.lower() =='n' or s.lower() == "null":
        return True
    else:
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
                sys.exit("This date has already been inserted.")
    for name in parameter_names:
        parameter = input("Please insert the " + name + "\n")
        while not is_number(parameter) and not is_null(parameter):
            wait()
            print("Not a valid entry!\n")
            parameter = input("Please insert the" + name + "\n")
        if is_null(parameter):
            parameter = "Null"
        parameter_dict[name] = (parameter)


def insert_data():
    with open('AquaManager.csv', 'a',encoding='utf8', newline='') as csvfile:
        fieldnames = ["Date","pH","NO2","NO3","PO4","Ammonia","Alkalinity","Ca","Mg"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(parameter_dict)
    check_entry_number


def anything_else():
    print("\nDone!\nAnything else?\n")
    start()


def check_entry_number():
    f = open("AquaManager.csv", 'r', encoding='utf8', errors='ignore')
    for i, line in enumerate(f.readlines()):
        total_lines = i
    if total_lines > 30:
        print("\nCongratulations! Your tank has reached one month of age! Maybe think of adding some corals to it!\n")
    elif total_lines > 100:
        print("\nYou have tested the water 100 times! Congrats!\n")
    return


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




print("\n \n \n AquaManager \n \n \n")
print("Today is " + date.today().isoformat())
start()