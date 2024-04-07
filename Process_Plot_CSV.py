'''
Andrew Harris
CIS123
5.5 Performance Assessment 
'''

import csv #importing csv library 
from matplotlib import pyplot as plt #importing matplotlib for plotting

x=[] #declaring empty list for x axis
y=[] #declaring empty list for x axis
personalInfo=['Andrew','Harris','30','Information Science','100','11/4/2021'] #creating list with info to be appended

#opening file in append mode to write information to it
with open("c:\\Users\\andhar5173\\Desktop\\PerformanceAssessment5_5DataFile.csv","a",newline="") as myfile:

        #creating writer object and writing personalInfo to file
        writer = csv.writer(myfile)
        writer.writerow(personalInfo)

        #closing file
        myfile.close()

        #opening file again to create graph, not in append mode this time
        with open("c:\\Users\\andhar5173\\Desktop\\PerformanceAssessment5_5DataFile.csv") as mynewfile:

            #creating reader object and specifying 'age' and 'grade' rows for x and y axis
            reader = csv.reader(mynewfile)
            for row in reader:
                x.append(row[2])
                y.append(row[4])

            
            #creating plot w/ label 
            plt.plot(x,y, label="Loaded from Performance Assessment Data File")
            plt.xlabel=("age") #labeling x axis
            plt.ylabel=("grade") #labeling y axis
            plt.title=("Grades by age") #title of plot
            plt.legend() #showing plot legend
            plt.show() #showing plot



   
        
        



