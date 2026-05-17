import os
import praw

def main():
    """
    A minima read-only script to fetch public sub reddit metadata 
    for personal offline text parsing and trend analysis.
    
    This script performs only GET operations and handles no user authentication
    beyond the standard app credentials.
    """
    # Initialize the Reddit instance
    # Credentials can be loaded securely via environment variables or a praw.ini file
    reddit = praw.Reddit(
        client_id=os.environ.get("REDDIT_CLIENT_ID", "YOUR_CLIENT_ID"),
        client_secret=os.environ.get("REDDIT_CLIENT_SECRET", "YOUR_CLIENT_SECRET"),
        user_agent=os.environ.get("REDDIT_USER_AGENT", "script:local_data_pipeline:v1.0 (by /u/YOUR_REDDIT_USERNAME)")
    )

    # Example read-only target subreddits for technology trend evaluation
    target_subreddits = ["Python", "selfhosted", "sysadmin"]
    
    print("Initiating read-only public data ingest pipeline...")
    
    for sub_name in target_subreddits:
        print(f"\n=== Fetching Public Content Listing: r/{sub_name} ===")
        try:
            subreddit = reddit.subreddit(sub_name)
            
            # Retrieve the top 5 hot submissions (Strictly a GET operation)
            for submission in subreddit.hot(limit=5):
                print(f"ID: {submission.id}")
                print(f"Title: {submission.title}")
                print(f"Score: {submission.score} | Comment Count: {submission.num_comments}")
                print(f"Created (UTC): {submission.created_utc}")
                print("-" * 40)
                
        except Exception as e:
            print(f"Error accessing public data for r/{sub_name}: {e}")

    print("\nData ingest simulation complete.")

if __name__ == "__main__":
    main()
