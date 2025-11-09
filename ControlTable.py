#Import external files for usage
import queryStorage as qs
import ObtainData as od
import listStorage as ls
import graphControlOrganized as gdc
import Luis_Code as lc


import numpy as np #Array

#Exception class for input validation
class validation(Exception):
    pass

#Functions for input validation
def validate(value):
    if value < 0 or value > 5:
        raise validation("\nValue must be between 0 and 5]\n")
    return True
def validate2(value):
    if not value == 0 and not value == 1:
        raise validation("\n[Value must be 0 or 1]\n")
    return True

#Call for retrieving the info from the table
od.data()

#Call for storing the question's answers, the data
answers = qs.returnQuestions()

#Call for the rows we will retrieve from the table
rowsAll = ls.rowsAll

#For those rows, they will need names and titles
rowsAllNames = ls.rowsAllNames
titlesAll = ls.titleAll

#For loop that will retrieve the information of the tables and store them like x, y, and z
for i in range(0,5):
    rowsAll[i][0].extend([row[rowsAllNames[i][0]] for row in answers[i]])
    rowsAll[i][1].extend([row[rowsAllNames[i][1]] for row in answers[i]])
    rowsAll[i][2].extend([row[rowsAllNames[i][2]] for row in answers[i]])

#Hector's Questions
questions = [
            "|How many people did the media types reach, in the first six months, with an engagement score lower than 8?       |",
            "|What is the duration of the advertisements for the consumers in the different cities with 20,000 clicks or more? |",
            "|What is the total acquisition cost of advertisements in each platform with a ROI equal to 5?                     |",
            "|What is the total Return on investment (ROI) in each language and Location that was used to advertise?           |",
            "|What are the languages used when the clicks on ads where below 500 and we only used companies from 'A' to 'J'?   |"
]

#Luis's Question
questionsLuis = ["What is the gender distribution of consumers by media type used for advertising? |",
                 "What is the age distribution of consumers by advertisement duration?             |",
                 "What is the amount of people based on the costumer segment and their language?   |",
                 "What is the amount of clicks in the different cities based on the duration?      |",
                 "What is the amount of people per campaign goal and the customer segment?         |"]


print("---------Databases | Graphs -----------")
firstPass = True
while firstPass:
    try:
        firstPass = True
        secondPass = True
        thirdPass = True
        choice0 = input("Choose Questions | Hector (0) | Luis (1) | Close(x): ")

        #Check if we want to close the program
        if choice0.lower() == "x":
            firstPass = False
        else:
            #If not closed, check if the selected option is a number
            if not choice0.isdigit():
                raise validation("\n[Please enter a valid character]\n")

            #Check if it is the number 0 or 1
            if validate2(int(choice0)):

                #Print the corresponding questions
                if choice0 == "0":

                    a = 1
                    print()
                    for i in questions:
                        print("-" * 126 + "|")
                        print(f"Question {a}: {i}")
                        a += 1
                    print("-" * 126 + "|")
                elif choice0 == "1":
                    a = 1
                    print()
                    for i in questionsLuis:
                        print("-" * 93 + "|")
                        print(f"Question {a}: {i}")
                        a += 1
                    print("-" * 93 + "|")

                while secondPass:
                    try:
                        #If Hector's graph are selected, select what graph you want to check
                        choice1 = input("Go back(0) | Select Graph | (1-5): ")

                        #Check that it is a digit
                        if not choice1.isdigit():
                            raise validation("\n[Please enter a valid character]\n")

                        #A boolean determining that the value is between 1 and 5
                        permitted = validate(int(choice1))
                        if choice0 == "0":
                            #If it is a valid value, we continue
                            if permitted:
                                #If we want to leave, the loop's boolean will become false
                                if choice1 == "0":
                                     secondPass = False

                                elif  permitted:
                                    thirdPass = True
                                    i = int(choice1) - 1

                                    #Give the values to x, y, and z, and also to the titles
                                    x = rowsAll[i][0]
                                    y = rowsAll[i][1]
                                    z = rowsAll[i][2]
                                    xTitle = titlesAll[i][0]
                                    yTitle = titlesAll[i][1]
                                    zTitle = titlesAll[i][2]
                                    mainTitle = titlesAll[i][-1]

                                    #Make sure that the repeated names are stored as only 1
                                    x = list(dict.fromkeys(x))
                                    y = list(dict.fromkeys(y))
                                    z = np.array(z)

                                    while thirdPass:
                                        try:
                                            #Choose the type of graph
                                            print("Choose graph type:")
                                            print("| (0)Go Back           |")
                                            print("| (1)Pie Chart         |")
                                            print("| (2)3D Bar Chart      |")
                                            print("| (3)Bar Chart         |")
                                            print("| (4)3D Scatter Chart  |")
                                            print("| (5)Scatter Chart     |")
                                            choice2 = input(">")
                                            if not choice2.isdigit():
                                                raise validation("\n[Please enter a valid character]\n")
                                            if validate(int(choice2)):

                                                #Call the corresponding graph
                                                if choice2 == "1":
                                                    gdc.pieChart(x, y, z, mainTitle)
                                                elif choice2 == "2":
                                                    gdc.bar3D(x, y, z, xTitle, yTitle, zTitle, mainTitle)
                                                elif choice2 == "3":
                                                    gdc.barPlot(x, y, z, xTitle, yTitle, zTitle, mainTitle)
                                                elif choice2 == "4":
                                                    gdc.scatter3D(x, y, z, xTitle, yTitle, zTitle, mainTitle)
                                                elif choice2 == "5":
                                                    gdc.scatter(x, y, z, xTitle, yTitle, zTitle, mainTitle)
                                                elif choice2 == "0":
                                                    thirdPass = False
                                        except Exception as e:
                                            print(e)
                                elif choice1 == "0":
                                    secondPass = False

                        #If luis's graphs are chosen, it will be prompted to
                        #select a graph between 1 and 5, and the corresponding
                        #graph/function will be called
                        elif choice0 == "1":
                            if permitted:
                                if choice1 == "0":
                                    secondPass = False
                                elif choice1 == "1":
                                    lc.graph1()
                                elif choice1 == "2":
                                    lc.graph2()
                                elif choice1 == "3":
                                    lc.graph3()
                                elif choice1 == "4":
                                    lc.graph4()
                                elif choice1 == "5":
                                    lc.graph5()
                    except Exception as e:
                        print(e)
    except Exception as e:
        print(e)
