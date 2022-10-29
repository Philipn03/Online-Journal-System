# Journal

Fully functional command line program that allows you to find, create, read, and delete files on your computer.

Example Starting Program

# create a new journal called 'myjournal' (could also use O for existing file)
C c:\users\philip -n myjournal

# add a username and password to 'myjournal'
E -usr "philip n" -pwd "password123"

# add a bio to 'myjournal'
E -bio "Hi my name is Philip, this is my bio."

# add a post to 'myjournal'
E -addpost "Hello, this is my first post!"

# print the contents of 'myjournal'
P -all

# print all posts stored in 'myjournal'
P -posts

# print single post by id stored in 'myjournal'
P -post 1

# delete a post in 'myjournal' by id
E -delpost 1
