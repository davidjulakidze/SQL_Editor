import mysql.connector
from mysql.connector import errorcode

### AUTHOR: Davit Julakidze
### License: GNU PUBLIC V3
### 07/02/2018





def connect_to_database(config):
    try:
        database = mysql.connector.connect(**config)
        return database
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        database.close()


## FILL OUT BELOW

database = connect_to_database(config = {
    'user': 'root',
    'password': '',
    'host': '',
    'database': '',
})



def make_new_entry(LastName, FirstName, 
                    STI_location, Title, Office_Phone="", 
                    Mobile_Phone="", Ext="", eMail="", 
                    table = "test_directory", cursor = database.cursor()):

    try:
        if(LastName == "" or FirstName == "" or STI_location == "" or Title == ""):
            return "Error: Please complete all fields marked with * "
        elif(eMail == ""):
            return "Error: Invalid email"
        else:
            add_employee = ("""INSERT INTO %s (LastName,FirstName,STI_Location,Title,Office_Phone,Mobile_Phone,Ext,eMail) 
                        VALUES ("%s","%s","%s","%s","%s","%s","%s","%s")
                        """% (table, FirstName, LastName, STI_location, Title, Office_Phone, Mobile_Phone, Ext, eMail))
            cursor.execute(add_employee)
            database.commit()
            return "Created!"
    except:
        return "Error: Potential Duplicate"

def close_cursor(cursor):
    return cursor.close()

def close_database(cursor = database.cursor()):
    close_cursor(cursor)
    return database.close()

def update_entry(CurrenteMail, table = "test_directory", 
                STI_location = "STI_location", locationValue = "",
                Title = "Title", TitleValue = "",
                Office_Phone = "Office_Phone", OfficeValue = "",
                Mobile_Phone = "Mobile_Phone", MobileValue = "",
                Ext = "Ext", ExtValue = "",
                eMail = "eMail", eMailValue = "",
                firstName = "FirstName", firstNameValue= "",
                lastName = "LastName", LastNameValue = "", cursor = database.cursor()):
    try:
        if(eMailValue == ""):
            return "Error: Invalid Email"
        elif(firstNameValue == "" or LastNameValue == "" or locationValue == "" or TitleValue == ""):
            return "Error: Please complete all fields marked with * "
        else:
            update_employee = ("""UPDATE %s 
                            SET %s = "%s", %s = "%s", %s = "%s", %s = "%s", %s = "%s", %s = "%s" , %s = "%s", %s = "%s"
                            WHERE eMail = "%s" """ % (table,
                            firstName, firstNameValue,
                            lastName, LastNameValue,
                            STI_location, locationValue,
                            Title, TitleValue,
                            Office_Phone, OfficeValue,
                            Mobile_Phone, MobileValue,
                            Ext, ExtValue,
                            eMail, eMailValue,
                            CurrenteMail))
            cursor.execute(update_employee)
            database.commit()
            return "Updated!"
    except:
        return "Unknown Error"
