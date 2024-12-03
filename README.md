
# Stock Movement Prediction Based on Social Media Sentiment

## Project Overview
This project predicts stock movements based on sentiment analysis of social media posts. 
The pipeline involves data scraping, text preprocessing, sentiment analysis, feature engineering, 
and machine learning model training.

## Features
1. Scrapes data from Reddit subreddits related to stock discussions.
2. Cleans and preprocesses the data to remove noise and prepare for analysis.
3. Performs sentiment analysis on the text data to identify polarity.
4. Generates features and labels for machine learning models.
5. Trains Logistic Regression and Random Forest models to predict stock movements.

## Installation
### Prerequisites
- Python 3.8 or higher

### Steps
1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd stock-movement-prediction
   ```
3. Install dependencies using the provided `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the following scripts in order:

1. **Data Scraping**:
   ```bash
   python scripts/reddit_scraper.py
   ```

2. **Data Preprocessing**:
   ```bash
   python scripts/preprocessing.py
   ```

3. **Sentiment Analysis**:
   ```bash
   python scripts/sentiment_analysis.py
   ```

4. **Feature Engineering**:
   ```bash
   python scripts/feature_engineering.py
   ```

5. **Model Training**:
   ```bash
   python scripts/model_training.py
   ```

## Output
- **Data Outputs**:
  - `reddit_combined_posts.csv`: Raw scraped data.
  - `cleaned_combined_posts.csv`: Preprocessed data.
  - `sentiment_combined_posts.csv`: Data with sentiment analysis results.
  - `features_combined_posts.csv`: Final dataset with features and labels.

- **Trained Models**:
  - `logistic_regression_model.pkl`
  - `random_forest_model.pkl`

## Results
The project evaluates the performance of Logistic Regression and Random Forest models:
- **Metrics**: Accuracy, Precision, Recall, and F1-score.
- Random Forest generally performs similar to Logistic Regression in this dataset.

## Future Enhancements
- Include data from other social media platforms like Twitter or Telegram.
- Experiment with advanced NLP models like BERT or GPT for sentiment analysis.
- Perform real-time stock movement prediction.

## License
This project is licensed under the MIT License.