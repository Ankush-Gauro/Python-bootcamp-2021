import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import plotly.plotly as pl
import plotly.offline as of
import cufflinks as cf
import datetime as dt
import datetime as dt
%matplotlib inline

of.init_notebook_mode(connected = True)
cf.go_offline()

donations = pd.read_csv('Donations.csv')
donors = pd.read_csv('Donors.csv')
projects = pd.read_csv('Projects.csv')
resources = pd.read_csv('Resources.csv')
schools = pd.read_csv('Schools.csv')
teachers = pd.read_csv('Teachers.csv')

print('Shape of Donation dataframe is:', donations.shape)
donations.head()
donations.describe()
print('Shape of Donors dataframe is:', donors.shape)
donors.head()
donors.describe()
print('Shape of Projects dataframe is:', projects.shape)
projects.head()
projects.describe()
print('Shape of Resources dataframe is:', resources.shape)
resources.head()
resources.describe()
print('Shape of Schools dataframe is:', schools.shape)
schools.head()
schools.describe()
print('Shape of Teachers dataframe is:', teachers.shape)
teachers.head()
teachers.describe()

data = pd.merge(donations, projects, how='inner', on='Project ID')
data2 = pd.merge(data, donors, how='inner', on='Donor ID')
data3 = pd.merge(data2, schools, how='inner', on='School ID')
data4 = pd.merge(data3, teachers, how='inner', on='Teacher ID')
data4.head()
a = data4.columns.values.tolist()

print("Q-1:Which 10 states have the most number of schools that opened projects to gather donations? Plot using bar plt.")
s = schools['School State'].value_counts().sort_values(ascending = False).head(10)
s
s.iplot(kind='bar', xTitle='States', yTitle='Number of schools', title='Number of schools involved in projests by states')

print('Q-2:What are the top 10 states in which schools gathered most amount of AVERAGE donations for their projects?')
s2 = data4.groupby('School State')['Donation Amount'].mean().sort_values(ascending=False).head(10)
s2.iplot(kind='bar', xTitle='State', yTitle='Average donation per project', title='Top 10 states(with max donation)', colorscale='paired')

print("Q-3:Analysis the maximum, minimum, mean, median and 25 and 75% percentiles of Donations?")
mean = np.mean(data4['Donation Amount'].dropna())
median = np.median(data4['Donation Amount'].dropna())
percentiles = np.percentiles(data4['Donation Amount'].dropna(),[25,75])
minimum = data4['Donation Amount'].dropna().min()
maximum = data4['Donation Amount'].dropna().max()
print('Max donation amount:', maximum)
print('Min donation amount:', minimum)
print('Mean donation amount:', np.round(mean, 2))
print('Median donation amount:', np.round(median, 2))
print('25 and 75 percentile donation amount:', percentiles)

print("We can immediately observe from above statistics that our Donations Amount column have lots of outliers since mean is 60 whereas median is 25 which shows that there are plenty of outliers causing mean to rise, second indicator is that we have 25th and 75th percentiles both below than mean. In other words although %75 percent of our data smaller than 50 we have a mean values which is 60.66 which is also a good indicator of outliers. Lastly we can easily say that maximum value is a huge outlier too.")

print("Q-4:In which percent the data has points greater or smaller than the values shown in the x-axis?")
x = np.sort(data4['Donation Amount'].dropna())
y = np.arange(l, len(x)+1)/len(x)
plt.plot(x,y,marker='.')

print("Q-5:In which states there are more donations done by donors?")
s3 = data4.groupby('Donor State')['Donation ID'].count().sort_values(ascending = False).head(10)
se.iplot(kind='bar', xTitle='state', yTitle='Number of donations', title='Donations count', colorscale ='paired')

print("Q-6:Now, it is time for a more advanced question ? Is there a relationship between the number of projects offered and number of donations made by the donors. Which states performing better in this case ? How many of them responding project requests below average and which states are performing best in terms of donations per project ? In order to answer this question we must first get the number of projects per state and then number of donations made per state. Then we should merge this two and plot a scatter plot to visualize it . Lets do it !")
s4 = schools['School state'].value_counts()
s5 = data4.groupby('Donor State')['Donation ID'].count()
df = pd.concat([s4,s5],axis=1,keys=['Projects','Donations'])
df = df.dropna()
df.head()
df.iplot(kind='scatter', xTitle='Projects', yTitle='Donations', title='Projects v/s donations', symbol='x', colorscale='paired',mode='markers')

print("Q-7:Fit a linear model which will basically indicate the relationship between projects and donations.")
slope, intercept = np.polyfit(df.Projects, df.Donations, 1)
x = np.array([df.Projects.min().df.Projects.max()])
y = slope * x + intercept
plt.plot(x,y)

print("Q-8:Combine the plots.")
df.plot.scatter(x='Projects', y='Donations')
slope,intercept = np.polyfit(df.Projects,df.Donations,1)
x = np.array([df.Projects.min(),df.Projects.max()])
y = slope*x + intercept
plt.plot(x,y)
plt.tight_layout()
plt.margins(0.05)

print("Q-9:How many differernt project types exist? What is the total donation amount for each of them?")
data4.head(2)
s6 = data4['Project Type'].value_counts()
s6
s7 = data4.groupby('Project Type')['Donation Amount'].sum().astype(int)
s7
plt.subplot(2,1,1)
plt.pie(s6, startangle=90)
slt.subplot(2,1,2)
plt.pie(s7, startangle=90)
plt.tight_layout()
plt.margin(0.05)
fig = plt.gcf()
fig.set_size_inches(25, 15)

print("Q-10:How many project subject categories trees exist? Which one attracted most donations?")
data4['Project Subject Category Tree'].nunique()
s8 = data4.groupby('Project Subject Category Tree')['Donation Amount'].sum().astype(int).sort_values(ascending=False).head(10)
s8
s9 = s8/1000000
s9.iplot(kind='bar', xTitle='Project sub category', yTitle='Donation amount in millions', title='Donation amount by project subject', colorscale='paired')

print("Q-11:What is the mean time that takes a project to be fully funded after posted and how it varies between states ?")
data4[['Project Posted Date', '']].isnull().sum()
data4[['Project Posted Date', 'Project Fully Funded Date']].head()
data4['Project Posted Date'] = pd.to_datetime(data4['Project Posted Date'])
data4['Project Fully Funded Date'] = pd.to_datetime(data4['Project Fully Funded Date'])
data4['Funding Time'] = data4['Project Fully Funded Date'] - data4['Project Posted Date']
data4[['Funding Time','Project Posted Date' , 'Project Fully Funded Date']].head()
data4[['Funding Time','Project Posted Date' , 'Project Fully Funded Date']].isnull().sum()
data5 = data4[pd.notnull(data4['Funding Time'])]
data5[['Funding Time','Project Posted Date' , 'Project Fully Funded Date']].isnull().sum()
data5['Funding Time'] = data5['Funding Time'].dt.days
data5[['Funding Time','Project Posted Date' , 'Project Fully Funded Date']].head()
wrong_overall_mean_time = data5['Funding TIme'].mean()
wrong_overall_mean_time
overall_mean_time = data5.groupby('Project ID')['Funding Time'].mean()
output = overall_mean_time.mean()
output

#average funding time for each state
state_project_funding_time = data5.groupby(['School State', 'Project ID'])['Funding Time'].mean()
state_project_funding_time
states_average_project_funding_time = state_project_funding_time.groupby('School State').mean()
states_average_project_funding_time.round(0)

print("Q-12:Which states are the best and which are the worst performing in terms of this criteria(mean project fully funded time)?")
fast = states_average_project_funding_time.round(0)
fast[fast<32].sort_values().head(10)
fast_funding = fast[fast<32].sort_values().head(10)
fast_funding.iplot(kind='bar', xTitle='States', yTitle='fully funding time(in days)', title='states that fund projects earlier than other', colorscale='paired')

slow = states_average_project_funding_time.round(0)
slow[slow>32].sort_values(ascending=False).head(10)
slow_funding = slow[slow>32].sort_values(ascending=False).head(10)
slow_funding.iplot(kind='bar', xTitle='States', yTitle='fully funding time(in days)', title='states that fund projects later than other')
