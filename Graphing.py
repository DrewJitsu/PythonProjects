'''
Andrew Harris
Graphing
'''

from matplotlib import pyplot as plt
import csv

x=[]
y=[]

with open("c:\\Users\\andhar5173\\Desktop\\Excel Sheet.csv")as myfile:

    reader=csv.reader(myfile)
    for row in reader:
        try:
            x.append(row[3])
            y.append(float(row[11])*100)
        except:
            y.append(80)

    plt.ylim(50,90)
    plt.plot(x,y, label="Loaded from example.csv")
    plt.xlabel("county")
    plt.ylabel("vote %")
    plt.title("Voting percentage by precinct in Fairfax county")
    plt.legend()
    plt.show()

