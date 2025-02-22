import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def train_model(df):
   
    X = df.drop(columns=['Churn'])
    y = df['Churn']


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

   
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)


    y_pred = model.predict(X_test)

  
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
    print("Classification Report:\n", classification_report(y_test, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))


    joblib.dump(model, "churn_model.pkl")

if __name__ == "__main__":
    df = pd.read_csv("processed_churn.csv")  
    train_model(df)
