# SQL_Editor
Edit any SQL Database using this simplified program

# Setup
In order to install you need to have python 3.6 installed.\
Once downloaded go to your console and do: \
Pip install pyinstaller

open sql_create_and_update.py and configure the config where it says user, password, host and database\
based on your needs

then navigate to where setup.py is and do "python setup.py build" \
then navigate to your build directory and double click on sql_editor.exe

# License
This code is licensed with GNU Public v3 License

# Changelog
V 2.0
----------
Changed Update entry to only require email address of the entry\
Fixed bug where people with the same last name wouldn't be added\
Added Error handling\
Made email field required in order to update/create entry


V 1.0
-----------
Added Create new entry\
Added Update Entry\
Fixed problem where update entry didnt work when there was no email enterred
