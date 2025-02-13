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
df.drop(['NEWJobHunt', 'NEWJobHuntResearch', 'NEWLearn'], axis=1, inplace=True)


df[['RespondentID','Country']].groupby('Country').count()

missingData = df[['Employment','DevType']].isnull().groupby(df['Country']).sum().reset_index()

A=sns.catplot(
    data=missingData, kind="bar",
    x="Country", y="Employment",
    height = 6, aspect = 2)
B=sns.catplot(
    data=missingData, kind="bar",
    x="Country", y="DevType",
    height = 6, aspect = 2)
plt.show()

'''There is not a substantial difference between the two plots, so theres not an egregious
difference. US and Germany have more missing data because they have more respondents.
The missing data for these two columns can be categorized as MCAR. This means we can safely 
delete the rows that have missing data in these columns! This is a prime example of where 
you can employ Pairwise Deletion to only delete rows that have missing data for either 
Employment or DevType:'''


