import pandas as pd
import numpy as np
import os

# Step 1: Define stock movement labels
def generate_labels(sentiment):
    return 1 if sentiment > 0 else 0

# Step 2: Main function for feature engineering
def feature_engineering(input_file, output_file):
    print(f"Loading sentiment data from {input_file}...")
    data = pd.read_csv(input_file)
    print("Extracting features...")
    features = data[['Sentiment']]
    print("Generating target labels...")
    data['Stock_Movement'] = data['Sentiment'].apply(generate_labels)
    print(f"Saving features and labels to {output_file}...")
    output_data = pd.concat([features, data['Stock_Movement']], axis=1)
    output_data.to_csv(output_file, index=False)
    print("Feature engineering complete.")

# Step 3: Define paths and run
if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    sentiment_data_path = os.path.join(script_dir, "../data/sentiment_combined_posts.csv")
    feature_data_path = os.path.join(script_dir, "../data/features_combined_posts.csv")
    feature_engineering(sentiment_data_path, feature_data_path)
