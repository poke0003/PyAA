class GameTurn:
    """object to preserve and manage state of the game turn."""

    def __init__(self):
        self._currentTurn = 1.1
        self.currentFaction = 'Germany'
        self.factionDict = {
            '0.1':'Germany',
            '0.2':'USSR',
            '0.3':'Japan',
            '0.4':'USA',
            '0.5':'China',
            '0.6':'UK',
            '0.7':'Italy',
            '0.8':'ANZAC',
            '0.9':'France'
        }

    def getCurrentTurn(self):
        return f'{self._currentTurn:.1f}'

    def _currentFactionIndicator(self):
        return self._currentTurn % 1

    def incrementTurn(self, minor = True):
        if minor:
            self._currentTurn += 0.1
            if self._currentFactionIndicator() < 0.1:
                self._currentTurn += 0.1
        else:
            self._currentTurn = int(self._currentTurn) + 1.1
        self.updateFaction()

    def updateFaction(self):
        self.currentFaction = self.factionDict[f'{self._currentFactionIndicator():.1f}']

    def nextFaction(self, minorTurns = 1):
        while self._currentFactionIndicator() + (minorTurns/10) > 0.91:
            minorTurns -= 9
        return self.factionDict[f'{self._currentFactionIndicator() + (minorTurns/10):.1f}']


#Test Routine
if __name__ == '__main__':
    print ('Basic GameTurn class test')
    myTurn = GameTurn()
    print (f'Default Turn (1.1): {myTurn.getCurrentTurn()}')
    print (f'Default Faction (Germany): {myTurn.currentFaction}')
    print ('-- Cycle through 10 turns (ending USSR) --')
    for i in range(10):
        myTurn.incrementTurn()
        print (f'New Turn: {myTurn.getCurrentTurn()}')
        print (f'New Faction: {myTurn.currentFaction}')
    print ('-- New Major Turn --')
    myTurn.incrementTurn(False)
    print (f'New Turn (X.1): {myTurn.getCurrentTurn()}')
    print (f'New Faction (Germany): {myTurn.currentFaction}')
    print (f'Next Faction (USSR): {myTurn.nextFaction()}')
    print (f'Faction After That (Japan): {myTurn.nextFaction(2)}')
    print (f'Full 26 turns later (France): {myTurn.nextFaction(26)}')
