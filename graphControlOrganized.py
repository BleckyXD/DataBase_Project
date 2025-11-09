import numpy as np #Array
import matplotlib.pyplot as plt #Plots
from matplotlib import cm  # Colormaps
import random #Colors
import time #Colors

#Declare function for the pie chart
def pieChart(x, y, z, mainTitle):
    #Repair the values
    z = z.reshape(len(x), len(y))
    z1 = z.sum(axis=1) #x
    z2 = z.sum(axis=0) #y

    #Give random colors to the slices
    colors = randomColors(len(x))

    #Give the explode to the highest value
    e1 = []
    for i in z1:
        if i == max(z1):
            e1.append(0.1)
        else:
            e1.append(0)
    e2 = []
    for i in z2:
        if i == max(z2):
            e2.append(0.1)
        else:
            e2.append(0)

    #Declare the details that the graph will visually have, including text
    visualDetails = {'edgecolor': 'white', 'linewidth': 2, 'linestyle': '--'}
    textprops = {'fontsize': 12, 'color': 'black', 'fontweight': 'bold'}


    #Create the subplots, so that we can show both pie charts, each next to eachother
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))

    # Change background colors
    fig.patch.set_facecolor("grey")

    #Call the first graph
    ax[0].pie(z1, autopct='%d%%', colors=colors, startangle=270, pctdistance=0.75, explode=e1,
              wedgeprops=visualDetails, textprops=textprops, shadow=True, radius=1)

    #Give the graph a legend
    ax[0].legend(labels=x, title="Legend", loc='upper left', bbox_to_anchor=(-0.1, 1.1))

    #Create more random colors
    colors = randomColors(len(y))

    #Call the second graph
    ax[1].pie(z2, autopct='%d%%', colors=colors, startangle=270, pctdistance=0.75, explode=e2,
              wedgeprops=visualDetails, textprops=textprops, shadow=True, radius=1)

    # Give the graph a legend
    ax[1].legend( labels=y, title="Legend", loc='upper right', bbox_to_anchor=(1, 1.1))

    #Set the title for the graphs
    plt.suptitle(mainTitle, fontsize=25, fontweight='bold')

    # Save the plot
    plt.savefig(mainTitle + ".png")

    plt.show()

#Declare function for the bar plot
def barPlot(x, y, z, xTitle, yTitle, zTitle, Title):

    #Repair the values
    z = z.reshape(len(x), len(y))
    z1 = z.sum(axis=1)
    z2 = z.sum(axis=0)

    #Create the subplots with 1 row and two columns, two plots next to each other
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))
    fig.patch.set_facecolor('#d8d8d8')  # background color

    #Give random colors
    colors = randomColors(len(x))

    #Call the bar chart
    ax[0].bar(x, z1, color=colors, edgecolor='black')

    #Set the labels in the axis
    ax[0].set_xlabel(xTitle)
    ax[0].set_ylabel(zTitle)

    #Give grid lines
    ax[0].grid(axis='y', linestyle='--', alpha=0.6)

    #Repeat for next bar plot
    colors = randomColors(len(x))
    ax[1].bar(y, z2, color= colors, edgecolor='black')
    ax[1].set_xlabel(yTitle)
    ax[1].set_ylabel(zTitle)
    ax[1].grid(axis='y', linestyle='--', alpha=0.6)

    #Give title to the graphs
    plt.suptitle(Title, fontsize=14, fontweight='bold')

    #Make sure nothing is overlapping
    plt.tight_layout()

    # Save the plot
    plt.savefig(Title + ".png")

    plt.show()

def scatter3D(x, y, z, xTitle, yTitle, zTitle, Title):

    #Declare the size of the figure
    fig = plt.figure(figsize=(10, 7))

    #Add the 3d subplot area, so we get 3 axes
    ax = fig.add_subplot(projection='3d')

    #Repair the x, y, and z values, so that the graph can use them
    xPosition = np.arange(len(x))
    yPosition = np.arange(len(y))
    xPosition, yPosition = np.meshgrid(xPosition, yPosition)

    #Flatten the values, so that they match when creating the bars
    xPosition = xPosition.flatten() - 0.5  # moves bars slightly right
    yPosition = yPosition.flatten() + 0.1  # moves bars slightly backward
    zPosition = z.flatten()

    #Used to convert the values of z in values between 0 and 1, so
    #that we can give them color based on their amount
    norm = plt.Normalize(z.min(), z.max())

    #Create the colormap for the graph, which will give a different
    #color, depending on the value
    colors = cm.jet(norm(zPosition))

    #Declare the amount of positions in each axis for the titles
    ax.set_yticks(np.arange(len(y)))
    ax.set_xticks(np.arange(len(x)))

    #Declare the labels of these positions
    ax.set_yticklabels(y, fontsize=10)
    ax.set_xticklabels(x, fontsize=10)

    #Declare the title label for the three axis
    ax.set_xlabel(xTitle, fontsize=11, labelpad=15)
    ax.set_ylabel(yTitle, fontsize=10, labelpad=15)
    ax.set_zlabel(zTitle, fontsize=10, labelpad=15)

    #Create the graph
    ax.scatter3D(xPosition, yPosition, zPosition,color=colors, s = 100)

    #Set the title
    ax.set_title(Title, fontsize=20, pad=15)

    #Save the plot
    plt.savefig(Title + ".png")

    plt.show()

def scatter(x, y, z, xTitle, yTitle, zTitle, Title):

    #Repair the values
    z = z.reshape(len(x), len(y))
    z1 = z.sum(axis=1)
    z2 = z.sum(axis=0)

    #Create the subplot, so we can output two scatter graphs
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))

    #Give it random colors
    colors = randomColors(len(x))

    #Create the graph
    ax[0].scatter(x, z1, color=colors, s=100)

    #Set it's labels
    ax[0].set_xlabel(xTitle)
    ax[0].set_ylabel(zTitle)

    #Give it grid lines
    ax[0].grid(axis='y', linestyle='--', alpha=0.6)

    #Repeat for second graph
    colors = randomColors(len(y))

    ax[1].scatter(y, z2, color=colors, s=100)
    ax[1].set_xlabel(yTitle)
    ax[1].set_ylabel(zTitle)
    ax[1].grid(axis='y', linestyle='--', alpha=0.6)

    #Give it a title
    plt.suptitle(Title, fontsize=20, fontweight='bold')

    # Save the plot
    plt.savefig(Title + ".png")

    plt.show()

def bar3D(x, y, z, xTitle, yTitle, zTitle, Title):

    #Declare the figure with a 3d space
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(projection='3d')

    # Declare the amount of positions in each axis for the titles
    xPosition = np.arange(len(x))
    yPosition = np.arange(len(y))

    #Create all the possible combinations
    #between x and y
    xPosition, yPosition = np.meshgrid(xPosition, yPosition)

    #Flatten the axis, so that they match
    #between each other
    xPosition = xPosition.flatten() - 0.5  # moves bars right
    yPosition = yPosition.flatten() + 0.1 # moves bars left

    #Starting position of the columns, 0
    zPosition = np.zeros_like(xPosition)

    #Flatten the values, so that they can be given to each one
    #of the coordinates we obtained from the meshgrid
    heights = z.flatten()

    #Size of the column width
    length = width = 0.4

    # Used to convert the values of z in values between 0 and 1, so
    # that we can give them color based on their amount
    norm = plt.Normalize(z.min(), z.max())

    # Create the colormap for the graph, which will give a different
    # color, depending on the value
    colors = cm.jet(norm(heights))

    #Create the graph
    ax.bar3d(xPosition, yPosition, zPosition, length, width, heights, color=colors, shade=True)

    #Set the positions where the labels go
    ax.set_yticks(np.arange(len(y)))
    ax.set_xticks(np.arange(len(x)))

    #Set the labels in each one of the positions
    ax.set_yticklabels(y, fontsize=10)
    ax.set_xticklabels(x, fontsize=10)

    #Set the title labels for the axes
    ax.set_xlabel(xTitle, fontsize=10, labelpad=15)
    ax.set_ylabel(yTitle, fontsize=10, labelpad=15)


    #Set the title of the graph
    ax.set_title(Title, fontsize=20, pad=15)

    #Set the color bar
    mappable = cm.ScalarMappable(cmap='jet', norm=norm)
    mappable.set_array(heights)
    cbar = plt.colorbar(mappable, ax=ax, shrink=0.6, pad=0.1)
    cbar.set_label(zTitle)

    #Set the angle of the graph
    ax.view_init(elev=25, azim=120)

    # Save the plot
    plt.savefig(Title + ".png")

    plt.show()

#Function for declaring random colors
def randomColors(n):
    random.seed(time.time())
    colors = []
    for i in range(n):
        colors.append((random.random(), random.random(), random.random()))
    return colors