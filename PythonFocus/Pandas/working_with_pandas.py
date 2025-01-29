# Before we analyze anything, we need to import pandas
# and load our data
# import pandas as pd
import string

# df = pd.read_csv('shoefly_messy_orders.csv')
#
# df.head(10)
#
# df['shoe_type'] = df.shoe_type.apply(string.lower)
#
# df.head(10)
#
# df['in_stock'] = df.shoe_material.apply(lambda x: False if x == 'fabric' else True)
#
# df.head(10)
#
# df['description'] = df.apply(lambda row: "{} {} bought {} {} {}"\
#     .format(row.first_name,
#             row.last_name,
#             row.shoe_color,
#             row.shoe_material,
#             row.shoe_type),
#     axis=1)
# df.head(10)

'''Adding a column

One way is by providing a list of the length of the df: 

df['Quantity'] = [100, 150, 50, 35]'''

# import codecademylib3
# import pandas as pd
#
# df = pd.DataFrame([
#   [1, '3 inch screw', 0.5, 0.75],
#   [2, '2 inch nail', 0.10, 0.25],
#   [3, 'hammer', 3.00, 5.50],
#   [4, 'screwdriver', 2.50, 3.00]
# ],
#   columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
# )
#
# df['Sold in Bulk?'] = ['Yes', 'Yes', 'No', 'No']

'''We can also add a new column that is the same for all rows in the DataFrame: 
df['In Stock?'] = True
'''

# import codecademylib3
# import pandas as pd
#
# df = pd.DataFrame([
#   [1, '3 inch screw', 0.5, 0.75],
#   [2, '2 inch nail', 0.10, 0.25],
#   [3, 'hammer', 3.00, 5.50],
#   [4, 'screwdriver', 2.50, 3.00]
# ],
#   columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
# )
#
# df['Is taxed?'] = 'Yes'
#
# print(df)


'''Finally, you can add a new column by performing a function on the existing columns.
df['Sales Tax'] = df.Price * 0.075
'''

# df = pd.DataFrame([
#   [1, '3 inch screw', 0.5, 0.75],
#   [2, '2 inch nail', 0.10, 0.25],
#   [3, 'hammer', 3.00, 5.50],
#   [4, 'screwdriver', 2.50, 3.00]
# ],
#   columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
# )
# #Every column name goes in brackets AND quotes
# df['Margin'] = df['Price'] - df['Cost to Manufacture']

'''COLUMN OPERATIONS with .apply
Use .apply to perform an operation on every line of the column chosen.'''
# df = pd.DataFrame([
#   ['JOHN SMITH', 'john.smith@gmail.com'],
#   ['Jane Doe', 'jdoe@yahoo.com'],
#   ['joe schmo', 'joeschmo@hotmail.com']
# ],
# columns=['Name', 'Email'])
#
# df['Lowercase Name'] = df.Name.apply(str.lower)
#
# print(df)

'''Lambda to split'''
# df['Email Provider'] = df.Email.apply(
#     lambda x: x.split('@')[-1]
#     )

'''Applying a lambda to a column'''
# df = pd.read_csv('employees.csv')
#
# get_last_name = lambda x: x.split(' ')[-1]
# df['last_name'] = df.name.apply(get_last_name)
# print(df)

#OR
# df['last_name'] = df.name.apply(lambda x: x.split(' ')[-1])

'''Applying a lambda to a row use axis=1
Say we want to add in the price with tax for each line, we’ll need to look at two columns: 
Price and Is taxed?.
If Is taxed? is Yes, then we’ll want to multiply Price by 1.075 (for 7.5% sales tax).
If Is taxed? is No, we’ll just have Price without multiplying it.
We can create this column using a lambda function and the keyword axis=1:'''
# df['Price with Tax'] = df.apply(lambda row:
#      row['Price'] * 1.075
#      if row['Is taxed?'] == 'Yes'
#      else row['Price'],
#      axis=1
# )

'''Calculating overtime (I got it wrong the first time. Wrong parenthesis)'''
# df = pd.read_csv('employees.csv')
#
# total_earned = lambda row : (row.hourly_wage * row.hours_worked) if row.hours_worked <= 40 else (40 * row.hourly_wage + (row.hours_worked - 40) * row.hourly_wage * 1.5)
#
# df['total_earned'] = df.apply(total_earned, axis=1)
#
# print(df)

#OR

#df['total_earned'] = df.apply(lambda row : (row.hourly_wage * row.hours_worked) if row.hours_worked <= 40 else (40 * row.hourly_wage + (row.hours_worked - 40) * row.hourly_wage * 1.5), axis=1)


'''Renaming columns enmasse: df.columns['name1', 'name2', etc]
df = pd.DataFrame({
    'name': ['John', 'Jane', 'Sue', 'Fred'],
    'age': [23, 29, 21, 18]
})
df.columns = ['First Name', 'Age']'''

# df = pd.read_csv('imdb.csv')
# df.columns = ['ID', 'Title', 'Category', 'Year Released', 'Rating']
# print(df)

'''Or rename columns specifically: 
df.rename(columns={
    'name': 'First Name',
    'age': 'Age'},
    inplace=True)
    
So you are passing in a dictionary providing the old column name as key, and new name as value.'''
# df = pd.read_csv('imdb.csv')
# df.rename(columns={'name': 'movie_title'}, inplace=True)
# print(df)

'''This is ordered in a one-shot way that makes much more sense'''
orders = pd.read_csv('shoefly.csv')
print(orders.head())
orders['shoe_source'] = orders.shoe_material.apply(lambda x:'animal' if x == 'leather' else 'vegan')
orders['salutation'] = orders.apply(lambda row:'Dear Mr. ' + row['last_name'] if row['gender'] == 'male' else 'Dear Ms. ' + row['last_name'], axis=1)

'''Petal Power Project'''
# import codecademylib3
# import pandas as pd
# inventory = pd.read_csv('inventory.csv')
# #print(inventory.head(10))
#
# staten_island = inventory.iloc[0:10]
# # print(staten_island)
#
# product_request = staten_island[['product_description', 'price']]
# # print(product_request)
#  '''Uses multiple filtering options at once'''
# seed_request = inventory.loc[(inventory.location == 'Brooklyn') & (inventory.product_type == 'seeds')]
# # print(seed_request)
#
# inventory['in_stock']= inventory.apply(lambda row : 'True' if row['quantity'] > 0 else 'False', axis=1)
# # print(inventory.head(10))
#
# inventory['total_value'] = inventory.apply (lambda row : row['price']*row['quantity'], axis=1)
# #print(inventory.head(10))
#
# combine_lambda = lambda row: '{} - {}'.format(row.product_type, row.product_description)
#
# inventory['full-description']= inventory.apply(combine_lambda, axis=1)
# print(inventory.head(10))

'''PIVOT TABLES'''
# orders = pd.read_csv('orders.csv')
# print(orders.head())
#
# shoe_counts = orders.groupby(['shoe_type', 'shoe_color']).id.count().reset_index()
#
# shoe_counts_pivot = shoe_counts.pivot(columns='shoe_color', index='shoe_type', values='id').reset_index()
# print(shoe_counts_pivot)

# import codecademylib3
# import pandas as pd
#
# user_visits = pd.read_csv('page_visits.csv')
#
# print(user_visits.head())
#
# click_source = user_visits.groupby('utm_source').id.count().reset_index()
# # print(click_source)
#
# click_source_by_month = user_visits.groupby(['utm_source', 'month']).id.count().reset_index()
# # print(click_source_by_month)
#
# click_source_by_month_pivot = click_source_by_month.pivot(columns='month', index='utm_source', values='id').reset_index()
# print(click_source_by_month_pivot)

'''AB Testing Project. Not sure if it is right'''
# import codecademylib3
# import pandas as pd
#
# ad_clicks = pd.read_csv('ad_clicks.csv')
# # print(ad_clicks.head())
#
# source = ad_clicks.groupby('utm_source').user_id.count().reset_index()
# #print(source)
#
# ad_clicks['is_click'] = ad_clicks.ad_click_timestamp.apply(lambda x: True if pd.notna(x) else False)
# #print(ad_clicks.head())
#
# clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click'])['user_id'].count().reset_index()
# # print(clicks_by_source)
#
# clicks_pivot= clicks_by_source.pivot(
#   columns='is_click',
#   index='utm_source',
#   values='user_id'
# ).reset_index()
# # print(clicks_pivot)
#
# clicks_pivot['percent_clicked'] = clicks_pivot[True]/(clicks_pivot[True] + clicks_pivot[False])
# #print(clicks_pivot)
#
# # group_counts = ad_clicks[ad_clicks.experimental_group == 'A'].count()
#
# group_counts = ad_clicks.groupby('experimental_group')['user_id'].count().reset_index()
# #print(group_counts)
#
# which_ad = ad_clicks.groupby(['experimental_group','is_click'])['user_id'].count().reset_index()
# #print(which_ad)
#
# which_ad_pivot = which_ad.pivot(
#   columns='experimental_group',
#   index='user_id',
#   values='is_click'
# ).reset_index()
# #print(which_ad_pivot)
#
# total_users = ad_clicks.user_id.nunique() #1654
#
# users_a = ad_clicks.loc[(ad_clicks['is_click'] == True) & (ad_clicks['experimental_group'] == 'A')].reset_index(drop=True)
# #print(users_a.head())
#
# users_b = ad_clicks.loc[(ad_clicks['is_click'] == True) & (ad_clicks['experimental_group'] == 'B')].reset_index(drop=True)
#
# #print(users_b.head())
#
# percent_users_a = users_a.count()/total_users
# # print(percent_users_a) #0.18742442563482467
#
# percent_users_b = users_b.count()/total_users
# # print(percent_users_b) #0.15417170495767835
#
# # users_a['percent_clicks']=users_a.groupby(['is_click',
# #   'day'])['user_id'].reset_index()
# # print(users_a.head())
#
# users_a['percent_clicks'] = (
#     users_a.groupby('day')['user_id'].transform(lambda x: x.count() / users_a['user_id'].count())
# )
# users_a_pivot= users_a.pivot(
#   columns = 'day',
#   index='user_id',
#   values='percent_clicks'
# )
# print(users_a_pivot)
#
# users_b['percent_clicks'] = (
#     users_b.groupby('day')['user_id'].transform(lambda x: x.count() / users_b['user_id'].count())
# )
#
# users_b_pivot= users_b.pivot(
#   columns = 'day',
#   index='user_id',
#   values='percent_clicks'
# )
# print(users_b_pivot)

# sales = pd.read_csv('sales.csv')
# print(sales)
# targets = pd.read_csv('targets.csv')
# print(targets)
# men_women = pd.read_csv('men_women_sales.csv')
# print(men_women)
#
# all_data = sales.merge(targets).merge(men_women)
# print(all_data)
## searching for several things:
# results = all_data.loc[(all_data.revenue > all_data.target)&(all_data.women > all_data.men)]
# print(results)