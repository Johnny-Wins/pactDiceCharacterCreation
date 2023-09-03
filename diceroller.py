import random
def main():
    
    #initialize starting variables
    successfulRuns = 0
    unsuccesfulRuns = 0
    results = [0,0,0,0,0,0]

    #request user inputs
    bonus = int(input("What is the bonus on this roll, counting both bonuses and maluses?"))
    learning = int(input("What is your learning score on this roll (the numer of extra dice you get when rolling?)"))

    simCount = 100000

    #initiate simulation
    for x in range(simCount):
        baseRange = [
            random.randrange(1 + bonus,7 + bonus),
            random.randrange(1 + bonus,7 + bonus),
            random.randrange(1 + bonus,7 + bonus),
            random.randrange(1 + bonus,7 + bonus),
        ]

        learningRange = []

        for y in range(learning):
            learningRange.append(random.randrange(1 + bonus,7 + bonus))

        improvedRange = sorted(baseRange)

        exhaustion = learning

        for z in range(learning):
            for a in range(len(improvedRange)):
                if exhaustion > z and learningRange[z] > a:
                    exhaustion = exhaustion - 1
                    improvedRange[a] = learningRange[z]
                    
        

        if checkRangeOfDice(improvedRange,6):
            results[5] += 1
            print("We got a perfect result!\n\n\n\n\n")
        else:
            if checkRangeOfDice(improvedRange,5):
                results[4] += 1
            else:
                if checkRangeOfDice(improvedRange,4):
                    results[3] += 1
                else:
                    if checkRangeOfDice(improvedRange,3):
                        results[2] += 1
                    else:
                        if checkRangeOfDice(improvedRange,2):
                            results[1] += 1
                        else:
                            results[0] += 1


    print("Results with all sixes:",results[5])
    print("Results with fives and sixes:",results[4])
    print("Results with 4-6:",results[3])
    print("Results with 3-6:",results[2])
    print("Results with 2-6:",results[1])
    print("Results with 1-6:",results[0])
    
    print("Percentage of results with all sixes:",results[5] / simCount * 100, "%")
    print("Percentage of results with just 5-6:",results[4] / simCount * 100, "%")
    print("Percentage of results with just 4-6:",results[3] / simCount * 100, "%")
    print("Percentage of results with just 3-6:",results[2] / simCount * 100, "%")
    print("Percentage of results with just 2-6:",results[1] / simCount * 100, "%")
    print("Percentage of remaining results:",results[0] / simCount * 100, "%")
    

    


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


main()