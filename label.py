import pandas as pd 
from sklearn.preprocessing import LabelEncoder        
categorical/text values into numbers.) 
df = pd.read_csv("customer_data.csv") 
print("Original Data:") 
print(df) 
# A) Label Encoding 
le = LabelEncoder()                                      
df["Gender"] = le.fit_transform(df["Gender"]) 
print("\n--- Label Encoding ---") 
print(df) 
# B) One-Hot Encoding 
df_onehot = pd.get_dummies(df, columns=["City"]) 
print("\n--- One-Hot Encoding ---") 
print(df_onehot) 
//   Female → 0 
Male   → 1                 
if customer is in pune then true otherwise false   
(LabelEncoder converts              
// (Create LabelEncoder object) 
Label Encoding = Text → Numbers 
One-Hot Encoding = Categories → Separate Columns
→ Separate Columns 
4. Write a Python program to create a DataFrame using sales_data.csv with the attributes 
Product_ID, Price, Quantity_Sold, Discount, and Revenue. Apply data transformation 
techniques on the DataFrame and display the transformed data. 
a) Min-Max Scaling  
b) Standardization 
c) Normalization 
import pandas as pd 
from sklearn.preprocessing import MinMaxScaler, StandardScaler, Normalizer 
df = pd.read_csv("sales_data.csv") 
print("Original Data:") 
print(df) 
data = df[["Price", "Quantity_Sold", "Discount", "Revenue"]] 
# A) Min-Max Scaling 
minmax = MinMaxScaler() 
minmax_data = minmax.fit_transform(data) 
print("\nA) Min-Max Scaling:") 
print(minmax_data) 
# B) Standardization 
standard = StandardScaler() 
standard_data = standard.fit_transform(data) 
print("\nB) Standardization:") 
print(standard_data) 
# C) Normalization 
normal = Normalizer() 
normal_data = normal.fit_transform(data)
normal_data = normal.fit_transform(data) 
print("\nC) Normalization:")
nC) Normalization:") 
print(normal_data)
