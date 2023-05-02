import sqlite3


class UserRepository:
    """This class manages adding new users to database.

    Attributes:
        _connection: connection to sql database
    """
    def __init__(self, connection):
        self._connection = connection

    def create_user(self, username, password):
        """This function adds new username and password to database.

        Args:
            username: The username the user wants to register
            password: The password the user wants to use
        """
        new_user = (username, password)
        self._connection.row_factory = sqlite3.Row
        cursor = self._connection.cursor()
        cursor.execute("insert into users (username, password) values (?, ?);", new_user)
        self._connection.commit()

    def find_user(self, username, password):
        """This function checks if username and password is found in the database

        Args:
            username: The username the user wants to login with
            password: The password the user wants to login with

        Returns:
            username and password if found in database
        """
        #find = (username, password)
        cursor = self._connection.cursor()
        cursor.execute(f"SELECT username, password FROM users "
            f"WHERE username='{username}' AND password='{password}';")
        row = cursor.fetchone()
        #if row:
         #   print(row[0], row[1])
        #else:
         #   print("Käyttäjää ei löytynyt")
        return row




#test = UserRepository(get_database_connection())
#test.find_all()
#print(test.find_user("a", "b")[0], test.find_user("a", "b")[1])
#users = NewUser()

#users.user_info()

#users = OldUser()
#users.user_info()
