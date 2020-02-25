#!/usr/local/bin/python3
# This program will read in the csv schedule file from the NCSL
# website, and then convert it to a JSON file for use in iOS
# shortcuts.

# import the json module, for use in writing the json file
import json
import sys

# open the csv file for reading
inputFile = sys.argv[1]
outputFile = sys.argv[2]
gameDataInput = open(inputFile,'r')

# capture which team to filter on from argument 3
teamID = sys.argv[3]

# read in the game data, each line a separate array item
games = gameDataInput.readlines()

# extract the header names for each column from the first line
headers = games[0].split(',')

# create a empty dictionary to hold the entire json formatted game data
gameData = {}

# create an empty array of dictionaries, one for each game
gameDataArray = []

# step through each line of data (1 per game), skipping the first (the header data)
for i in range(1,len(games)):
    # get the data for the current game, and store it in an array
    eachGame = games[i].split(',')
    # filter data for selected teamID
    if (teamID == eachGame[3] or teamID == eachGame[7]):
        if (teamID == eachGame[3]):
            opponent = eachGame[8]
        elif (teamID == eachGame[7]):
            opponent = eachGame[4]

        # build the dictionary for the current game, stripping the '\n' character from the last key:value pair
        gameDataDictionary = {headers[0]:eachGame[0],headers[1]:eachGame[1],headers[2]:eachGame[2],"OPPONENT":opponent,headers[9].replace('\n',""):eachGame[9].replace('\n','')}
        # append the current game to the overall array of game data
        gameDataArray.append(gameDataDictionary)

# populate the dictionary for the json file
gameData['Games'] = gameDataArray

# open the json file for writing, write the data, and then close the file
gameDataOutput = open(outputFile, 'w+')
gameDataOutput.write(json.dumps(gameData, indent=4))
gameDataOutput.close()
