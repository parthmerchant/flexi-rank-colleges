from tkinter import *
from tkinterhtml import HtmlFrame
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

argv = sys.argv
Logo= "resources/FlexiRankLogo.png"
QButton= "resources/QButton.png"
Plots= "resources/plot.png"
Ranks="resources/ranks.html"

def ranking(attribute, data):
    if attribute == "0":
        satSort = data.sort_values('SAT_AVG', ascending=False)
        satRank = satSort[['INSTNM','SAT_AVG','ADM_RATE','COSTT4_A']]
        newSAT = satRank.head(20)
        return newSAT
    elif attribute == "1":
        admSort = data.sort_values('ADM_RATE', ascending=True)
        admSortTwo = admSort[admSort.ADM_RATE > 0.0]
        admRank = admSortTwo[['INSTNM','SAT_AVG','ADM_RATE','COSTT4_A']]
        newADM = admRank.head(20)
        return newADM
    elif attribute == "2":
        costSort = data.sort_values('COSTT4_A', ascending=False)
        costRank = costSort[['INSTNM','SAT_AVG','ADM_RATE','COSTT4_A']]
        newCost = costRank.head(20)
        return newCost


def chart(df, attribute, year):
    if attribute == "0":
        col = 'SAT_AVG'
        ytit = 'SAT Scores'
    elif attribute == "1":
        col = 'ADM_RATE'
        ytit = 'Admission Rate'
    elif attribute == "2":
        col = 'COSTT4_A'
        ytit = 'Cost of Attendence'

    if attribute == "0":
        maxi = df[col].max()
        maxY = 1600
        mini = df[col].min()
        minY = mini * 0.8
    elif attribute == "1":
        maxi = df[col].max()
        maxY = maxi * 1.3
        mini = df[col].min()
        minY = mini * 0.7
    elif attribute == "2":
        maxi = df[col].max()
        maxY = maxi * 1.05
        mini = df[col].min()
        minY = mini * 0.9
    stepVal = (maxY - minY)/16

    x = df['INSTNM']
    y_pos = np.arange(len(x))
    y = df[col]
    # Create Bar Chart
    plt.bar(y_pos, y, align='center', alpha=0.5)
    # Format X-axis
    plt.xticks(y_pos, x, fontsize=5, rotation=90)
    plt.yticks(np.arange(minY, maxY, step=stepVal))
    plt.ylim(minY,maxY)
    # Create Y-axis Label
    plt.ylabel(ytit)
    #Create title for data visualization
    plt.title(year+' '+ytit)
    #Display data visualization
    #plt.show()
    plt.savefig(Plots, bbox_inches='tight')


def main():
        fName = argv[1]
        #fName = 'FilteredData.csv'
        attribute = argv[2]
        year = argv[3]

        fPath = 'data/'
        file = fPath + fName
        filteredData = pd.read_csv(file, index_col=0, low_memory=False)

        ranks = ranking(attribute, filteredData)
        chart(ranks, attribute, year)

        master = Toplevel()
        master.title("FlexiRank Colleges")

# ####### Header
        logo_img = PhotoImage(file=Logo)
        frc_label = Label(master, image=logo_img)
        frc_label.grid(row=0, column=0, columnspan=5)

        btn_img = PhotoImage(file=QButton)
        q_btn = Button(master, image=btn_img)
        q_btn.grid(row=0, column=5, columnspan=1)

# ####### CHART
        plot_img = PhotoImage(file=Plots)
        plot = Label(master, image=plot_img)
        plot.grid(row=1, column=0, columnspan=6)

# ####### TABLE
        html_frame = HtmlFrame(master, horizontal_scrollbar='auto')
        html_frame.grid(row=2, column=1, columnspan=5)

#########
        ranks.to_html(Ranks)
        html_data = open(Ranks).read()
        html_frame.set_content(html_data)
#########
        #filtData = pd.read_csv('data/FilteredData.csv', index_col=0, low_memory=False)
        #rankss = filtData.head(20)
        #rankss.to_html('resources/ranks.html', classes='table table-borderless')
        #html_data = open('resources/ranks.html').read()
        #html_frame.set_content(html_data)
#########

        master.mainloop()


main()
