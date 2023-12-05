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
    
    def optimizeWithLearning(self):
        spellRange = interpretAsPactDice(self.runData[0],self.runData[1],self.runData[2],self.runData[3])
        self.spellScore = sum(spellRange)
        #Begin Learning Section

        if len(self.runData) > 4:

            amountOfLearning = len(self.runData) - 4

            learningValues = []

            for x in range(amountOfLearning):
                learningValues.append(self.runData[4 + x])

            for die in learningValues:
                replacementScores = [-5,-5,-5,-5]
                for x in range(4):
                    theoreticalRange = [self.runData[0],self.runData[1],self.runData[2],self.runData[3]]
                    theoreticalRange[x] = die

                    replacementScores[x] = sum(interpretAsPactDice(theoreticalRange))
                
                if max(replacementScores) > self.spellScore:
                    



        #End learning section
        
        self.optimizedSpell = spellRange

        return spellRange
    
class ResultTable:
    def __init__(self):
        self.negativeOne = 0
        self.negativeTwo = 0
        self.negativeThree = 0
        self.negativeFour = 0
        self.zero = 0
        self.one = 0
        self.two = 0
        self.three = 0
        self.four = 0
        self.five = 0
        self.six = 0
        self.seven = 0
        self.eight = 0
        self.nine = 0
        self.ten = 0
        self.eleven = 0
        self.twelve = 0
        self.thirteen = 0
        self.fourteen = 0
        self.fifteen = 0

    def resultArray(self):
        return [self.negativeFour,self.negativeThree,self.negativeTwo,self.negativeOne,self.zero,self.one,self.two,self.three,self.four,self.five,self.six,self.seven,self.eight,self.nine,self.ten,self.eleven,self.twelve,self.thirteen,self.fourteen,self.fifteen]
    
    def printResults(self,simcount):

        curListPos = -4
        for x in self.resultArray():
            print(curListPos, ": ", x, " || ", round(x / simcount * 100,2), "% of results",sep='')
            curListPos += 1


        


    
def interpretAsPactDice(die1,die2,die3,die4):
    runData = [die1,die2,die3,die4]
    spellRange = [-5,-5,-5,-5]

    #sets puissance
    if runData[0] < 1: #Sets result if die is less than 1
        spellRange[0] = -1
    elif runData[0] == 1: #Sets result if die 1
        spellRange[0] = 1.8
    elif runData[0] == 2: #Sets result if die is 2
        spellRange[0] = 1
    elif runData[0] == 3: #Sets result if die is 3
        spellRange[0] = 2
    elif runData[0] == 4: #Sets result if die is 4
        spellRange[0] = 2
    elif runData[0] == 5: #Sets result if die is 5
        spellRange[0] = 3
    elif runData[0] > 5: #Sets result if die is 6 or more
        spellRange[0] = 4

    #sets access
    if runData[1] < 1: #Sets result if die is less than 1
        spellRange[1] = -1
    elif runData[1] == 1: #Sets result if die 1
        spellRange[1] = -1
    elif runData[1] == 2: #Sets result if die is 2
        spellRange[1] = 1.8
    elif runData[1] == 3: #Sets result if die is 3
        spellRange[1] = 0
    elif runData[1] == 4: #Sets result if die is 4
        spellRange[1] = 0
    elif runData[1] == 5: #Sets result if die is 5
        spellRange[1] = 0
    elif runData[1] > 5: #Sets result if die is 6 or more
        spellRange[1] = 4

    #sets longevity
    if runData[2] < 1: #Sets result if die is less than 1
        spellRange[2] = -1
    elif runData[2] == 1: #Sets result if die 1
        spellRange[2] = -1
    elif runData[2] == 2: #Sets result if die is 2
        spellRange[2] = -2
    elif runData[2] == 3: #Sets result if die is 3
        spellRange[2] = 1.8
    elif runData[2] == 4: #Sets result if die is 4
        spellRange[2] = 2
    elif runData[2] == 5: #Sets result if die is 5
        spellRange[2] = 3
    elif runData[2] > 5: #Sets result if die is 6 or more
        spellRange[2] = 3

    #sets excecutions
    if runData[3] < 1: #Sets result if die is less than 1
        spellRange[3] = -1
    elif runData[3] == 1: #Sets result if die 1
        spellRange[3] = 1.8
    elif runData[3] == 2: #Sets result if die is 2
        spellRange[3] = 0
    elif runData[3] == 3: #Sets result if die is 3
        spellRange[3] = 0
    elif runData[3] == 4: #Sets result if die is 4
        spellRange[3] = 0
    elif runData[3] == 5: #Sets result if die is 5
        spellRange[3] = 3
    elif runData[3] > 5: #Sets result if die is 6 or more
        spellRange[3] = 4    

    return spellRange
            
        
            

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
    simCount = 10
    runLog = []

    if rollType == 1:
        rollType = "Total"
    if rollType == 2:
        rollType = "Pactdice"


    #initiate simulation
    for x in range(simCount):
        runResults = []

        for die in range(diceNum):
            
            runResults.append(random.randrange(1,diceType + 1) + dieBonus)

        currentRun = Run(runResults)

        currentRun.optimizeWithLearning()

        runLog.append(currentRun)

    #Display results
    
    if rollType == "Total":
        sum = 0
        for run in runLog:
            sum += run.total()
            sum += flatBonus
        average = sum / simCount
        print("The average total is ",average)

    if rollType == "Pactdice":
        sum = 0
        resultTable = ResultTable()
        for run in runLog:
            sum += run.spellScore

            if run.spellScore == 15:
                resultTable.fifteen += 1
            if run.spellScore < 15 and run.spellScore > 13.99:
                resultTable.fourteen += 1
            if run.spellScore < 14 and run.spellScore > 12.99:
                resultTable.thirteen += 1
            if run.spellScore < 13 and run.spellScore > 11.99:
                resultTable.twelve += 1
            if run.spellScore < 12 and run.spellScore > 10.99:
                resultTable.eleven += 1
            if run.spellScore < 11 and run.spellScore > 9.99:
                resultTable.ten += 1
            if run.spellScore < 10 and run.spellScore > 8.99:
                resultTable.nine += 1
            if run.spellScore < 9 and run.spellScore > 7.99:
                resultTable.eight += 1
            if run.spellScore < 8 and run.spellScore > 6.99:
                resultTable.seven += 1
            if run.spellScore < 7 and run.spellScore > 5.99:
                resultTable.six += 1
            if run.spellScore < 6 and run.spellScore > 4.99:
                resultTable.five += 1
            if run.spellScore < 5 and run.spellScore > 3.99:
                resultTable.four += 1
            if run.spellScore < 4 and run.spellScore > 2.99:
                resultTable.three += 1
            if run.spellScore < 3 and run.spellScore > 1.99:
                resultTable.two += 1
            if run.spellScore < 2 and run.spellScore > 0.99:
                resultTable.one += 1
            if run.spellScore < 1 and run.spellScore > -0.99:
                resultTable.zero += 1
            if run.spellScore < 0 and run.spellScore > -1.99:
                resultTable.negativeOne += 1
            if run.spellScore < -1 and run.spellScore > -2.99:
                resultTable.negativeTwo += 1
            if run.spellScore < -2 and run.spellScore > -2.99:
                resultTable.negativeThree += 1
            if run.spellScore == -4:
                resultTable.negativeFour += 1
            



        average = sum / simCount
        print("The average quality of this spell is ",average)
        resultTable.printResults(simCount)

        rangeOfDice = []



            
        

    

    


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
    
rollSomeDice(2,6,6,0,0,0)