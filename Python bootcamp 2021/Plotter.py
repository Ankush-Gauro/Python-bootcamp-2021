import chart_studio.plotly as pl
import numpy as np
import pandas as pd
#import plotly.plotly as pl
import plotly.offline as po
import cufflinks as cf

po.init_notebook_mode(connected = True)
cf.go_offline()

def create_data(data):
    if(data == 1):
        x = np.random.rand(100,5)
        df1 = pd.DataFrame(x,columns=['A','B','C','D','E'])
    elif(data == 2):
        x = [0,0,0,0,0]
        r1= [0,0,0,0,0]
        r2= [0,0,0,0,0]
        r3= [0,0,0,0,0]
        r4= [0,0,0,0,0]
        print('Enter the values for columns:')
        i=0
        for i in [0,1,2,3,4]:
            x[i] = input()
            i = i + 1
        print('Enter values for first row:')
        i=0
        for i in [0,1,2,3,4]:
            r1[i] = int(input())
            i = i + 1
        print('Enter values for second row:')
        i=0
        for i in [0,1,2,3,4]:
            r2[i] = int(input())
            i = i + 1
        print('Enter values for third row:')
        i=0
        for i in [0,1,2,3,4]:
            r3[i] = int(input())
            i = i + 1
        print('Enter values for fourth row:')
        i=0
        for i in [0,1,2,3,4]:
            r4[i] = int(input())
            i = i + 1
        df1 = pd.DataFrame([r1,r2,r3,r4] , columns = x)
    elif(data == 3):
        File = input('Enter the file name:')
        x = pd.read_csv(File)
        df1 = pd.DataFrame(x)
    
    else:
        print("DataFrame creation failed!")
    return df1

def plotter(plot):
    if (plot == 1):
        finalplot = df1.iplot(kind ='scatter')
    if (plot == 2):
        finalplot = df1.iplot(kind ='scatter', mode ='markers', symbol='x', colorscale='paired')
    if (plot == 3):
        finalplot = df1.iplot(kind = 'bar')
    if (plot == 4):
        finalplot = df1.iplot(kind = 'hist')
    if (plot == 5):
        finalplot = df1.iplot(kind = 'box')
    if (plot == 6):
        finalplot = df1.iplot(kind = 'surface')
    else:
        finalplot = print("Enter valid character!")
    return finalplot

def plotter2(plot):
    col = input("Enter the number of columns you want to plot by selecting only 1, 2, or 3:")
    con = int(col)
    if (col ==1):
        colm = input("Enter the column you want to plot from dataframe head:")
        if (plot == 1):
            finalplot = df1[colm].iplot(kind ='scatter')
        elif (plot == 2):
            finalplot = df1[colm].iplot(kind ='scatter', mode ='markers', symbol='x', colorscale='paired')
        elif (plot == 3):
            finalplot = df1[colm].iplot(kind ='bar')
        elif (plot == 4):
            finalplot = df1[colm].iplot(kind ='hist')
        elif (plot == 5):
            finalplot = df1[colm].iplot(kind ='box')
        elif (plot == 6 or plot == 7):
            finalplot = print("Bubble and surface plot require more than one column arguments!")
        else:
            print("Invalid character!")
    elif (col == 2):
        print('Enter the columns you want to plot from dataframe head:')
        x = input('First column:')
        y = input('Second column:')
        if (plot == 1):
            finalplot = df1[[x,y]].iplot(kind ='scatter')
        elif (plot == 2):
            finalplot = df1[[x,y]].iplot(kind ='scatter', mode ='markers', symbol='x', colorscale='paired')
        elif (plot == 3):
            finalplot = df1[[x,y]].iplot(kind ='bar')
        elif (plot == 4):
            finalplot = df1[[x,y]].iplot(kind ='hist')
        elif (plot == 5):
            finalplot = df1[[x,y]].iplot(kind ='box')
        elif (plot == 6):
            finalplot = df1[[x,y]].iplot(kind ='surface')
        elif (plot == 7):
            size = input("Enter the size column for bubble plot:")
            finalplot = df1[[x,y]].iplot(kind ='bubble', x=x, y=y,size=size)
        else:
            finalplot = print('Enter valid character!')
    elif (col == 3):
        print('Enter the columns you want to plot from dataframe head:')
        x = input('First column:')
        y = input('Second column:')
        z = input('Third clolumn:')
        if (plot == 1):
            finalplot = df1[[x,y,z]].iplot(kind ='scatter')
        elif (plot == 2):
            finalplot = df1[[x,y,z]].iplot(kind ='scatter', mode ='markers', symbol='x', colorscale='paired')
        elif (plot == 3):
            finalplot = df1[[x,y,z]].iplot(kind ='bar')
        elif (plot == 4):
            finalplot = df1[[x,y,z]].iplot(kind ='hist')
        elif (plot == 5):
            finalplot = df1[[x,y,z]].iplot(kind ='box')
        elif (plot == 6):
            finalplot = df1[[x,y,z]].iplot(kind ='surface')
        elif (plot == 7):
            size = input("Enter the size column for bubble plot:")
            finalplot = df1.iplot(kind ='bubble', x=x, y=y,z=z,size=size)
        else:
            finalplot = print('Enter valid character!') 
    else:
        finalplot = print('Enter valid character!')
    return finalplot

def main(cat):
    if (cat == 1):
        print("Select the type of plot you need to plot:")
        print("Press 1 for Line Plot:")
        print("Press 2 for Scatter Plot:")
        print("Press 3 for Bar Plot:")
        print("Press 4 for Histogram:")
        print("Press 5 for Box Plot:")
        print("Press 6 for Surface Plot:")
        plot = int(input())
        output = plotter(plot)
    elif (cat == 2):
        print("Select the type of plot you need to plot by writting 1-7:")
        print("Press 1 for Line Plot:")
        print("Press 2 for Scatter Plot:")
        print("Press 3 for Bar Plot:")
        print("Press 4 for Histogram:")
        print("Press 5 for Box Plot:")
        print("Press 6 for Surface Plot:")
        print("Press 7 for Bubble Plot: ")
        plot = int(input())
        output = plotter2(plot)
    else:
        print("Please enter valid character!")
        
print("Select the type of data you need to plot:")
print("Enter (1) for random data with 100 rows and 5 columns:")
print("Enter (2) for customized dataframe with 5 columns and 4 rows:")
print("Enter (3) for uploading csv/json/txt file:")
data = int(input())
df1 = create_data(data)

print("Your DataFrame head is given below check the columns to plot using cufflinks!")
df1.head()

print("What kind of plot you need, the complete data plot or columns plot?")
cat = input('Press 1 for plotting all columns or press 2 for specifying columns to plot:')
cat = int(cat)
main(cat)

