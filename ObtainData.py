import mariadb
import queryStorage as qs
from mariadb import Error, Cursor, Connection
import Luis_Code as lc

#Function that will retrieve the info from maria db
def data():

    #Configurations for the Maria db server
    DB_CONFIG = {
        'host': 'localhost',
        'user': 'coen2220',
        'password': 'coen2220',
        'database': 'proyect_database',
        'port': 3306,
    }
    connection: Connection = None
    try:
        #Connect to Maria db
        connection = mariadb.connect(**DB_CONFIG)

        # Create cursor, we can extract the information as dictionaries
        cursor: Cursor = connection.cursor(dictionary=True)

        #Send that cursor to two separate functions
        qs.infoObtain(cursor)
        lc.infoObtain(cursor)

    except Error as e:
        print(f"MariaDB Error: {e}")

    finally:
         if connection:
             connection.close()