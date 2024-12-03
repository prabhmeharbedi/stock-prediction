from textblob import TextBlob
import pandas as pd
import os

# Step 1: Function to calculate sentiment
def get_sentiment(text):
    if isinstance(text, float):  # Handle non-string inputs
        text = ""  # Replace with an empty string
    analysis = TextBlob(text)
    return analysis.sentiment.polarity  # Returns sentiment polarity (-1 to 1)

# Step 2: Main function to analyze sentiment
def analyze_sentiment(input_file, output_file):
    print(f"Loading cleaned data from {input_file}...")
    data = pd.read_csv(input_file)

    # Ensure no NaN values in Cleaned_Text column
    data['Cleaned_Text'] = data['Cleaned_Text'].fillna('')

    # Debugging: Check data types and missing values
    print("Preview of Cleaned_Text column:")
    print(data['Cleaned_Text'].head())
    print("Data types in Cleaned_Text column:")
    print(data['Cleaned_Text'].apply(type).value_counts())

    print("Performing sentiment analysis...")
    data['Sentiment'] = data['Cleaned_Text'].apply(get_sentiment)

    # Categorize sentiment
    data['Sentiment_Category'] = data['Sentiment'].apply(
        lambda x: 'Positive' if x > 0 else 'Negative' if x < 0 else 'Neutral'
    )

    print(f"Saving sentiment data to {output_file}...")
    data.to_csv(output_file, index=False)
    print("Sentiment analysis complete.")

# Step 3: Define paths and run
if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    cleaned_data_path = os.path.join(script_dir, "../data/cleaned_combined_posts.csv")
    sentiment_data_path = os.path.join(script_dir, "../data/sentiment_combined_posts.csv")
    analyze_sentiment(cleaned_data_path, sentiment_data_path)
