import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report
import os
import joblib

# Step 1: Train and evaluate models
def train_model(input_file, save_dir):
    print(f"Loading feature data from {input_file}...")
    data = pd.read_csv(input_file)
    X = data[['Sentiment']]
    y = data['Stock_Movement']
    print("Splitting data into training and testing sets...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print("Training Logistic Regression model...")
    lr_model = LogisticRegression()
    lr_model.fit(X_train, y_train)
    print("Training Random Forest model...")
    rf_model = RandomForestClassifier()
    rf_model.fit(X_train, y_train)
    print("Evaluating models...")
    models = {"Logistic Regression": lr_model, "Random Forest": rf_model}
    for name, model in models.items():
        y_pred = model.predict(X_test)
        print(f"\n{name} Model Performance:")
        print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
        print(f"Precision: {precision_score(y_test, y_pred):.2f}")
        print(f"Recall: {recall_score(y_test, y_pred):.2f}")
        print("Classification Report:\n", classification_report(y_test, y_pred))
        model_path = os.path.join(save_dir, f"{name.replace(' ', '_').lower()}_model.pkl")
        print(f"Saving {name} model to {model_path}...")
        joblib.dump(model, model_path)

# Step 2: Define paths and run
if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    feature_data_path = os.path.join(script_dir, "../data/features_combined_posts.csv")
    model_save_dir = os.path.join(script_dir, "../models")
    if not os.path.exists(model_save_dir):
        os.makedirs(model_save_dir)
    train_model(feature_data_path, model_save_dir)
