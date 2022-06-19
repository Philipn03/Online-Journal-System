# Philip Nguyen
# philipbn@uci.edu
# 57277528
from Profile import Profile

STORE_PRO = 'Where would you like to store your profile (enter a valid path)?\n'
STORE_PRO_NAME = 'What would you like your Profile Name to be?\n'
DSU_FILE = 'Enter DSU File you would like to open:\n'
ERR_MSG = 'ERROR...Must CREATE or OPEN Profile\n'

def intro():
    print('Welcome to ICS 32 Journal \n\nType Q anytime you want to exit the program\n')
    print('How would you like to get started\n')
    print('  C. Create New Profile \n  O. Open Existing File\n')

def action():
    print('What would you like to do next?')
    print('C. Create New Profile \nO. Open Existing Profile \nE. Edit Existing Profile \nA. Add Entry \nD. Delete Entry \nP. Print \nQ. Quit ')

def print_opt():
    print('What would you like to print\n\nusr : Username \npwd : Password \nbio : Bio \nposts : All posts \npost : One post [id] \nall : All\n')

def print_entry(pro:Profile):
    print('\nPOST ID : POST')
    print('--------------')
    x = 0
    for i in pro.get_posts():
        print(f"{x} : {i.get_entry()}")
        x += 1

def print_ent(pro:Profile):
    print(pro.get_posts())

def o_info(path):
    print()
    print('Successfully loaded:', path)
    print()

def c_info(pro:Profile):
    print('Enter New Profile Information (leave blank to skip)\n')
    username1 = input("Enter username:\n")
    password1 = input("Enter password:\n")
    bio1 = input("Place bio (or press ENTER to skip):\n")

    pro.dsuserver = 'localhost'
    pro.username = username1
    pro.password = password1
    pro.bio = bio1

def print_all(pro:Profile):
    print()
    print('Username: ' + pro.username)
    print('Password: ' + pro.password)
    print('Bio: ' + pro.bio)
    print_entry(pro)
    print()
