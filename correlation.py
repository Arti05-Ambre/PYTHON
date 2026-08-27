import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data={  
    
"Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun","Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
"Temperature":[22,24,28,32,35,30,27,27,28,29,25,22],
"Humidity": [55, 52, 48, 45, 50, 70, 80, 82, 75, 65, 58, 55],
"Rainfall": [5, 8, 10, 15, 30, 150, 250, 220, 180, 70, 20, 8],
"Wind Speed": [8, 9, 10, 12, 14, 16, 18, 17, 15, 11, 9, 8]
}
df=pd.DataFrame(data)
print("Weather Dataset:")
print(df)
correlation = df[["Temperature", "Humidity", "Rainfall", "Wind Speed"]].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(
    correlation,
    annot=True,    
    cmap="coolwarm",  
fmt=".2f" 
)
plt.title("Correlation Heat Map of Weather Parameters")
plt.show()

