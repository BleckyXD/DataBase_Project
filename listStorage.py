#Query 1 / Graph 1
#Lists that will store the column that we retrieve
campaigns = []
months = []
mediaType = []

#Three titles for the graphs
title1 = ["Months", "Media Platforms", "Campaigns", "Engagement Score"]

#Store the column lists in one place
qRows1 = [months, mediaType, campaigns]

#Names of the columns we will retrieve, the keys
rows1Names = ["Months", "Media Platform", "Amount of Campaigns"]

#This same process is repeated for the 5 queries

#Query 2 / Graph 2
Amount = []
location = []
duration = []
title2 = ["Location", "Duration", "Campaign Amount", "Advertisements and Duration"]
qRows2 = [Amount, location, duration]
rows2Names = ["Location", "Duration", "Campaign"]

#Query 3 / Graph 3
acquisitionCost = []
location = []
language = []
title3 = ["Language", "Location", "Acquisition Cost", "Total Acquisition Cost"]
qRows3 = [acquisitionCost, location, language]
rows3Names = ["Language", "Location", "Acquisition Cost"]

#Query 4 / Graph 4
totalROI = []
roiLocation = []
mediaPlat = []
title4 = ["Media Type", "Location", "ROI", "Language Based ROI"]
qRows4 = [totalROI, roiLocation, mediaPlat]
rows4Names = ["Media Platform", "Location", "Total ROI"]

#Query 5 / Graph 5
lan = []
camp = []
amountPeople = []
title5 = ["Languages", "Customer Segments", "Campaigns", "Low interacting Ads"]
qRows5 = [lan, camp, amountPeople]
rows5Names = ["Language", "Customer Segments", "Amount of Campaigns"]

#Store all the row lists that contain the lists that store the information separately
#In other words, a nested list
#Same logic is repeated for the names and titles
rowsAll = [qRows1, qRows2, qRows3, qRows4, qRows5]
rowsAllNames = [rows1Names, rows2Names, rows3Names, rows4Names, rows5Names]
titleAll = [title1, title2, title3, title4, title5]
