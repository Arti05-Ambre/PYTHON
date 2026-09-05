import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram,linkage
data={
    "Product":["laptop","Mobile","Tablet","Headphones", 
              "Smartwatch","Camera","keyboard","Monitor"],
    "Price":[60000,25000,30000,3000,8000,45000,2000,15000],
    "Rating":[4.5,4.3,4.2,4.1,4.0,4.4,4.2,4.3],
    "Sales":[120,300,200,500,350,100,450,250] 
} 
df=pd.DataFrame(data) 
print("Product Dataset:")
print(df) 
X=df[["Price","Rating","Sales"]]
linked=linkage(X, method="ward")
plt.figure(figsize=(10,6))
dendrogram(
    linked,
    labels=df["Product"].values,
    leaf_rotation=45
)
plt.title("Dendrogram of similar Products")
plt.xlabel("Products")
plt.ylabel("Distance")
plt.show()
