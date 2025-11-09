#The 5 querys of the 5 questions
Question1 = """SELECT Count(Dates) AS "Amount of Campaigns",
               CASE
                   When MONTH(Dates) = 1 THEN "January"
                   When MONTH(Dates) = 2 THEN "February"
                   When MONTH(Dates) = 3 THEN "March"
                   When MONTH(Dates) = 4 THEN "April"
                   When MONTH(Dates) = 5 THEN "May"
                   When MONTH(Dates) = 6 THEN "June"
                   When MONTH(Dates) = 7 THEN "July"
                   When MONTH(Dates) = 8 THEN "August"
                   When MONTH(Dates) = 9 THEN "September"
                   When MONTH(Dates) = 10 THEN "October"
                   When MONTH(Dates) = 11 THEN "November"
                   When MONTH(Dates) = 12 THEN "December"
               END AS "Months", Channel_used AS 'Media Platform'
               FROM advertisingdata WHERE Month(Dates) < 7 AND engagement_Score < 8 GROUP BY month(Dates), Channel_used;"""

Question2  = """SELECT count(Campaign_ID) AS "Campaign", Location, Duration FROM advertisingdata 
                Where Clicks > 20000 GROUP BY Location, Duration ORDER BY Duration;"""

Question3 = """SELECT CAST(SUM(ROUND(Acquisition_Cost)) AS SIGNED) AS 'Acquisition Cost', Location, Language FROM advertisingdata 
               WHERE ROI = 5 GROUP BY Location, Language"""

Question4 = """SELECT CAST(ROUND(SUM(ROI)) AS SIGNED) AS 'Total ROI', Location, Channel_Used AS 'Media Platform'
               From advertisingdata GROUP BY Channel_Used, Location ORDER BY Location, Channel_Used"""
Question5 = """SELECT COUNT(Campaign_ID) AS 'Amount of Campaigns', Customer_Segment AS 'Customer Segments' , LANGUAGE AS 'Language' 
               FROM advertisingdata WHERE clicks <500  GROUP BY Customer_Segment, Language"""

#Lists that will store the information that is retrieved from each one
#of the queries
answer1 = []
answer2 = []
answer3 = []
answer4 = []
answer5 = []

#Store all the queries in one place and the answers as well
questions = [Question1, Question2, Question3, Question4, Question5]
answers = [answer1, answer2, answer3, answer4, answer5]

#Function that will use the received cursor to retrieve the
#information from the used query, fetch all the info from that
#query, and store it in the corresponding answer
def infoObtain(cursor):
    for i in range(0,5):
        cursor.execute(questions[i])
        answers[i] = cursor.fetchall()

#Finally, return all the answers
def returnQuestions():
    return answers