import random
class Run: # this class makes an object which includes information about an individual run within a simulation. It can be queried in multiple ways to extra useful data about what happened during that run.
    def __init__(self,runData): #this constructor should be fed an array of die results
        self.runData = runData
    
    def total(self):
        sum = 0
        for die in self.runData:
            sum += die
        return sum
    
    def numOfSuccesses(self,check):
        successes = 0
        for die in self.runData:
            if die >= check:
                successes += 1
        return successes

def main():
    
    #initialize starting variables

    #request user inputs
    rollTypeInput = int(input("Enter 1 if this is a roll concerned with the overall total, and 2 if this is a roll concerned with the results of individual \n"))

    if rollTypeInput == 1:
        rollType = "Total"
    if rollTypeInput == 2:
        rollType = "Success"

    diceNum = int(input("How many dice are you going to roll?\n"))
    diceType = int(input("What kind of dice are you rolling (how many sides do they have?)\n"))
    dieBonus = int(input("What number are you adding to every die (if any)?)\n"))

    if rollType == "Total":
        flatBonus = int(input("What number are you adding to the overall result (if any)?)\n"))
        threshhold = 0
    if rollType == "Success":
        threshhold = int(input("What roll does a die need to reach (or exceed) in order to count as a success?\n"))
        flatBonus = 0

    rollSomeDice(rollType,diceNum,diceType,dieBonus,flatBonus,threshhold)


def rollSomeDice(rollType,diceNum,diceType,dieBonus,flatBonus,threshhold):
    simCount = 100000
    runLog = []

    if rollType == 1:
        rollType = "Total"
    if rollType == 2:
        rollType = "Success"


    #initiate simulation
    for x in range(simCount):
        runResults = []

        for die in range(diceNum):
            
            runResults.append(random.randrange(1,diceType + 1) + dieBonus)

            
        
        
        

        currentRun = Run(runResults)

        runLog.append(currentRun)

    #Display results
    
    if rollType == "Total":
        sum = 0
        for run in runLog:
            sum += run.total()
            sum += flatBonus
        average = sum / simCount
        print("The average total is ",average)

    if rollType == "Success":
        sum = 0
        for run in runLog:
            sum += run.numOfSuccesses(threshhold)
        average = sum / simCount
        print("The average number of successes is ",average)

        rangeOfDice = []

        for x in range(diceNum):
            rangeOfDice.append(x + 1)

        for dice in rangeOfDice: #this loop will go once for each die in each roll
            goodRun = 0
            for run in runLog:
                if run.numOfSuccesses(threshhold) >= dice:
                    goodRun += 1
            average = goodRun / simCount
            averagePercent = round((average * 100),2)
            print(averagePercent,"percent of runs have at least",dice,"succesful dice.")

            
        

    

    


def checkDie(dieResult,query):
    if dieResult >= query:
        return True
    else:
        return False
    
def checkRangeOfDice(dieArray,query):
    arrayGooditude = 0
    for x in dieArray:
        if checkDie(x,query):
            arrayGooditude += 1

    if arrayGooditude == len(dieArray):
        return True
    else:
        return False
    
def d6():
    return random.randrange(1, 7)

def makeTroikan(numTroikans):
    
    for x in range(numTroikans):
        print("Character Number ",x + 1)
        print("Skill: ", (3 + (random.randrange(1, 4))))
        print("Stamina: ", d6() + d6() + 12)
        print("Luck: ",d6() + 6)
        print("Background: ",d6(),d6(),sep='')
        print("Starting Silver: ",d6() + d6(),"\n")


makeTroikan(2)