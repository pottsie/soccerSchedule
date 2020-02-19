# This program will read in the csv schedule file from the NCSL
# website, and then convert it to a JSON file for use in iOS
# shortcuts.

# import the json module, for use in writing the json file
import json

# open the csv file for reading
gameDataInput = open('SCAA_schedule.csv','r')

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
    # build the dictionary for the current game, stripping the '\n' character from the last key:value pair
    gameDataDictionary = {headers[0]:eachGame[0],headers[1]:eachGame[1],headers[2]:eachGame[2],headers[3]:eachGame[3],headers[4]:eachGame[4],headers[5]:eachGame[5],headers[6]:eachGame[6],headers[7]:eachGame[7],headers[8]:eachGame[8],headers[9]:eachGame[9],headers[10]:eachGame[10],headers[11].replace('\n',""):eachGame[11].replace('\n','')}
    # append the current game to the overall array of game data
    gameDataArray.append(gameDataDictionary)

# populate the dictionary for the json file
gameData['Games'] = gameDataArray

# open the json file for writing, write the data, and then close the file
gameDataOutput = open('club_schedule.json', 'w+')
gameDataOutput.write(json.dumps(gameData, indent=4))
gameDataOutput.close()
