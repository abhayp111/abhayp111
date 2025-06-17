# chatbot/main.py
from chatbot import chat

while True:
    q = input("\nYou: ")
    if q.lower() in ["exit", "quit"]:
        break
    print("Bot:", chat(q))
