import pandas as pd
data1 = pd.read_csv('./data/daily_sales_data_0.csv')
data2 = pd.read_csv('./data/daily_sales_data_1.csv')
data3 = pd.read_csv('./data/daily_sales_data_2.csv')
data = data1.append(data2).append(data3)
data = data[data["product"] == "pink morsel"]
data["sales"] = data['price'].str[1:].astype('float')*data["quantity"]
data.to_csv('output.csv',columns=['sales','date','region'],index=False)