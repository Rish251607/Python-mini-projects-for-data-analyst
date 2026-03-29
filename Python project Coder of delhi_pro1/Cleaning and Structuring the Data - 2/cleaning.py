import json

def clean_data(data):
    # -----------Remove users with missing names
    # data["users"] = [user for user in data["users"] if user["name"].strip()]     # OR 
    filtered_users = []
    for i in data["users"]:
        if i["name"].strip():
            filtered_users.append(i)
    data["users"] = filtered_users
    
    #------------- Remove duplicate friends
    for i in data["users"]:
        i["friends"] = list(set(i["friends"]))
    
    # --------------Remove inactive users
    # data["users"] = [user for user in data["users"] if user["friends"] or user["liked_pages"]]  # OR
    filtered_users = []
    for i in data["users"]:
        if i["friends"] or i["liked_pages"]:
            filtered_users.append(i)
    data["users"] = filtered_users

    # --------------Remove duplicate pages
    unique_pages = {}
    for i in data["pages"]:
        unique_pages[i["id"]] = i     
        # means 101 = {"id": 101, "name": "Python Developers"}
        #       102 = {"id": 102, "name": "Data Science Enthusiasts"} ....
    data["pages"] = list(unique_pages.values())       # phir humnai dictionry ki values ki list bna di 
    # Note - yeh dono ({"id": 104, "name": "Web Dev Hub"},{"id": 104, "name": "Web Development"}) id mai sai last waali ko lega, but hum agar chahtai hai ki yeh pehli ko le to hum *SET* ka use karengai

    """
    # data["pages"] = list({page["id"]: page for page in data["pages"]}.values())   # OR
    seen = set() 
    unique_pages = []
    for page in data["pages"]:
        if page["id"] not in seen:
            seen.add(page["id"])
            unique_pages.append(page)
    data["pages"] = unique_pages
    """

    return data

# Load, clean, and save the cleaned data
with open("data.json","r") as file:
    raw_data = json.load(file)                # OR 
# raw_data = json.load(open("data.json"))

cleaned_data = clean_data(raw_data)

with open("cleaned_codebook_data.json", "w") as file:
    json.dump(cleaned_data, file, indent=4)             # OR
# json.dump(cleaned_data, open("cleaned_codebook_data.json", "w"), indent=4)

print("Data cleaned successfully!")



"""
Output
{
    "users": [
        {"id": 1, "name": "Amit", "friends": [2, 3], "liked_pages": [101]},
        {"id": 2, "name": "Priya", "friends": [1, 4], "liked_pages": [102]},
        {"id": 4, "name": "Sara", "friends": [2], "liked_pages": [104]}
    ],
    "pages": [
        {"id": 101, "name": "Python Developers"},
        {"id": 102, "name": "Data Science Enthusiasts"},
        {"id": 103, "name": "AI & ML Community"},
        {"id": 104, "name": "Web Development"}
    ]
}
"""


"""
import json

def clean_data(data):
    # Remove users with missing names
    filtered_users = []
    for i in data["users"]:
        if i["name"].strip():
            filtered_users.append(i)
    data["users"] = filtered_users
    
    # Remove duplicate friends
    for i in data["users"]:
        i["friends"] = list(set(i["friends"]))
    
    # Remove inactive users
    filtered_users = []
    for i in data["users"]:
        if i["friends"] or i["liked_pages"]:
            filtered_users.append(i)
    data["users"] = filtered_users

    # Remove duplicate pages
    unique_pages = {}
    for i in data["pages"]:
        unique_pages[i["id"]] = i
    data["pages"] = list(unique_pages.values())
    
    return data

# Load, clean, and save the cleaned data
with open("data.json", "r") as file:
    raw_data = json.load(file)

cleaned_data = clean_data(raw_data)

with open("cleaned_codebook_data.json", "w") as file:
    json.dump(cleaned_data, file, indent=4)

print("Data cleaned successfully!")
"""