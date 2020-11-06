#Task 1.1
import pandas as pd
#defining the required sheets in the list
sheets = []
xl = pd.ExcelFile('data.xls')
for sn in xl.sheet_names:
    if 'Detail_67_' in sn:
        sheets.append(sn)
df = []
#looping through the list of sheets and appending the data to df list
for i in sheets:
    df.append(pd.read_excel('data.xls', sheet_name = i))
#concating the data list into data frame
df_final = pd.concat(df)
#writing the data frame to the csv file
df_final.to_csv('detail.csv')
print("Success! detail.csv created.")

######################################################################################################################

#Task 1.2
sheets = []
xl = pd.ExcelFile('data.xls')
for sn in xl.sheet_names:
    if 'DetailVol_67_' in sn:
        sheets.append(sn)
df = []
#looping through the list of sheets and appending the data to df list
for i in sheets:
    df.append(pd.read_excel('data.xls', sheet_name = i))
#concating the data list into data frame
df_final = pd.concat(df)
#writing the data frame to the csv file
df_final.to_csv('detailVol.csv')
print("Success! detailVol.csv created.")

######################################################################################################################

#Task 1.3
sheet1 = []
xl1 = pd.ExcelFile('data.xls')
for sn in xl1.sheet_names:
    if 'DetailTemp_67_' in sn:
        sheet1.append(sn)

sheet2 = []
xl2 = pd.ExcelFile('data_1.xls')
for sn in xl2.sheet_names:
    if 'DetailTemp_67_' in sn:
        sheet2.append(sn)
df = []
#looping through the list of sheets and appending the data to df list
for i in sheet1:
    df.append(pd.read_excel('data.xls', sheet_name = i))
for i in sheet2:
    df.append(pd.read_excel('data_1.xls', sheet_name = i))
    
#concating the data list into data frame
df_final = pd.concat(df)
#writing the data frame to the csv file
df_final.to_csv('detailTemp.csv')
print("Success! detailTemp.csv created.")

######################################################################################################################