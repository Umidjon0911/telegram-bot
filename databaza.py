import sqlite3

# # Create table
# try:
#     sqliteConnection = sqlite3.connect('DOKONCHI.db')
#     sqlite_create_table_query = '''CREATE TABLE BUYURTMALAR (
#                                 ID INTEGER NOT NULL,
#                                 MAXSULOT TEXT NOT NULL,
#                                 SONI TEXT NOT NULL,
#                                 SUMMASI TEXT NOT NULL);'''

#     cursor = sqliteConnection.cursor()
#     print("Successfully Connected to SQLite")
#     cursor.execute(sqlite_create_table_query)
#     sqliteConnection.commit()
#     print("SQLite table created")

#     cursor.close()

# except sqlite3.Error as error:
#     print("Error while creating a sqlite table", error)
# finally:
#     if sqliteConnection:
#         sqliteConnection.close()
#         print("sqlite connection is closed")

# Insert data
def Qoshish(telegram_id, maxsulot, soni, summasi):
    try:
        sqliteConnection = sqlite3.connect('DOKONCHI.db')
        sqlite_insert_query = '''INSERT INTO BUYURTMALAR (ID, MAXSULOT, SONI, SUMMASI) VALUES(?,?,?,?)'''

        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        cursor.execute(sqlite_insert_query, (telegram_id, maxsulot, soni, summasi))
        sqliteConnection.commit()
        print("Record inserted successfully")

        cursor.close()

    except sqlite3.Error as error:
        print("Error while inserting data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")

# Qoshish(514151, "salom", "5", "515")

# # Read data
def oqish():
    try:
        sqliteConnection = sqlite3.connect('DOKONCHI.db', timeout=20)
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT * FROM BUYURTMALAR"""
        cursor.execute(sqlite_select_query)
        buyurtmalar = cursor.fetchall()
        cursor.close()
        return buyurtmalar

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

# # Delete data
# def ochir(id):
#     try:
#         sqliteConnection = sqlite3.connect('DOKONCHI.db')
#         cursor = sqliteConnection.cursor()
#         print("Connected to SQLite")

#         sql_delete_query = """DELETE FROM BUYURTMALAR WHERE ID = ?"""
#         cursor.execute(sql_delete_query, (id,))
#         sqliteConnection.commit()
#         print("Record deleted successfully")
#         cursor.close()

#     except sqlite3.Error as error:
#         print("Failed to delete record from sqlite table", error)
#     finally:
#         if sqliteConnection:
#             sqliteConnection.close()
#             print("The SQLite connection is closed")

