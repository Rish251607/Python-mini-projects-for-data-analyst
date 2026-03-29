import json

def load_data(filename):
    with open(filename, "r") as file:
        return json.load(file)

def find_people_you_may_know(user_id, data):
    # Build dictionary: user_id -> set of their friends
    user_friends = {user["id"]: set(user["friends"]) for user in data["users"]}

    if user_id not in user_friends:
        return []
    
    direct_friends = user_friends[user_id]
    suggestions = {}

    # Loop through each direct friend
    for friend_id in direct_friends:
        if friend_id in user_friends:  # Avoid KeyError
            # Check each friend-of-a-friend
            for mutual in user_friends[friend_id]:
                if mutual != user_id and mutual not in direct_friends:
                    # Count mutual friends for each suggestion
                    suggestions[mutual] = suggestions.get(mutual, 0) + 1
    
    # Sort by mutual friend count (descending)
    sorted_suggestions = sorted(suggestions.items(), key=lambda x: x[1], reverse=True)
    
    # Return only the user IDs in sorted order
    return [uid for uid, _ in sorted_suggestions]

# Load data and test
data = load_data("data.json")
user_id = 1
recommendations = find_people_you_may_know(user_id, data)
print(f"People You May Know for User {user_id}: {recommendations}")
