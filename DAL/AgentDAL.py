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



person = Agent('Or', 'Haim', 'Home', 'Alive')
sql = MySQLServer()
dal = AgentDAL(sql)
dal.AddAgent(person)
