class Territory:
    """Object that defines a map territory"""


    def __init__(self, name, territoryType, isCapital, incomeValue, startingOwner):
        self.name = name
        self.terrType = territoryType
        self.isCapital = isCapital
        self.income = incomeValue
        self.owner = {'0.0':startingOwner}

    def _keysAsNums(self):
        return [float(i) for i in self.owner.keys()]

    def updateOwner(self, newOwner, currentTurn):
        self.owner[currentTurn] = newOwner

    def getCurrentOwner(self):
        return self.owner[f'{max(self._keysAsNums()):.1f}']

    def resetOwnerToTurnX(self, resetTurn):
        rollbackKeys = [largeKey for largeKey in self.owner.keys() if int(float(largeKey)*10) > int(float(resetTurn)*10)]
        while len(rollbackKeys) > 0:
            del self.owner[rollbackKeys.pop()]

    def getOwnerOnTurnX(self, referenceTurn):
        if referenceTurn in self.owner:
            return self.owner[referenceTurn]
        else:
            return self.owner[max([smallKey for smallKey in self.owner.keys() if int(float(smallKey)*10) <= int(float(referenceTurn)*10)])]

    def __str__(self):
        return f'{self.name}: {self.terrType} type with income {self.income} owned by {self.getCurrentOwner()} - Capital status: {self.isCapital}'

#WORKS!!  Still need to build test Routine
if __name__ == '__main__':
    t = Territory('West Germany', 'Land', True, 10, 'Germany')
    print (t)
    #insert test routine here
