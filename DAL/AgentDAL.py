from mysql.connector import connect

from MySQL.MySQLServer import MySQLServer
from Models.Agent import Agent

class AgentDAL:

    def __init__(self, mysqlserver:MySQLServer):
        self.sql = mysqlserver

    def AddAgent(self, agent:Agent):
        self.sql.OpenConnection()
        connection = self.sql.Connection
        cur = connection.cursor()
        cur.execute(f"""INSERT INTO agents (codeName, realName, location, status, missionsCompleted) VALUES ("{agent.CodeName}", "{agent.RealName}", "{agent.Location}", "{agent.Status}", "{agent.MissionComplete}")""")
        connection.commit()
        self.sql.CloseConnection()

    def GetAgentByCodeName(self, codeName:str):
        self.sql.OpenConnection()
        connection = self.sql.Connection
        cur = connection.cursor()
        cur.execute(f"""SELECT * FROM agents WHERE codeName = {f"{codeName}"}""")
        agent = cur.fetchall()

        if agent:
            return agent
        else:
            return None
        self.sql.CloseConnection()

    def RemoveAgent(self, agent:Agent):
        self.sql.OpenConnection()
        connection = self.sql.Connection
        cur = connection.cursor()
        cur.execute(f"""DELETE FROM agents WHERE codeName = {f"{agent.CodeName}"}""")
        connection.commit()
        self.sql.CloseConnection()

    def UpdateMissionsCompleted(self, agent:Agent):
        self.sql.OpenConnection()
        connection = self.sql.Connection
        cur = connection.cursor()
        cur.execute(f"""UPDATE agents SET missionsCompleted = {f"{agent.MissionComplete}"}""")
        connection.commit()
        self.sql.CloseConnection()
