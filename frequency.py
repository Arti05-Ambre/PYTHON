import pandas as pd 
b) Equal Frequency Binning
b) Equal Frequency Binning  
df = pd.read_csv("age_data.csv")
df = pd.read_csv("age_data.csv")    
print("Original Data:") 
print(df)  
# a) Equal Width Binning 
df["Equal_Width"] = pd.cut( 
df["Age"],  
bins=3, 
labels=["Young", "Adult", "Senior"]  
) 
print("\nEqual Width Binning:") 
print(df) 
# b) Equal Frequency Binning 
df["Equal_Frequency"] = pd.qcut( 
df["Age"], 
q=3, 
labels=["Young", "Adult", "Senior"] 
) 
print("\nEqual Frequency  Binning:") 
print(df)
