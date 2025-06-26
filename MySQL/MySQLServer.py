import mysql.connector

class MySQLServer:

    def __init__(self):
        self.Host = 'localhost'
        self.User = 'root'
        self.Password = ''
        self.DB = 'eagleeyedb'
        self.Connection = None

    def OpenConnection(self):
        if self.Connection is not None and not self.Connection.is_connected():
            return self.Connection
        else:
            try:
                self.Connection = mysql.connector.connect(host=self.Host, user=self.User, password=self.Password, database=self.DB)
                return self.Connection
            except Exception as ex:
                raise ex


    def CloseConnection(self):
        if self.Connection is not None and self.Connection.is_connected():
            self.Connection.close()