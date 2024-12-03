import praw
import pandas as pd
import os

# Initialize Reddit API
reddit = praw.Reddit(
    client_id="1ypDC1DTqB8Zhrpgn1JndQ",
    client_secret="uz2mDMKOF03zeop4YxE65nMZrR6JCw",
    user_agent="Stock_Scraper/1.0 by Express_Choice_7873"
)

# Step 2: Function to Scrape Subreddit Posts
def scrape_subreddit(subreddits, num_posts_per_subreddit=1000):
    all_posts = []
    for subreddit_name in subreddits:
        print(f"Scraping subreddit: {subreddit_name}")
        subreddit = reddit.subreddit(subreddit_name)
        for post in subreddit.hot(limit=num_posts_per_subreddit):
            all_posts.append({
                "Subreddit": subreddit_name,
                "Title": post.title,
                "Text": post.selftext,
                "Upvotes": post.score,
                "Comments": post.num_comments,
                "URL": post.url
            })
    return pd.DataFrame(all_posts)

# Step 3: Main Function
if __name__ == "__main__":
    # Define subreddits to scrape
    subreddits = ["stocks", "investing", "wallstreetbets", "StockMarket"]

    # Number of posts to scrape per subreddit
    num_posts = 1000

    print(f"Scraping {num_posts} posts per subreddit...")

    # Scrape data
    data = scrape_subreddit(subreddits, num_posts_per_subreddit=num_posts)

    # Define absolute path for the data directory
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Get script directory
    data_dir = os.path.join(script_dir, "../data")  # Construct absolute path for 'data' directory

    # Ensure 'data' directory exists
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # Save data to CSV
    output_path = os.path.join(data_dir, "reddit_combined_posts.csv")  # Construct output file path
    data.to_csv(output_path, index=False)  # Save DataFrame to CSV
    print(f"Data saved to {output_path}")