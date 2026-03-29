
# ----------------------  PROJECT 1 BUILDING CALCULATOR BY PYTHON  ---------------------
try:
    select1 = int(input("Enter a valid integer 1 for calculation: "))
    select2 = int(input("Enter a valid integer 2 for calculation: "))
    bodmos = input("Select a valid operation (+, -, *, /): ")

    if bodmos == '+':
        print("Result of addition:", select1 + select2)

    elif bodmos == '-':
        print("Result of subtraction:", select1 - select2)

    elif bodmos == '*':
        print("Result of multiplication:", select1 * select2)

    elif bodmos == '/':
        if select2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            print("Result of division:", select1 / select2)

    else:
        print("Invalid operation selected. Choose only +, -, *, /.")

except ValueError:
    print("Error: Please enter valid integer values.")


# ----------------------  PROJECT 2 BUILDING MILLIONAIRE GAME  -----------------------------
questions = [
    ["Who is Shah Rukh Khan?", "WWE wrestler", "Actor", "Scientist", "Plumber", 2],
    ["Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Venus", 2],
    ["What is the capital of France?", "Berlin", "Madrid", "Paris", "Rome", 3],
    ["Who wrote 'Harry Potter'?", "J.K. Rowling", "William Shakespeare", "Charles Dickens", "Mark Twain", 1],
    ["Which gas do humans breathe in to survive?", "Oxygen", "Carbon Dioxide", "Nitrogen", "Helium", 1],
    ["Who is known as the Father of Computers?", "Albert Einstein", "Charles Babbage", "Isaac Newton", "Nikola Tesla", 2],
    ["Which is the largest ocean in the world?", "Atlantic Ocean", "Pacific Ocean", "Indian Ocean", "Arctic Ocean", 2],
    ["Which country invented pizza?", "France", "Germany", "Italy", "Spain", 3],
    ["What is H2O commonly known as?", "Salt", "Water", "Oxygen", "Hydrogen", 2],
    ["Which is the fastest land animal?", "Lion", "Cheetah", "Horse", "Tiger", 2]
]

prize = [100000,200000,300000,400000,500000,600000,700000,800000,900000,1000000]

for i in questions:
# Basic printing             -- using comma,                                                     OR
    print("Question: ",i[0])
    print("Option a.", i[1])
    print("Option b.", i[2])
    print("Option c.", i[3])
    print("Option d.", i[4])
    print() 

# # # Using Using f-string (dot version) for question numbering             -- using dot.             OR
# #     print("Question: ",i[0])
# #     print(f"Option a. {i[1]}")
# #     print(f"Option b. {i[2]}")
# #     print(f"Option c. {i[3]}")
# #     print(f"Option d. {i[4]}")
# #     print()

# # # Using enumerate() (using dot)                              -- For question numbering with index
# # for index, i in enumerate(questions, start=1):
# #     print(f"Q{index}: {i[0]}")
# #     print(f"Option a. {i[1]}")
# #     print(f"Option b. {i[2]}")
# #     print(f"Option c. {i[3]}")
# #     print(f"Option d. {i[4]}")
# #     print()


    # check wheather the answer is correct or not:
    a = int(input("Enter your answer. 1 for a, 2 for b, 3 for c, 4 for d: \n"))
    if(i[5] == a):
        print("Correct answer.....Hurray")
    else:
        print(f"Incorrect, the correct answer was {i[5]}")
        print("Better luck next time!")
        break


# ---------------------------  PROJECT 3 PDF MERGER  ---------------------------------
# Install the Library
# Run this command in your terminal or command prompt: 
pip install PyPDF2
from PyPDF2 import PdfMerger

# Create a PdfMerger object
merger = PdfMerger()

# List of PDF files to merge (in order)
pdf_files = ["file1.pdf", "file2.pdf", "file3.pdf"]

# Append all PDFs
for pdf in pdf_files:
    merger.append(pdf)

# Save the merged PDF
merger.write("merged_output.pdf")
merger.close()
print("✅ PDFs merged successfully!")


# -----------------------------  PROJECT 4 DRINK WATER REMINDER  ----------------------------------
import time
import datetime

while True:
    # Get the current time
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    
    # Display reminder
    print(f"[{current_time}] 💧 Reminder: Drink Water!")
    
    # Wait for 1 hour (3600 seconds)
    time.sleep(10)
# OR
# Install plyer,Run this command in your terminal:
pip install plyer
import time
from plyer import notification

while True:
    notification.notify(
        title="💧 Water Reminder",
        message="Time to drink water and stay hydrated!",
        timeout=10  # Notification stays for 10 seconds
    )
    # Wait for 1 hour before showing next reminder
    time.sleep(10)  


# ------------- PROJECT 5 BUILD NEWS API ---------------      {Enter_your_own_api_key [Go to NEWSAPI website]}
import requests        # if not intall then use --> pip install requests

# Step 1: Enter your API key from newsapi.org
API_KEY = "your_api_key_here"  
BASE_URL = "https://newsapi.org/v2/top-headlines"

# Step 2: Set your parameters (country = "in" for India)
params = {
    'country': 'in',
    'apiKey': API_KEY,
    'pageSize': 5  # Get top 5 headlines
}

# Step 3: Make the request
response = requests.get(BASE_URL, params=params)

# Step 4: Parse and display the news
if response.status_code == 200:
    data = response.json()
    articles = data.get('articles')

    if articles:
        print("\n📰 Top Headlines:\n")
        for idx, article in enumerate(articles, 1):
            print(f"{idx}. {article['title']}")
            print(f"   ➤ {article['description']}")
            print(f"   🔗 {article['url']}\n")
    else:
        print("No articles found.")
else:
    print("Error:", response.status_code)

# OR 

import requests

# query = "artificial intelligence"      # OR
query = input("What type of news are you interested in today")
api_key = "your_api_key_here"   # Enter_your_own_api_key [Go to NEWSAPI website]

URL = f"https://newsapi.org/v2/everything?q={query}&from=2025-07-07&sortBy=publishedAt&apiKey={api_key}"

r = requests.get(URL)

data = r.json()

# Check if the request was successful
if r.status_code == 200:
    articles = data["articles"]
    for i in articles:
        print(i["title"])
        print(i["url"])
        print("-" * 60)
else:
    print("Error:", r.status_code)
    print("Details:", r.text)


# -------------------------   PROJECT 6 AI CHAT BOT ----------------------                --  [OPERN AI]
import openai        # if not intall then use --> pip install openai (openai is python package)

# Replace with your actual OpenAI API key
openai.api_key = "your_api_key_here" 

# To store the conversation history
messages = []

def get_completion(user_message):
    # Append user message to message history
    messages.append({"role": "user", "content": user_message})

    # Send the conversation to the model
    response = openai.ChatCompletion.create(
        model="gpt-4o",  # Use "gpt-3.5-turbo" if you're not on GPT-4o
        messages=messages
    )

    # Extract assistant's reply
    assistant_message = response['choices'][0]['message']['content']
    messages.append({"role": "assistant", "content": assistant_message})

    # Print the assistant's reply
    print("Jarvis:", assistant_message)

# Main function
if __name__ == "__main__":
    print("Hi, I am Jarvis. How may I help you?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Jarvis: Goodbye!")
            break
        get_completion(user_input)

