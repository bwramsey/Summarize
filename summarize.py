#!/usr/bin/python
import csv  # working with csv files
import os   # reading/writing files/directories
import sys  # for sys.exit if no valid file is found
from ollama import chat
aiModel = "gemma2"
entryCol = 12 # which column has the data we're looking for
	
# -- prompt for the survey results file from Carmen --
# search the directory for ".csv" files
fileList = []
for file in os.listdir("./"):
	if file.endswith(".csv"):
		fileList.append( file )

if len(fileList) < 1:
	sys.exit("Move a valid file into this directory. ")

# print a list of csv files for the user to select
for num, name in enumerate( fileList, start=1 ):
	print( str(num) +") " + name )

# prompt for the survey file exported from Carmen
indxA = input("Enter number for the Survey Results file: ")
surveyFilename = fileList[int(indxA)-1]
print(surveyFilename)

# open the survey csv file exported from Carmen, attach it to a reader, and read it into a list
surveyFile = open(surveyFilename, 'r')
csvSurvey =csv.reader( surveyFile )
surveyDataList = list( csvSurvey )
surveyFile.close()

tmp = [row for row in surveyDataList if row[0] == 'name']
headerRow = tmp[0]
surveyDataList = [row for row in surveyDataList if row != headerRow]

strFull = ''
for row in surveyDataList:
	strFull = strFull + '\n' + row[entryCol]
#print( strFull )

# what name to use for output files
outputFilename = input("Enter output filename: ")
if( len(outputFilename) <= 4):
	outputFilename = outputFilename + '.txt'       
elif( outputFilename[-4:] != '.txt'):
	outputFilename = outputFilename + '.txt'

messages = [
  {
    'role': 'user',
    'content': 'Students were asked this question: \" ' + headerRow[entryCol] + '\". Their responses were: \"' + strFull + '\". Please summarize their responses for their instructor.'
  },
]

response = chat( aiModel , messages=messages)
strAnswer = response['message']['content']
#print(response['message']['content'])
outputFile = open(outputFilename, 'w')	
outputFile.write( "Students were asked: \n\n" + headerRow[entryCol] + '\n\n')
outputFile.write( "Below is a summary of their responses: \n\n")
outputFile.write("------------------------------------------------------------------\n\n")
outputFile.write( strAnswer )	
	
print("Response written to file: " + outputFilename)	
#for st in outputList:
#    outputWriter.writerow([st])
outputFile.close()
exit()

