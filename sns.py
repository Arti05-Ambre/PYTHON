    import seaborn as sns  
import matplotlib.pyplot as plt
iris = sns.load_dataset("iris")
features = ["sepal_length","sepal_width","petal_length","petal_width"]
for feature in features:
    plt.figure(figsize=(7,5))
    sns.boxplot(x="species",y=feature,data=iris)
    plt.title("BOX Plot of" +feature)
    plt.xlabel("Species")
    plt.ylabel(feature)
    plt.show()
    
