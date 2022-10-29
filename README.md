# Journal

Fully functional command line program that allows you to find, create, read, and delete files on your computer.

Example Starting Program

// Create a new journal called 'myjournal' (could also use O for existing file)
C c:\users\philip -n myjournal

// Add a username and password to 'myjournal'
E -usr "philip n" -pwd "password123"

// Add a bio to 'myjournal'
E -bio "Hi my name is Philip, this is my bio."

// Add a post to 'myjournal'
E -addpost "Hello, this is my first post!"

// Print the contents of 'myjournal'
P -all

// Print all posts stored in 'myjournal'
P -posts

// Print single post by id stored in 'myjournal'
P -post 1

// Delete a post in 'myjournal' by id
E -delpost 1
