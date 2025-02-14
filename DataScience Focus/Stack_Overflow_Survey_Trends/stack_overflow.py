import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('developer_dataset.csv', low_memory=False)

print(df.columns)
print(df.count())
print(df.describe())
print(df.dtypes)

# Are there columns that have more missing data than others?
# The count shows less data in YearsCodePro, ConvertedComp, and WorkWeekHrs.

# Which columns seem interesting? What insights would you want to gain from the data?
# ConvertedComp (compensation) has a mean of 125K but a median of 79K, suggesting right-skewed data with a few high earners pulling up the mean.
#It also has a wide range between min and max values.

# Are there columns that have potentially more sensitive data than others? How would that change our strategies in dealing with them?
#The Work Week Hrs has a lot of missing data.

#Looking for places with 60%+ missing data:
# maxRows = df['RespondentID'].count()
# print(f'% Missing Data: {(1 - df.count() / maxRows) * 100}')

# NEWJobHunt                82.800852
# NEWJobHuntResearch        83.200101
# NEWLearn                  78.215792
#^ These qualify
# df.drop(['NEWJobHunt', 'NEWJobHuntResearch', 'NEWLearn'], axis=1, inplace=True)

# df[['RespondentID','Country']].groupby('Country').count()
#
# missingData = df[['Employment','DevType']].isnull().groupby(df['Country']).sum().reset_index()
#
# A=sns.catplot(
#     data=missingData, kind="bar",
#     x="Country", y="Employment",
#     height = 6, aspect = 2)
# B=sns.catplot(
#     data=missingData, kind="bar",
#     x="Country", y="DevType",
#     height = 6, aspect = 2)
# plt.show()

'''There is not a substantial difference between the two plots, so theres not an egregious
difference. US and Germany have more missing data because they have more respondents.
The missing data for these two columns can be categorized as MCAR. This means we can safely 
delete the rows that have missing data in these columns! This is a prime example of where 
you can employ Pairwise Deletion to only delete rows that have missing data for either 
Employment or DevType:'''

empfig = sns.catplot(x="Country", col="Employment",
                data=df, kind="count",
                height=6, aspect=1.5);

# Focus on a few of the key developer types outlined in the Stack Overflow survey
devdf = df[['Country','DevType']]
devdf.loc[devdf['DevType'].str.contains('back-end'), 'BackEnd'] = True
devdf.loc[devdf['DevType'].str.contains('front-end'), 'FrontEnd'] = True
devdf.loc[devdf['DevType'].str.contains('full-stack'), 'FullStack'] = True
devdf.loc[devdf['DevType'].str.contains('mobile'), 'Mobile'] = True
devdf.loc[devdf['DevType'].str.contains('administrator'), 'Admin'] = True

devdf = devdf.melt(id_vars=['Country'],
    value_vars=['BackEnd','FrontEnd','FullStack','Mobile','Admin'],
    var_name='DevCat',
    value_name='DevFlag')

devdf.dropna(how='any', inplace=True)

devFig = sns.catplot(x="Country", col="DevCat",
                data=devdf, kind="count",
                height=6, aspect=1.5);

df.dropna(subset = ['Employment', 'DevType'], inplace=True, how='any')

missingUndergrad = df['UndergradMajor'].isnull().groupby(df['Year']).sum().reset_index()

sns.catplot(x="Year", y="UndergradMajor",
                data=missingUndergrad, kind="bar",
                height=4, aspect=1);
plt.show()
#2020 has no missing data, so all the 2020 respondants had made major decisions.

# Sort by ID and Year so that each person's data is carried backwards correctly
df = df.sort_values(['RespondentID','Year'])

df['UndergradMajor'].bfill(axis=0, inplace=True)

# Key major groups outlined in the Stack Overflow survey
majors = ['social science','natural science','computer science','development','another engineering','never declared']

edudf = df[['Year','UndergradMajor']]
edudf.dropna(how='any', inplace=True)
edudf.loc[edudf['UndergradMajor'].str.contains('(?i)social science'), 'SocialScience'] = True
edudf.loc[edudf['UndergradMajor'].str.contains('(?i)natural science'), 'NaturalScience'] = True
edudf.loc[edudf['UndergradMajor'].str.contains('(?i)computer science'), 'ComSci'] = True
edudf.loc[edudf['UndergradMajor'].str.contains('(?i)development'), 'ComSci'] = True
edudf.loc[edudf['UndergradMajor'].str.contains('(?i)another engineering'), 'OtherEng'] = True
edudf.loc[edudf['UndergradMajor'].str.contains('(?i)never declared'), 'NoMajor'] = True

edudf = edudf.melt(id_vars=['Year'],
    value_vars=['SocialScience','NaturalScience','ComSci','OtherEng','NoMajor'],
    var_name='EduCat',
    value_name='EduFlag')

edudf.dropna(how='any', inplace=True)
edudf = edudf.groupby(['Year','EduCat']).count().reset_index()

eduFig = sns.catplot(x="Year", y='EduFlag', col="EduCat",
                data=edudf, kind="bar",
                height=6, aspect=1.5);
plt.show()

'''You notice that the vast majority of people who enter the workforce for development 
have some background in a Computer Science major. Interestingly, however, the number 
of Computer Science majors significantly declined over the years surveyed, indicating 
that there could be other majors that have successfully entered the workforce for their 
desired job. This would require further analysis and could allow an individual to 
pursue a separate education path and still end up in some kind of developer role.'''

'''Examine the relationship between years of experience and compensation
At this point, you have studied the demographics of developers around the world, 
from where they live to the education paths they have taken. Now, you turn your 
focus to the various aspects that would influence the job-hunting process.

Years of experience are an important metric when looking to understand the general 
skill and technical capabilities of a potential candidate. Compensation is also important 
for our client to understand what the “going rate” for a particular developer is in today’s 
market. You might assume that there is a strong correlation between experience and job 
compensation, making it an excellent hypothesis to explore.

In order to understand a bit about the data for each of these two fields, perform some 
more exploratory analysis:'''

compFields = df[['Year','YearsCodePro','ConvertedComp']]

D = sns.boxplot(x="Year", y="YearsCodePro",
            data=compFields)

E = sns.boxplot(x="Year", y="ConvertedComp",
            data=compFields)
plt.show()

'''You see that although there are some outlier data points for each column, 
the overall distribution is fairly consistent year-over-year. This indicates 
that there is a strong correlation between the data points, which should tell a 
good story about how experience can translate into compensation. Since there is a 
clear trend with the data points, you decide the best method for filling in the 
missing data for these two columns is through Multiple Imputation:'''
import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.model_selection import train_test_split

imputedf = df[['YearsCodePro','ConvertedComp']]

traindf, testdf = train_test_split(imputedf, train_size=0.1)

# Create the IterativeImputer model to predict missing values
imp = IterativeImputer(max_iter=20, random_state=0)

# Fit the model to the the test dataset
imp.fit(imputedf)

# Transform the model on the entire dataset
compdf = pd.DataFrame(np.round(imp.transform(imputedf),0),
                      columns=['YearsCodePro','ConvertedComp'])
'''The above code will loop through (up to 20 times), and fill in the missing data 
based on the context provided by the other column. This should create data points 
that are indicative of the overall trend of the data. Now, you can analyze the 
relationship between YearsCodePro and CinvertedComp through the use of a boxplot 
like so:'''

compPlotdf = compdf.loc[compdf['ConvertedComp'] <= 150000]
compPlotdf['CodeYearBins'] = pd.qcut(compPlotdf['YearsCodePro'], q=5)

sns.boxplot(x="CodeYearBins", y="ConvertedComp",
            data=compPlotdf)
plt.show()

'''The plot above validates your hypothesis from before. While there are high (and low) 
earning developers at every experience level, experience appears to correlate with 
compensation. The more experienced a developer was, the more (on average) they were 
compensated.'''

'''At this point, we have analyzed information about the developer community from a 
variety of points of view. Our client understands the global presence of the developer 
community, their varied backgrounds, and how their experience translates into compensation. 
Overall, these statistical analyses can guide actions in moving forward with a staffing 
plan that aligns with your client’s growth plan and technical requirements.

By using a variety of techniques for handling missing data, you were able to reliably 
curate a cleaner dataset to fuel this set of analyses. These strategies allow you to 
salvage otherwise messy data, and should help you in the future with other datasets.'''