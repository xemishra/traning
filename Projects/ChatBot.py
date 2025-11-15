import tkinter as tk
from tkinter import scrolledtext
import random

# knowledge base
responses = {
    "hello": ["Hi there!", "Hello! How can i help you?", "Hey! What's up?"],
    "how are you": ["I'm doing great!", "Feeling like a bot should - awesome!", "All good, Thanks for asking!"],
    "your name": ["My name is PyBot", "You can me PyBot!", "I'm PyBot, Your assistant!"],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a nice day!"]
}

# Function to get response from bot
def getResponse(userMessage):
    userMessage = userMessage.lower()
    for key in responses:
        if key in userMessage:
            return random.choice(responses[key])
    return "Sorry, I don't understand that!"

# function to send message!
def sendMessage():
    userMessage = entry.get()
    if userMessage.strip() == "":
        return
    chat_window.insert(tk.END, "You:" + userMessage + "\n", "User")
    entry.delete(0, tk.END)

    botMessage = getResponse(userMessage)
    chat_window.insert(tk.END, "Bot:" + botMessage + "\n", "bot")

# GUI Setup
root = tk.Tk()
root.title("PyBot - Chatbot")
root.geometry("450x550")

# Chat Window
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height = 20, font=("Arial", 12))
chat_window.pack(pady=10)
chat_window.tag_config("user", foreground="blue")
chat_window.tag_config("bot", foreground="green")

# entry field!
entry = tk.Entry(root, width=30, font=("Arial", 14))
entry.pack(pady=5, side=tk.LEFT, padx=5)

# Buttons
send_btn = tk.Button(root, text="Send", command=sendMessage, width=10, bg="lightblue")
send_btn.pack(pady=5, side=tk.LEFT)

# Run the APP!
root.mainloop()
