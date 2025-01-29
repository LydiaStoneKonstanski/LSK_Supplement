# Before we analyze anything, we need to import pandas
# and load our data

'''Shoefly Using statistical analysis'''
# import pandas as pd
# orders = pd.read_csv('orders.csv')
# # print(orders.head(10))
# most_expensive = orders.price.max()
# print(most_expensive)# $493.00
# num_colors = orders.shoe_color.nunique()
# print(num_colors) #5

'''Grouping more than 1 column'''
# pricey_shoes = orders.groupby('shoe_type').price.max()
# print(pricey_shoes)
# print(type(pricey_shoes))

'''Grouping by more than one column using lambdas'''
# import codecademylib3
# import numpy as np
# import pandas as pd
#
# orders = pd.read_csv('orders.csv')
#
# cheap_shoes = orders.groupby('shoe_color').price.apply(lambda x: np.percentile(x, 25)).reset_index()
# print(cheap_shoes)


# df = pd.read_csv('shoefly_page_visits.csv')
# df.head(10)
# # This command shows us how many users visited the site from different sources in different months.
# df.groupby(['month', 'utm_source']).id.count().reset_index()
# # This command shows us how many users visited the site from different sources in different months.
# df.groupby(['month', 'utm_source']).id.count()\
#     .reset_index()\
#     .pivot(columns='month', index='utm_source', values='id')

