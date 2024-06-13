// Dedicated to God the Father
// All Rights Reserved Christopher Andrew Topalian Copyright 2000-2024
// https://github.com/ChristopherTopalian
// https://github.com/ChristopherAndrewTopalian

// HowToCombinePYFilesAllFolders.js

TUTORIAL:
How to Combine all .py files in all folders that are in our py folder.

Getting things ready:
We should add two new lines at the end every script. This way they will combine nicely with a line break in between each script.

Step One: Open our py folder

Step Two: Type in the address bar
of the py folder,
cmd,
press Enter

This opens our py folder in the command prompt

Step Three: Type the command shown below
in the command prompt and then
press Enter

for /r "%CD%" %i in (*.py) do type "%i" >> main.py

Now we have a newly created .py file
named main.py that has all of our py files
included into one file.

Now that all of our code is in one file
we can easily paste it into a book
to teach the world our code.

Happy Scripting :-)

