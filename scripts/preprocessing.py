import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import os

# Step 1: Download required NLTK data
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize stopwords and lemmatizer
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# Step 2: Function to preprocess text
def preprocess_text(text):
    text = re.sub(r'http\S+', '', text)  # Remove URLs
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove non-alphabetic characters
    words = text.lower().split()
    words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    return ' '.join(words)

# Step 3: Main function to clean data
def clean_data(input_file, output_file):
    print(f"Loading data from {input_file}...")
    data = pd.read_csv(input_file)
    data['Text'] = data['Text'].fillna('')  # Replace NaN in 'Text' with empty strings
    print("Cleaning text data...")
    data['Cleaned_Text'] = data['Text'].apply(preprocess_text)
    print(f"Saving cleaned data to {output_file}...")
    data.to_csv(output_file, index=False)
    print("Data cleaning complete.")

# Step 4: Define paths and run
if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    raw_data_path = os.path.join(script_dir, "../data/reddit_combined_posts.csv")
    cleaned_data_path = os.path.join(script_dir, "../data/cleaned_combined_posts.csv")
    clean_data(raw_data_path, cleaned_data_path)
