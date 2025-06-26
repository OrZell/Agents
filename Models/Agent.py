class Agent:

    def __init__(self, codeName, realName, location, status, missionComplete=0):
        self.CodeName = codeName
        self.RealName = realName
        self.Location = location
        self.Status = status
        self.MissionComplete = missionComplete

    @property
    def IncreaseMissionComplete(self):
        self.MissionComplete += 1