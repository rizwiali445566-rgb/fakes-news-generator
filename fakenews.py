# 1 import random model
import random
history_file = "hitory_file.txt"

# step 2 create founction and pass the argumet like subect action and place

def news_generated(Subects, Actions, Place_or_things):
    subject = random.choice(Subects)
    action = random.choice(Actions)
    place_things = random.choice(Place_or_things)
    return f"Breaking news: {subject} {action} {place_things}"

# this founction is used to save the data in history_file

def save_news_files(news):
    with open(history_file, 'a') as file:
        file.write(news + '\n')

def show_history():
    try:
        with open(history_file, 'r') as file:
            lines = file.readlines()
            if not lines:
                print("No history is founded: ")
            else:
                for line in lines:
                    print(line.strip())
                print("_____________")
    except FileNotFoundError:
        print("No file is founded:  ")

#  clear histtory

def clear_history ():
    with open(history_file, 'w') as file:
        pass
    print("History clear successfully: ")


# create list
Subjects = [
    "Ferrari",
    "Jago singh",
    "Nawzs ",
    "Rizwan",
]
Actions = [
    "Riding",
    "Happy mode",
    "corrupet",
    "gentle man",

]
Place_or_things = [
    "Motorway M25",
    "In  jungle",
    "in pakistan",
    "like a man",
]

while True:
     
     print("""
======== MANU =====

        1. Fake news
        2. Show history
        3. Clear history
        4. Exit
           
====================
           
             
           """)
     
     choice = input("Enter the choice (1 to 4):")

     if choice == '1':
         news = news_generated(Subjects, Actions, Place_or_things)
         print("\n", news)
         save_news_files(news)
     elif choice == '2':
         show_history()
     elif choice == '3':
         clear_history()
     elif choice == '4':
         print("Thanks for using the App ")
         break
     else:
         print("Invalid number please seelct the correct number: ")


