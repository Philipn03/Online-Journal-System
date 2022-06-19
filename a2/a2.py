# Philip Nguyen 
# philipbn@uci.edu
# 57277528

from pathlib import Path
from Profile import Profile
from Profile import Post
import ui

ui.intro()
x = input()

path = Path()
profile = Profile()
post = Post()

# If the user enters admin in the beginning, interface is disabled
# Else if 'admin is not entered, the else statement runs on line 213'
if x == 'admin':

    print('Welcome to ADMIN Mode')
    x = input()
    command = x[:1]

    # If user inputs Q, make sure program quits 
    if command == 'Q':
        quit()

    # If command is not Q, continuing looping through while loop   
    while command != 'Q':
        
        # The user cannot just put in a single letter command. 
        # User has to put in an input in the input format
        while len(x) <= 1 and command != 'Q':
            print('ERROR')
            x = input()
            command = x[:1]

        while command != 'C' and command != 'O' and command != 'E' and command != 'P' and command != 'Q':
            print('ERROR')
            x = input()
            command = x[:1]

            
        # Command C creates a new file with extension .dsu. There is a try and except statement so if the user creates a file when the file exist already, it would just load instead
        # If loading the file creates an error because the file is nonexistent, we will create the path instead and save it to Profile object
        if command == 'C':
            index = -1
            for i in reversed(range(len(x)-3)):
                if x[i:i+4] == ' -n ':
                    index = i
                    break
            p = x[2:index]
            file_name_dsu = x[index+4:] + '.dsu'
            p2 = Path('.') / p
            path = Path('.') / p / file_name_dsu 
            try:
                profile.load_profile(path)
                print('File Already Exist and Loaded')
            except:
                if not p2.exists():
                    print('ERROR...Path must be VALID\n')
                else:
                    path.touch()
                    profile.save_profile(path)
                    print('Profile Created')
                
            x = input()
            command = x[:1]

        # If command is O, we will store the file into variable 'path' and load it
        # If loading file does not work, that means file DNE. Prints an error message and makes user try again
        elif command == 'O':
            path = Path() / x[2:]
            try:
                profile.load_profile(path)
                ui.o_info(path)
            except:
                print('ERROR...Try Again')
                
            x = input()
            command = x[:1]

        # If command is E, user wants to edit
        elif command == 'E':
            usr = ''
            pwd = ''
            bio = ''
            addpost = ''
            delpost = -1
            start = -1
            end = -1

            # Checks to see if input contains any of the valid options below (-user, -pwd, -bio, etc..)
            # If input does not contain any of the options then another input is prompted for user
            if ('-usr' in x) or ('-pwd' in x) or ('-bio' in x) or ('-addpost' in x) or ('-delpost' in x):

                for i in range(len(x)):

                    if x[i:i+5] == '-usr ':

                        # Found the index of the '-' in user
                        start = i+5

                        # Checks to find the second quotation mark. When found, I would store the index of the quotation mark to the 'end' variable
                        # I then would extract the actually username by slicng the input from start+1 (after first ") to the end (excluding second ")
                        # I assigned the profile attribute 'username' to usr
                        for j in range(start+1, len(x)):
                            if x[j] == '"':
                                end = j
                                break
                        usr = x[start+1:end]
                        profile.username = usr
                    
                    # Same function as '-usr'
                    if x[i:i+5] == '-pwd ':
                        start = i+5
                        for j in range(start+1, len(x)):
                            if x[j] == '"':
                                end = j
                                break
                        pwd = x[start+1:end]
                        profile.password = pwd

                    # Same function as '-usr'
                    if x[i:i+5] == '-bio ':
                        start = i+5
                        for j in range(start+1, len(x)):
                            if x[j] == '"':
                                end = j
                                break
                        bio = x[start+1:end]
                        profile.bio = bio

                    # Same function as '-usr' but since '-addpost' has more letters, I assigned start to i+9 (after first ")
                    if x[i:i+9] == '-addpost ':
                        start = i+9
                        for j in range(start+1, len(x)):
                            if x[j] == '"':
                                end = j
                                break
                        addpost = x[start+1:end]

                        # Created a Post Object used to add to Profile Post List
                        # Assigned Post Entry to the addpost variable which was extracted from the input using index slicing
                        post = Post()
                        post.entry = addpost
                        profile.add_post(post)

                    if x[i:i+9] == '-delpost ':

                        # Try/Except used because if the index that the user wants to delete is not an int, there would be an error
                        try:
                            start = i+9
                            delpost = int(x[start:])
                            if not profile.del_post(delpost):
                                print('Not valid')
                        except:
                            print('ERROR')
                
                # After all the edits are done, the profile should be saved
                # If user inputs an E command FIRST and has not created or loaded a file, the except statement would execute and print an error message. User needs to create or load file first
                try:
                    profile.save_profile(path)
                except:
                    print('ERROR')
                        

            x = input()
            command = x[:1]

        # If command is P, I would find what the user wants to print and print it out using profile.
        elif command == 'P':
            for i in range(len(x)):

                if x[i:i+5] == ' -usr':
                    print('Username: ' + profile.username)

                if x[i:i+5] == ' -pwd':
                    print('Password: ' + profile.password)

                if x[i:i+5] == ' -bio':
                    print('Bio: ' + profile.bio)

                if x[i:i+7] == ' -posts':

                    # I called the print_entry functin located in the ui module
                    # Uses a for loop to print out all entries and their id
                    ui.print_entry(profile)
                    print()
                  
                if x[i:i+7] == ' -post ':
                    try:
                        index = int(x.index('-post') + 6)
                        lst_index = int(x[index:])
                        print('\nSINGLE POST')
                        print('ID', lst_index, ':', profile._posts[lst_index]['entry'])
                    
                    except:
                        print('ERROR')

                # Call print_all function in ui module     
                if x[i:i+4] == '-all':
                    ui.print_all(profile)
                
            x = input()
            command = x[:1]

        elif command == 'Q':
            quit()

#If admin is NOT entered, the code below will execute (User friendly)
else:
    command = x[:1]

    if command == 'Q':
        quit()

    while command != 'Q':

        while len(x) > 1:
            print('ERROR')
            x = input()
            command = x[:1]

        # If user enters a letter not listed below, an error message will print and another input is asked for
        while command != 'C' and command != 'O' and command != 'E' and command != 'A' and command != 'D' and command != 'P' and command != 'Q':
            print('ERROR')
            x = input()
            command = x[:1]

        # Sort of the same thing as the admin 'C' but this time the directory and profile name is asked for
        # Creates new file with DSU extension 
        if command == 'C':
            directory = input(ui.STORE_PRO)
            profile_name = input(ui.STORE_PRO_NAME)
            p = directory
            p2 = Path('.') / p
            file_name_dsu = profile_name + '.dsu'
            path = Path('.') / p / file_name_dsu
            try:
                profile.load_profile(path)
                print('File Already Exist and Loaded\n')
                
            except:

                # If user enters a directory that DNE, an error message will be printed
                # Else if directory exist, the new file will be created and stored in directory
                # Creating the file also asks for username, password, and bio (ui.c_info())
                # Make sure to save all info
                if not p2.exists():
                    print()
                    print('ERROR...Path must be VALID\n')
                else:
                    path.touch()
                    ui.c_info(profile)
                    profile.save_profile(path)
                    print('Profile Created\n\n')
            
        # Asks for a DSU file to load
        # Loads file if it exist, else except statement is executed
        elif command == 'O':
            file = input(ui.DSU_FILE)
            path = Path('.') / file
            try:
                profile.load_profile(path)
                ui.o_info(path)
            except:
                print('ERROR...Try Again\n')

        # Asks for username, password, and bio all separately
        # If any input is skipped (press Enter), then user does not want to change the info
        elif command == 'E':
            print('Enter New Profile Information (leave blank to skip)\n')
            username1 = input("Enter username:\n")
            if username1 == '':
                pass
            else:
                profile.username = username1

            password1 = input("Enter password:\n")
            if password1 == '':
                pass
            else:
                profile.password = password1

            bio1 = input("Place bio (or press ENTER to skip):\n")
            if bio1 == '':
                pass
            else:
                profile.bio = bio1
            
            # If saving profile errors, that is because the user has not created or loaded a file
            try:
                profile.save_profile(path)
            except:
                print(ui.ERR_MSG)

        # Ask for adding an entry
        
        elif command == 'A':
            addpost = input('Enter Entry (no quotations needed):\n')
            post = Post()
            post.entry = addpost

            # If adding post causes an error, that is because the user has not created or loaded a file
            try:
                profile.add_post(post)
                profile.save_profile(path)
            except:
                print(ui.ERR_MSG)

        # Ask user to delete a post
        # A try/except is invovled because if user enters an non-int input, then error occurs
        # If statement checks if the index that user entered is valid
        # If index not valid, error message is printed out, else valid index will delete correct post
        elif command == 'D':
            try:
                delpost = int(input('Enter Entry ID to DELETE:\n'))
                if not profile.del_post(delpost):
                    print('Not valid')
                else:
                    print('Successfully DELETED')
                profile.save_profile(path)
            except:
                print('ERROR\n')

        # If user enters P, another input is prompted for printing options
        # If user enters nonvalid option, input is constantly prompted until right option is entered
        elif command == 'P':
            try:
                ui.print_opt()
                prt = input()
                while prt != 'usr' and prt != 'pwd' and prt != 'bio' and prt != 'posts' and prt != 'post' and prt != 'all':
                    print('ERROR. Try Again')
                    prt = input()
                if prt == 'usr':
                    print()
                    print('Username: ' + profile.username)
                    print()
                if prt == 'pwd':
                    print()
                    print('Password: ' + profile.password)
                    print()
                if prt == 'bio':
                    print()
                    print('Bio: ' + profile.bio)
                    print()
                if prt == 'posts':
                    ui.print_entry(profile)
                    print()
                if prt == 'post':
                    try:
                        id = int(input('What ID would you like to look at?\n'))
                        print('\nSINGLE POST')
                        print('ID', id, ':', profile._posts[id]['entry'])
                        print()
                    except:
                        print('ERROR\n')
                if prt == 'all':
                    ui.print_all(profile)
            except:
                print(ui.ERR_MSG)
        
        # At any time user enters Q, code stops running
        elif command == 'Q':
            quit()
        
        # Option menu is printed every single time after an option is executed
        ui.action()
        x = input()
        command = x[:1]

