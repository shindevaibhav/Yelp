import pandas as pd
df1 = pd.read_csv("yelp_csv_1.csv")
df2 = pd.read_csv("yelp_csv_2.csv")
df3 = pd.read_csv("yelp_csv_3.csv")

l1 = df1.loc[(df1["useful"] > 0) | (df1["funny"] > 0) | (df1["cool"] > 0)]
l1 = l1.reset_index(drop=True)
l2 = df2.loc[(df2["useful"] > 0) | (df2["funny"] > 0) | (df2["cool"] > 0)]
l2 = l2.reset_index(drop=True)
l3 = df3.loc[(df3["useful"] > 0) | (df3["funny"] > 0) | (df3["cool"] > 0)]
l3 = l3.reset_index(drop=True)
'''
len(l1.loc[l1["useful"] > 0])
len(l1.loc[l1["funny"] > 0])
len(l1.loc[l1["cool"] > 0])
len(l2.loc[l2["useful"] > 0])
len(l2.loc[l2["funny"] > 0])
len(l2.loc[l2["cool"] > 0])
len(l3.loc[l3["useful"] > 0])
len(l3.loc[l3["funny"] > 0])
len(l3.loc[l3["cool"] > 0])
'''
headers = ["text","useful","cool","funny"]
l1 =l1[headers]
l2 =l2[headers]
l3 =l3[headers]

l1.to_csv("data/mr/labeled_yelp_data_1.csv",index=False)
l2.to_csv("data/mr/labeled_yelp_data_2.csv",index=False)
l3.to_csv("data/mr/labeled_yelp_data_3.csv",index=False)

result = pd.concat([l1,l2,l3])
result.to_csv("data/mr/labeled_yelp_data_complete.csv",index=False)
