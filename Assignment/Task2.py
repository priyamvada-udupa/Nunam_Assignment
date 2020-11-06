#Task 2
import pandas as pd
#parsing the Absolute time column to datetime format
df = pd.read_csv('detail.csv', parse_dates = ["Absolute Time"], index_col = "Absolute Time")
#Applying the downsampling function
df = df.resample('T').mean()
#writing the new reduced data frame to new csv file
df.to_csv('detailDownsampled.csv')
print("Success! detailDownsampled.csv file created.")

######################################################################################################################

#parsing the Realtime column to datetime format
df = pd.read_csv('detailVol.csv', parse_dates = ["Realtime"], index_col = "Realtime")
#Applying the downsampling function
df = df.resample('T').mean()
#writing the new reduced data frame to new csv file
df.to_csv('detailVolDownsampled.csv')
print("Success! detailVol.csv file created.")

######################################################################################################################

#parsing the Realtime column to datetime format
df = pd.read_csv('detailTemp.csv', parse_dates = ["Realtime"], index_col = "Realtime")
#Applying the downsampling function
df = df.resample('T').mean()
#writing the new reduced data frame to new csv file
df.to_csv('detailTempDownsampled.csv')
print("Success! detailTempDownsampled.csv created.")

######################################################################################################################