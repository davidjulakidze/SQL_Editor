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
    'user': '',
    'password': '',
    'host': '',
    'database': '',
})



def make_new_entry(LastName, FirstName, STI_location, Title, Office_Phone="", Mobile_Phone="", Ext="", eMail="", table = "test_directory", cursor = database.cursor()):

    add_employee = ("""INSERT INTO %s (LastName,FirstName,STI_Location,Title,Office_Phone,Mobile_Phone,Ext,eMail) 
                    VALUES ("%s","%s","%s","%s","%s","%s","%s","%s")
                    """% (table, LastName, FirstName, STI_location, Title, Office_Phone, Mobile_Phone, Ext, eMail))
    cursor.execute(add_employee)
    database.commit()
    return True

def close_cursor(cursor):
    return cursor.close()

def close_database(cursor = database.cursor()):
    close_cursor(cursor)
    return database.close()

def update_entry(LastName, FirstName, CurrenteMail, table = "test_directory", 
                STI_location = "STI_location", locationValue = "",
                Title = "Title", TitleValue = "",
                Office_Phone = "Office_Phone", OfficeValue = "",
                Mobile_Phone = "Mobile_Phone", MobileValue = "",
                Ext = "Ext", ExtValue = "",
                eMail = "eMail", eMailValue = "",cursor = database.cursor()):
    update_employee = ("""UPDATE %s 
                          SET %s = "%s", %s = "%s", %s = "%s", %s = "%s", %s = "%s", %s = "%s" 
                          WHERE LastName = "%s" AND FirstName = "%s" AND eMail = "%s" """ % (table, 
                          STI_location, locationValue,
                          Title, TitleValue,
                          Office_Phone, OfficeValue,
                          Mobile_Phone, MobileValue,
                          Ext, ExtValue,
                          eMail, eMailValue,
                          LastName, FirstName, CurrenteMail))
    cursor.execute(update_employee)
    database.commit()
    return True


