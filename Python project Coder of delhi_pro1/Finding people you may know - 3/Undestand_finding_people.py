"""
Task 1: Understand the Logic
1 is friend with [2,3], 2 is friend of [4] (now we will implement this like as 1 ka dost 2 hai and 2 ka dost 4 hai so there is a good chance that 1 should know 4)

How 'People You May Know' Works:
If User A and User B are not friends but have mutual friends, we suggest User B to User A and vice versa.
More mutual friends = higher priority recommendation.
Example:

Amit (ID: 1) is friends with Priya (ID: 2) and Rahul (ID: 3).
Priya (ID: 2) is friends with Sara (ID: 4).
Amit is not directly friends with Sara, but they share Priya as a mutual friend.
Suggest Sara to Amit as "People You May Know".
But there are cases where we will have more than one "People You May Know". In those cases, greater the number of mutual friends, higher the probability that the user might know the person we are recommending.

Task 2: Implement the Algorithm
1. Find friends of user 1 (woh hai 2 and 3)
2. Find mutual friends (jaise 1 and 4 ka mutual friend hai 2)
3. We will give score (more score to them who have more chance to make friends (jaise 
                                  1 is friend of 2,3,5
5 ----- 4                         2 is friend of 1,4,6
|       |                         3 is friend of 1
|       |                         4 is friend of 2,5
|       |                         5 is friend of 1,4
1 ----- 2 ------- 6               6 is friend of 2
|                              
|                                 here,1 and 4 ke friend banne ka score 2 hai bcz there are 2 ways (1,5,4 and 1,2,4)
|                                 but there is score 1 for being friend with 6 as there is only one way i.e 1,2,6
3                                        

))

We'll create a function that:

Finds all friends of a given user.
Identifies mutual friends between non-friends.
Ranks recommendations by the number of mutual friends.
"""

import json

def load_data(filename):
    with open(filename, "r") as file:
        return json.load(file)

def find_people_you_may_know(user_id, data):
    user_friends = {}                                                 # -- Dictionary
    for i in data["users"]:
        user_friends[i["id"]] = set(i["friends"])
    # print(user_friends)                     # {1: {2, 3, 5}, 2: {1, 4, 6}, 3: {1}, 4: {2, 5}, 5: {1, 4}, 6: {2}}


    if user_id not in user_friends:                      # IMP
        return []
    
    direct_friends = user_friends[user_id]
    # print(direct_friends)                              # {2, 3, 5} 

    suggestions = {}                                                 # -- Dictionary
    
    for i in direct_friends:                   # loop will run for: i = 2 → i = 3 → i = 5
        if i in user_friends:                  # avoid KeyError
            # For all friends of friend
            for mutual in user_friends[i]:
                # print(mutual)                                                   # 1 4 6 1 1 1 4
                # If mutual id is not the same user and not already a direct friend of user
                if mutual != user_id and mutual not in direct_friends:                        # IMP
                    # Count mutual friends
                    suggestions[mutual] = suggestions.get(mutual, 0) + 1
                    # print(suggestions)                                            # {4: 2, 6: 1}

                    """
                    mutual != user_id → Don’t suggest the same person (e.g., don’t suggest Amit to Amit).

                    mutual not in direct_friends → Don’t suggest people who are already direct friends.

                    This ensures we only suggest “friends of friends” who are not already connected.
                    For i = 2 
                    user_friends[2] = {1, 4, 6}
                    mutual = 1 → fails mutual != user_id → ❌ skip
                    mutual = 4 → passes both checks ✅ → suggestions = {4: 1}
                    mutual = 6 → passes both checks ✅ → suggestions = {4: 1, 6: 1}

                    For i = 3
                    user_friends[3] = {1}
                    mutual = 1 → fails mutual != user_id → ❌ skip
                    (No new suggestions)

                    For i = 5
                    user_friends[5] = {1, 4}
                    mutual = 1 → fails mutual != user_id → ❌ skip
                    mutual = 4 → passes both checks ✅

                    
                    → already in suggestions → increment count → suggestions = {4: 2, 6: 1}

                    """
    
    sorted_suggestions = sorted(suggestions.items(), key=lambda x: x[1], reverse=True)
    # print(sorted_suggestions)                                    # [(4, 2), (6, 1)]
    """
    1. suggestions.items() --- This turns the dictionary into a list of tuples where:
                        --- The first element of each tuple is the suggested person’s ID.
                        --- The second element is the count of mutual friends. Here  [(4, 2), (6, 1)]

    2. sorted_suggestions = sorted(
        suggestions.items(),       # [(4, 2), (6, 1)]
        key=lambda x: x[1],        # Sort by second element (mutual count)
        reverse=True               # Highest count first
        )
        lambda x: x[1] → tells Python:
        “When sorting each tuple x, look at x[1] (the mutual friend count) instead of x[0] (user ID).”
        reverse=True → sort in descending order, so more mutual friends appear first.

    3. sorted_suggestions = [(4, 2), (6, 1)]  OR [(user_id, mutual_friend_count), ...]         [IMP]
    """
    return [uid for uid, _ in sorted_suggestions]
"""
return [uid for uid, _ in sorted_suggestions]
This is list comprehension of -.
uids = []
    for uid, _ in sorted_suggestions: 
        uids.append(uid)
    return uids
uid → the first element of each tuple.
_ → a throwaway variable for the second element (mutual count) because we don’t need it now.
From "[(4, 2), (6, 1)]" we get "[4, 6]"

When Python loops through these tuples:
uid gets the first element of the tuple → here it’s the user ID (e.g., 4 or 6).
_ gets the second element (the mutual friend count), but _ is just a throwaway variable—it means "I don't care about this value".
So for (4, 2):
uid = 4 → user ID of the suggestion
_ = 2 → number of mutual friends (ignored in this loop)

For (6, 1):
uid = 6
_ = 1 → number of mutual friends (ignored in this loop)

So, 'return [uid for uid, _ in sorted_suggestions]' ------->  Output: [4, 6]

"""

# Load data
data = load_data("data.json")
user_id = 1                                                            # Example: Finding suggestions for Amit
recommendations = find_people_you_may_know(user_id, data)
print(f"People You May Know for User {user_id}: {recommendations}")
