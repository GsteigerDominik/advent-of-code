pointDict= {
    # 1P
    "AX":4, #3P
    "BX":1, #0P
    "CX":7, #6P

    # 2P
    "AY":8, #6P
    "BY":5, #3P
    "CY":2, #0P

    # 3P
    "AZ":3, #0P
    "BZ":9, #6P
    "CZ":6 #3p
}
predictionDict= {
    #Verlieren
    "AX":3, #AZ
    "BX":1, #BXx
    "CX":2, #CY

    # We need to Draw
    "AY":4, #AX
    "BY":5, #BY
    "CY":6, #CZ

    # 3P
    "AZ":8, #AY
    "BZ":9, #BZ
    "CZ":7 #CX
}
import re


file1 = open('input.txt', 'r')
Lines = file1.readlines()

totalPoints=0
totalPointsPrediction=0


for line in Lines:
    #X is lose
    totalPoints += pointDict[re.sub(r'\s+', '', line)]
    totalPointsPrediction += predictionDict[re.sub(r'\s+', '', line)]
print(totalPoints)
print(totalPointsPrediction)