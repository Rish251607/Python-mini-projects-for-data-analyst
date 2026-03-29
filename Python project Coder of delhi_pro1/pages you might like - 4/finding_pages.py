"""
Finding "Pages You Might Like"
We've officially reached the final milestone of our first data science project at CodeBook – The Social Media for Coders. After cleaning messy data and building features like People You May Know, it's time to launch our last feature: Pages You Might Like.

Why This Matters
In real-world social networks, content discovery keeps users engaged. This feature simulates that experience using nothing but pure Python, showing how even simple logic can power impactful insights. So now the situation is that your manager is impressed with your 'People You May Know' feature and now assigns you a new challenge: Recommend pages that users might like!

On social media platforms, users interact with pages by liking, following, or engaging with posts. The goal is to analyze these interactions and suggest relevant pages based on user behavior.

Task 1: Understanding the Recommendation Logic
How 'Pages You Might Like' Works:
Users engage with pages (like, comment, share, etc.).
If two users have interacted with similar pages, they are likely to have common interests.
For the sake of this implementation, we consider liking a page as an interaction
Pages followed by similar users should be recommended.
Example:

Amit (ID: 1) likes Python Hub (Page ID: 101) and AI World (Page ID: 102).
Priya (ID: 2) likes AI World (Page ID: 102) and Data Science Daily (Page ID: 103).
Since Amit and Priya both like AI World (102), we suggest Data Science Daily (103) to Amit and Python Hub (101) to Priya.
What we are using here is called collaborative filtering:

"If two people like the same thing, maybe they’ll like other things each one likes too."

This is a basic form of a real-world recommendation engine, and our task is to implement it in pure Python. Let's Go!

Task 2: Implement the Algorithm
We'll create a function that:

Maps users to pages they have interacted with.
Identifies pages liked by users with similar interests.
Ranks recommendations based on common interactions.
"""

import json

# Function to load JSON data from a file
def load_data(filename):
    with open(filename, "r") as file:
        return json.load(file)

# Function to find pages a user might like based on common interests
def find_pages_you_might_like(user_id, data):
    # Dictionary to store user interactions with pages
    user_pages = {}
    for user in data["users"]:
        user_pages[user["id"]] = set(user["liked_pages"])
    
    # If the user is not found, return an empty list
    if user_id not in user_pages:
        return []
    
    user_liked_pages = user_pages[user_id]
    page_suggestions = {}
    
    for other_user, pages in user_pages.items():
        if other_user != user_id:
            shared_pages = user_liked_pages.intersection(pages)
            for page in pages:
                if page not in user_liked_pages:
                    page_suggestions[page] = page_suggestions.get(page, 0) + len(shared_pages)
    
    # Sort recommended pages based on the number of shared interactions
    sorted_pages = sorted(page_suggestions.items(), key=lambda x: x[1], reverse=True)
    return [page_id for page_id, _ in sorted_pages]

# Load data
data = load_data("data.json")
user_id = 1  # Example: Finding recommendations for Amit
page_recommendations = find_pages_you_might_like(user_id, data)
print(f"Pages You Might Like for User {user_id}: {page_recommendations}")