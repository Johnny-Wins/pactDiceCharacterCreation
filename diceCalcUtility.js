const schoolTable = [
    ["War Magic","Summoning","Elementalism","Augar of Omens","Evangelism"], //Conjure

    ["Harbinger","Host","Blood","Heartless","Cultist"], //Prices

    ["Goblin","Sympath","Collector","Luck","Chosen"], //Tools

    ["Scourge","Nomad/City","Technomancer","Astrology","Draiodhe"], //Realms

    ["Oni","Faerie","Enchanting","Finder/Chaos Mage","Shamanism"], //Interaction

    ["Heroics","Binding","Alchemy","Augury","Priesthood"], //Lore

    ["Ogre","Sealing","Wards","Chronomancy","Law"] //Protection
//Conflict|Deals|Visceral|Immaterial|Divine
]

const columns = ["Conflict","Deals","Visceral","Immaterial","Divine"]

const rows = ["Conjure","Prices","Tools","Realms","Interaction","Lore","Protection"]

class Arcana {
    constructor(row,col) {

        this.row = row;
        this.col = col;
        this.arcanaSchool = "";

        this.arcanaType = "Field";

        if(this.col == null) {
            this.arcanaType = "Row";
        };

        if(this.row == null){
            this.arcanaType = "Column";
        };

        //Arcanaschool definer

        if(this.col == null) {
            this.arcanaSchool = rows[row];
        };

        if(this.row == null){
            this.arcanaSchool = columns[col];
        };

        if((this.row != null) && (this.col != null)) {
            this.arcanaSchool = schoolTable[this.row][this.col];
        }
    }

    toString() {
        if(this.col == null) {
            return rows[this.row];
        };

        if(this.row == null){
            return columns[this.col];
        };

        return schoolTable[this.row][this.col];
    }
}

class Dabbling {
    constructor(row,col,card) {
        this.arcana = new Arcana(row, col);

        this.tier = card;
    }

    toString() {
        console.log("This tier " + this.tier + " dabbling is in the the arcana of " + this.arcana.arcanaSchool)
        return ("This tier " + this.tier + " dabbling is in the the arcana of " + this.arcana.arcanaSchool)
    }
}

class Clue {
    constructor(clueArray) {
        this.clueCol = clueArray[0];
        this.clueRow = clueArray[1];
        this.tier = clueArray[2];

        this.arcana = new Arcana(this.clueRow,this.clueCol)

        this.clueType = "Field";

        if(this.clueCol == null) {
            this.clueType = "Row";
        };

        if(this.clueRow == null){
            this.clueType = "Column";
        };
    }

    toString() {
        console.log("This is a tier " + this.tier + " clue;")
        if (this.clueType == "Field") {
            console.log("It is specific to the field of " + schoolTable[this.clueCol][this.clueRow])
            return schoolTable[this.clueCol][this.clueRow];
        }
        if (this.clueType == "Row") {
            console.log("It can be used for any schools in the row of " + rows[this.clueRow])
            return rows[this.clueRow];
        }
        if (this.clueType == "Column") {
            console.log("It can be used for any schools in the column of " + columns[this.clueCol])
            return columns[this.clueCol];
        }
    }
}

class Text {
    constructor(textArray) {
        this.arcanaList = []
        for(let count = 0; count < textArray.length; count++){
            this.arcanaList.push(new Arcana(textArray[count][0],textArray[count][1]));
        }
    }

    toString() {
        console.log("This is a text with the following arcana: ");
        let count = 0;
        /*arcaneTypes.forEach(function(arcana) {
            arcana.toString();
        })*/

        for(count = 0; count < this.arcanaList.length; count++){
            console.log(this.arcanaList[count].toString());
        }
    }
}

class Character {
    constructor(dabbleInputs,CluesInputs,textInputs,knowledge,learning) {
        /*this.arcanaColumn = arcanaColumn;
        this.columnCard = columnCard
        this.arcanaRow = arcanaRow;
        this.rowCard = rowCard;*/

        this.dabbleObjects = dabbleInputs.map(function(curDabble) {
            return new Dabbling(...curDabble);
        });


        this.CluesInputs = CluesInputs;
        this.clueObjects = CluesInputs.map(function(curClue) {
            return new Clue(curClue);
        });


        this.textInputs = textInputs;
        this.textObjects = textInputs.map(function(curText) {
            return new Text(curText);
        });

        this.knowledge = knowledge;
        this.knowledgeBonus = knowledge - 3;

        this.learning = learning;
    }

    removeText(num){
        this.textObjects.splice(num,1);
    }

    removeClue(num){
        this.clueObjects.splice(num,1);
    }

    toString() {
        console.log("This character the following Arcana Bonuses: ");
        this.dabbleObjects.forEach(function(curDab){ 
            curDab.toString();
        })

        
        console.log("The following Clues are available to this character: ");
        this.clueObjects.forEach(function(curClue){ 
            curClue.toString();
        })

        
        console.log("The following Texts are available to this character: ");
        this.textObjects.forEach(function(curText){ 
            curText.toString();
        })

        console.log("This character has a knowledge score of " + this.knowledge + " giving them a bonus of " + this.knowledgeBonus);

        console.log("This character has a learning of " + this.learning);
    }
}


//Rows: "Conjure","Prices","Tools","Realms","Interaction","Lore","Protection"
//Columns: "Conflict","Deals","Visceral","Immaterial","Divine"


const tamI = new Character(
    //[1,3,2,4,]

    [
        [null,1,3],[2,null,4],[6,3,3],[1,4,1],[6,2,-1]
    ],

    [
        [3,null,2], [null,6,2], [6,4,1], [2,null,1],[null,2,2]
    ],

    [
        [[2,1],[null,1],[2,null]],
        [[6,4],[null,4],[4,null],[null,1]]
    ]);

const Grif = new Character(

    [
        [null,3,4],[0,null,3],[0,3,2],[2,4,1],[6,0,0]
    ],

    [
    
    ],

    [
        
    ],

    4,

    1
)

Grif.toString()

function compareArcana (arcanaObj,row,col) {

    if (arcanaObj.arcanaType == "Field") {
        if (arcanaObj.row == row && arcanaObj.col == col) {
            return true;
        }
        else{
            return false;
        }
    }

    if (arcanaObj.arcanaType == "Row") {
        if (arcanaObj.row == row) {
            return true;
        }
        else{
            return false;
        }
    }

    if (arcanaObj.arcanaType == "Column") {
        if (arcanaObj.col == col) {
            return true;
        }
        else{
            return false;
        }
    }
}

function checkAllTheCriteria(inputChara,inputSchool) { //Will return a number between 1 and 6 based on what criteria are met

    let chara = JSON.parse(JSON.stringify(inputChara));

    let criteriaCount = 0;

    //check for the bonus of full dabbling (row and column and field)
    fullDab = 0;
    if(dabbleObjects.reduce(function(curDab){
        if(compareArcana(curDab.arcana,inputSchool[0],inputSchool[1])){
            return 1;
        }
    }));




    //SpecificText: Checks texts and dabblings; succeeds if there is at least one thing in the exact field of study (dabblings can only succeed if you have a row arcana, a column arcana, and a dabbling at their intersection); removes texts used

    //DeeperWorks: Checks texts and dabblings; succeeds if there are three things in the exact field of study; removes texts used

    //ExtensiveStudies: Checks texts and dabblings; succeeds if there are seven things in the exact field of study; removes texts used

    //RelatedWorks: Checks texts and dabblings; succeeds if there are three things that match two out of the three categories of ROw, Column, and Field; removes texts used

    //BroaderStudies: Checks texts and dabblings; succeeds if there are seven things that match two out of the three categories of Row, Column, and Field; removes texts used

    /*CollectedKnowledge: Checks clues; does not add to criteriaCount, but creates a list with the format:
    [1, yes],
    [2, yes],
    [4, no],
    [8, no],
    based on whether there are the associated number of clues.
    */

}

class Roll {
    constructor(rollArray){
        this.baseRoll = [rollArray[0],rollArray[1],rollArray[2],rollArray[3]]

        this.knowledgeRolls = []

        if (rollArray.length > 4){
            count = 0 
            while (count < rollArray.length){
                if (count > 3){
                    this.knowledgeRolls.push(rollArray[count]);
                }
                count++;
            }
        }

    }

    toString(){
        console.log("\nPuissance: " + this.baseRoll[0], "\nAccess: " + this.baseRoll[1] + "\nLongevity: " + this.baseRoll[2] + "\nExcecutions: " + this.baseRoll[3])
    }
    
}

function diceCheck(character,spellField,spellDifficulty,...rolls){ //Example Input: diceCheck(0,[0,3],4,[2,5,5,6,1],[3,4,1,6,5],[2,1,6,2,2])
    character = null;

    //spellField should be formatted as [row,column] as on the above tables
    spellFieldArcana = new Arcana(spellField[0],spellField[1])

    //spellDifficulty should be formated as a number from 1 to 8

    console.log("So you're trying to make a(n) " + spellFieldArcana.toString() + " spell with " + spellDifficulty + " difficulty.")

    console.log(rolls);

    console.log("You had the following rolls:\n")
    rolls.forEach(function(curr){
        console.log("\nPuissance: " + curr[0], "\nAccess: " + curr[1] + "\nLongevity: " + curr[2] + "\nExcecutions: " + curr[3])

        if (curr.length > 4){
            console.log("Also since your character has learning, you have these additional values to work with in this roll:")
        }

        count = 0 
        while (count < curr.length){
            if (count > 3){
                console.log(curr[count]);
            }
            count++;
        }
    })

    rollObjects = [];

    rolls.forEach(function(curr){

        rollObjects.push(new Roll(curr))

    })


    dabbleBonuses = [];
    (Grif.dabbleObjects.forEach(function(curDab){
        if(compareArcana(curDab.arcana,spellFieldArcana.row,spellFieldArcana.col)){
            dabbleBonuses.push(curDab);
        }
    }));

    rolltracker = 0
    Options = []

    dabbleBonuses.forEach(function(currDabbleBonus){

        bonusedRolls = rollObjects[rolltracker].baseRoll.map(function(currentDie){
            return currentDie + currDabbleBonus.tier - spellDifficulty;
        })

        bonusedOptions = rollObjects[rolltracker].knowledgeRolls.map(function(currentDie){
            return currentDie + currDabbleBonus.tier - spellDifficulty;
        })
        

        bonusedRolls[0] = [bonusedRolls[0],"Puissance"];
        bonusedRolls[1] = [bonusedRolls[1],"Access"];
        bonusedRolls[2] = [bonusedRolls[2],"Longevity"];
        bonusedRolls[3] = [bonusedRolls[3],"Excecutions"];

        bonusedRolls.sort((a,b) => a[0] - b[0]);
        
        bonusedOptions.forEach(function(currDie){
                let used = false;

            bonusedRolls.forEach(function(currCompareDie,index){
                if (currCompareDie[0] < currDie&&used == false){
                    
                    bonusedRolls[index] = [currDie,currCompareDie[1]];
                    used = true;
                } 
            })

        });


        
        optimizedRoll = [
            bonusedRolls.find((thingy) => thingy[1] == "Puissance"),
            bonusedRolls.find((thingy) => thingy[1] == "Access"),
            bonusedRolls.find((thingy) => thingy[1] == "Longevity"),
            bonusedRolls.find((thingy) => thingy[1] == "Excecutions")
        ]

        Options.push(optimizedRoll);
        rolltracker++;
    });
    
    console.log("So! Here are your options:")

    Options.forEach(function(curr){
        console.log("\n\n\n");
        curr.forEach((value) => console.log(value[1] + ": " + value[0]))
    })
}

