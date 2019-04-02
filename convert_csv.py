import pandas as pd
import numpy as np

# Read csv / tab-delimited in this example
df = pd.read_csv('subscribed_members_export_ef3462e259.csv',usecols=["Email Address", "First Name", "Last Name"])

print("---Asal----\n")
print(df)

# Reorder columns
df = df[["First Name", "Last Name", "Email Address"]]
print("---Setelah diurutkan----\n")
df = df.replace(np.nan, 'no name', regex=True)
print(df)

# Write csv / tab-delimited
df.to_csv('hasil.csv', sep=',',index=False,header=True)