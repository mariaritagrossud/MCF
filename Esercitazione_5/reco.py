#Definisco classe Hit
class Hit():

    def __init__(self, idm, ids, time):
        self.idm  = idm
        self.ids  = ids
        self.time = time
    
    #Ordinare oggetti
    def __lt__(self, other):
        if self.time == other.time:

            if self.idm == other.idm:
                return self.ids < other.idm
            else:
                return self.idm < other.idm
        else:
            return self.time < other.time
    
    def __sub__ (self, other):
        return self.time - other.time

    def tempo(self):
        return self.time
    
    
    





