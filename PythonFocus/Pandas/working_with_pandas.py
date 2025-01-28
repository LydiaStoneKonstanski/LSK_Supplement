# Before we analyze anything, we need to import pandas
# and load our data
import pandas as pd
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