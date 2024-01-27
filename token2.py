import string
import random
import requests
import os
import tkinter as tk
import discord
import threading

TOKENS_TO_GENERATE = 10  # Number of tokens to generate and check

# Function to generate a random Discord token
def generate_token():
    chars = string.ascii_letters + string.digits + '.' * 2
    token = ''.join(random.choice(chars) for _ in range(59))
    return token

# Function to check if a token is valid
def check_token(token):
    intents = discord.Intents.default()
    bot = discord.Client(intents=intents)
    try:
        bot.run(token)
        return True
    except discord.errors.LoginFailure:
        return False

# Function to save valid tokens to a file
def save_token(token):
    try:
        with open('valid_tokens.txt', 'a') as f:
            f.write(token + '\n')
    except:
        print('Error saving token to file')

# Main function to generate and check tokens
def generate_and_check_tokens():
    for _ in range(TOKENS_TO_GENERATE):
        token = generate_token()
        log_text.insert(tk.END, f"Checking token: {token}\n")
        valid = check_token(token)
        if valid:
            save_token(token)
            log_text.insert(tk.END, f"Valid token found: {token}\n")
        else:
            log_text.insert(tk.END, f"Invalid token: {token}\n")

# Function to handle button click event
def on_generate_button_click():
    threading.Thread(target=generate_and_check_tokens).start()

# Create the main window
window = tk.Tk()
window.title("Token Generator")
window.geometry("400x300")

# Create text box for logs
log_text = tk.Text(window, height=15, width=40)
log_text.pack(pady=10)

# Create button to generate and check tokens
generate_button = tk.Button(window, text="Generate Tokens", command=on_generate_button_click)
generate_button.pack()

# Run the main event loop
window.mainloop()