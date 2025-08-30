
import pandas as pd
df=pd.read_csv("climate_change_dataset_unclean.csv")


print(df.info())
print(df.isnull().sum())


# Change datatype of year float to Datetime 

df["Year"] = df["Year"].astype("Int64")
df["Year"] = pd.to_datetime(df["Year"],format="%Y")
df["Year"]=df["Year"].dt.year

# Sort the Data by year 


df_sorted = df.sort_values(by="Year", ascending=True,inplace=True)


# Removing NAN value




c=df.groupby("Country")["CO2 Emissions (Tons/Capita)"].transform("mean")
df["CO2 Emissions (Tons/Capita)"]=df["CO2 Emissions (Tons/Capita)"].fillna(c) 


d=df.groupby("Country")["Sea Level Rise (mm)"].transform("mean")
df["Sea Level Rise (mm)"]=df["Sea Level Rise (mm)"].fillna(d)



e=df.groupby("Country")["Rainfall (mm)"].transform("mean")
df["Rainfall (mm)"]=df["Rainfall (mm)"].fillna(e)


f=df.groupby("Country")["Population"].transform("mean")
df["Population"]=df["Population"].fillna(f)



# Now the data is cleaned . So we can start some analysis





print(df.info())
print(df.isnull().sum())




print(df_sorted)
df.to_csv("climate_change_dataset_unclean.csv", index=False)