import win32com.client
import pandas as pd
import re

SapGui = win32com.client.GetObject("SAPGUI").GetScriptingEngine  
session = SapGui.FindById("ses[0]") 

session.StartTransaction(Transaction="SE16")  
session.FindById('/app/con[0]/ses[0]/wnd[0]/usr/ctxtDATABROWSE-TABLENAME').text = "AGR_1251"
session.findById("wnd[0]").sendVKey(0)
session.FindById('/app/con[0]/ses[0]/wnd[0]/usr/ctxtI1-LOW').text = "*"
session.FindById('/app/con[0]/ses[0]/wnd[0]/usr/txtI3-LOW').text = "S_TCODE"
session.FindById('/app/con[0]/ses[0]/wnd[0]/usr/txtMAX_SEL').text = "200000"
session.findById("wnd[0]/tbar[1]/btn[8]").press()

session.findById("wnd[0]/tbar[1]/btn[45]").press()
session.findById("wnd[1]/usr/subSUBSCREEN_STEPLOOP:SAPLSPO5:0150/sub:SAPLSPO5:0150/radSPOPLI-SELFLAG[1,0]").select()
session.findById("wnd[1]/tbar[0]/btn[0]").press()
session.findById("wnd[1]/usr/ctxtDY_FILENAME").text ="final.txt"
session.findById("wnd[1]/tbar[0]/btn[11]").press()

df = pd.read_csv('/Users/th61a3/Desktop/Attachments/final.txt',delimiter='\t', encoding='cp1252')

#   Drop not neede columns
df.drop(df.columns[[0, 1,3, 4,5,6,7,10,11,12,13,14]], axis = 1, inplace = True)
df.fillna(0, inplace = True)

#df['LOW'].fillna(0, inplace = True)
#df['HIGH'].fillna(0, inplace = True)



df["AGR_NAME"] = df["AGR_NAME"].astype(str)
df["LOW"] = df["LOW"].astype(str)
df["HIGH"] = df["HIGH"].astype(str)

#   Write "Forbidden" to the columns in LOW and HIGH which are ... Forbidden
values_in_A = df[df['LOW'].str.contains('\*')]['AGR_NAME']
index_to_change = df[df['AGR_NAME'].isin(values_in_A)].index
df.loc[index_to_change, 'LOW'] = 'Forbidden'
df.loc[index_to_change, 'HIGH'] = 'Forbidden'

values_in_A = df[df['HIGH'].str.contains('\*')]['AGR_NAME']
index_to_change = df[df['AGR_NAME'].isin(values_in_A)].index
df.loc[index_to_change, 'LOW'] = 'Forbidden'
df.loc[index_to_change, 'HIGH'] = 'Forbidden'

mask = df['LOW'].str.match('^[A-Z].*[0-9]$') & df['HIGH'].str.match('^[A-Z].*[0-9]$')

df2=df[mask]

#Create an empty dataframe 
df3 = pd.DataFrame()

#Loop through DataFrame rows as (index, Series) pairs
for index, row in df2.iterrows():

 #Set diff as variable for the difference of the last digits from LOW and HIGH
 diff = int(row['HIGH'][-1]) - int(row['LOW'][-1])

 #Fill the dataframe with the rows multipled by their difference calues from before...
 df3 = df3.append([row]*(diff+1))

 #Create a column with the counted duplicates from AGR_NAME and LOW starting with 1
 df3['C'] = df3.groupby(['AGR_NAME','LOW']).cumcount()+1; df3

#Create a column with the counted duplicates from AGR_NAME and LOW starting with 1
df3['CC'] = df3['LOW'].str[3:]

#Change the format of column C from int to str
df3["C"] = df3["C"].astype(str)

#Create a map...this is surely possible with something smarter
chg = {
    '0': '-1', 
    '1': '0',
    '2':'1',
     '3':'2',
    '4': '3',
    '5': '4',
    '6': '5',
    '7': '6',
    '8': '7',
    '9': '8'
}

#Create a column with the mapped numbers
df3['CCC'] = df3['CC'].map(chg)

#Change the format of column CCC and C to int
df3['CCC'] = df3['CCC'].astype(int)

df3['C'] = df3['C'].astype(int)

#Create a column for the correct end number of column LOW
z = [ row.CCC + row.C for index, row in df3.iterrows() ]
df3['z'] = z

#Change the format of column C from int to str
df3["C"] = df3["C"].astype(str)

#Change the format of column z from int to str
df3["z"] = df3["z"].astype(str)

#Modify the values in LOW by cutting the last digit and adding the string from C
df3['LOW'] = df3['LOW'].str[:-1] + df3['z']

df3.drop(df3.columns[[3, 4,5,6]], axis = 1, inplace = True)

frames = [df, df3]

df = pd.concat(frames)

df.drop(df.columns[[2]], axis = 1, inplace = True)
df.drop_duplicates()

df.to_csv('/Users/th61a3/Desktop/Attachments/TBL_#_SE16_AGR_1251.csv', index=False, header=True)