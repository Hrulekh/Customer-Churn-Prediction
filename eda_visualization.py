import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_data(df):
 
    plt.figure(figsize=(6, 4))
    sns.countplot(x='Churn', data=df)
    plt.title("Churn Distribution")
    plt.show()

   
    plt.figure(figsize=(12, 6))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Feature Correlation Heatmap")
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv("processed_churn.csv")  
    visualize_data(df)
