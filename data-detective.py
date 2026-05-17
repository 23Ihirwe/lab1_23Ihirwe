import csv
import sys
import os

def load_raw_data(filename):
    """
    Loads the CSV file into a list of dictionaries exactly as it is (messy).
    """
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
        
    raw_tweets = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            raw_tweets.append(row)
            
    return raw_tweets

def clean_data(tweets):
    """
    QUEST 1: Handle missing fields.
    No .get() or .strip() helper functions are used here.
    """
    cleaned_list = []
    bad_rows_fixed_or_removed = 0
    
    for tweet in tweets:
        # Raw check if Text key is missing or entirely blank string
        if "Text" not in tweet or tweet["Text"] == "":
            bad_rows_fixed_or_removed = bad_rows_fixed_or_removed + 1
            continue  # Ignore this tweet and move to the next row
            
        is_row_modified = False
        
        # Check and repair Retweets column
        if "Retweets" not in tweet or tweet["Retweets"] == "":
            tweet["Retweets"] = "0"
            is_row_modified = True
            
        # Check and repair Likes column
        if "Likes" not in tweet or tweet["Likes"] == "":
            tweet["Likes"] = "0"
            is_row_modified = True
            
        if is_row_modified == True:
            bad_rows_fixed_or_removed = bad_rows_fixed_or_removed + 1
            
        cleaned_list.append(tweet)
        
    print(f"Quest 1 Complete: Fixed or removed {bad_rows_fixed_or_removed} bad rows.")
    return cleaned_list

def find_viral_tweet(tweets):
    """
    QUEST 2: Loop through the list to find the tweet with the highest 'Likes'.
    Bans max() entirely. Uses basic linear comparison logic.
    """
    # Use len() to check size as requested in the criteria
    if len(tweets) == 0:
        print("No data available.")
        return
        
    # Start tracking from a baseline below zero
    highest_likes_found = -1
    viral_tweet_record = None
    
    for tweet in tweets:
        # Convert string to integer for a correct mathematical comparison
        current_row_likes = int(tweet["Likes"])
        
        if current_row_likes > highest_likes_found:
            highest_likes_found = current_row_likes
            viral_tweet_record = tweet
            
    if viral_tweet_record != None:
        print("\nQuest 2 Complete: The Viral Post Found!")
        print(f"Username: {viral_tweet_record['Username']}")
        print(f"Likes: {viral_tweet_record['Likes']}")
        print(f"Text: {viral_tweet_record['Text']}\n")

def custom_sort_by_likes(tweets):
    """
    QUEST 3: Implement Selection Sort to sort by 'Likes' descending.
    NO .sort() or sorted() allowed!
    """
    list_length = len(tweets)
    
    # Outer loop moves the boundary of the unsorted subarray
    for i in range(list_length):
        max_index = i
        
        # Inner loop finds the largest element in the remaining unsorted list
        for j in range(i + 1, list_length):
            likes_at_j = int(tweets[j]["Likes"])
            likes_at_max = int(tweets[max_index]["Likes"])
            
            # Look for values that are larger to sort from highest to lowest
            if likes_at_j > likes_at_max:
                max_index = j
                
        # Swap the found maximum element with the first element of the loop pass
        temporary_holder = tweets[i]
        tweets[i] = tweets[max_index]
        tweets[max_index] = temporary_holder
                
    print("Quest 3 Complete: Custom Selection Sort Finished.")
    print("--- Top 10 Most Liked Tweets ---")
    
    # Slice the list to get exactly the top 10 items
    top_10_tweets = tweets[:10]
    
    # Simple counting tracker to loop and print the ranking manually
    rank_counter = 1
    for tweet in top_10_tweets:
        print(f"{rank_counter}. User: {tweet['Username']} | Likes: {tweet['Likes']}")
        rank_counter = rank_counter + 1
    print()

def search_tweets(tweets, keyword):
    """
    QUEST 4: Search for a keyword and extract matching tweets into a new list.
    """
    matching_tweets = []
    
    for tweet in tweets:
        # Check if the search word exists inside the text string
        if keyword in tweet["Text"]:
            # List mastery: using .append() to build the new list
            matching_tweets.append(tweet)
            
    # Print the len() of this new list to tell the user how many matched
    print(f"Quest 4 Complete: Found {len(matching_tweets)} tweets matching '{keyword}'.")
    
    for tweet in matching_tweets:
        print(f"- [{tweet['Username']}]: {tweet['Text']}")

if __name__ == "__main__":
    # Load data using starter code logic
    dataset = load_raw_data("twitter_dataset.csv")
    print(f"Loaded {len(dataset)} raw tweets.\n")
    
    # Execute the Quests sequentially using our raw variables
    cleaned_dataset = clean_data(dataset)
    find_viral_tweet(cleaned_dataset)
    custom_sort_by_likes(cleaned_dataset)
    
    user_keyword = input("Enter a keyword to search for: ")
    search_tweets(cleaned_dataset, user_keyword)
