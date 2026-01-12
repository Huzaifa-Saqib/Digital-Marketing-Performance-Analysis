import pandas as pd
import numpy as np
df= pd.read_csv("marketing_campaign_messy_data.csv")

df=df.drop(columns=['Clicks'])
df=df.dropna()
df=df.replace("UNKNOWN" , np.nan).dropna()
df=df.replace("ERROR" , np.nan).dropna()
df=df.replace("INVALID" , np.nan).dropna()

df=df.rename(columns={
    'Clicks ' : 'Clicks' , 
    ' Campaign_ID ' : 'Campaign_ID'
    })

df = df.replace({
    '1': 'Yes',
    'TRUE': 'Yes',
    'Y': 'Yes',
    '0': 'No',
    'FALSE': 'No',
    'N': 'No'
})

df['Spend'] = df['Spend'].str.replace('-', '', regex=False)

df=df.replace('Email' , 'E-mail')
df=df.replace('Tik_Tok' , 'TikTok')
df=df.replace('Insta_gram' , 'Instagram')
df=df.replace('Facebok' , 'Facebook')
df=df.replace('Gogle' , 'Google Ads')
df=df.replace('E-' , 'EM')

df['End_Date'] = pd.to_datetime(df['End_Date'], format='mixed', dayfirst=True).dt.date
df['Start_Date'] = pd.to_datetime(df['Start_Date'], format='mixed', dayfirst=True).dt.date


print(df)

file_name = 'cleaned_marketing_campaign_data.xlsx'
df.to_excel(file_name, index=False , sheet_name='Data')

print("Successfully Saved!!")