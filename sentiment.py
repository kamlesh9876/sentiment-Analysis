import tkinter as tk
from tkinter import scrolledtext
from textblob import TextBlob

def analyze_sentiment(message):
    blob = TextBlob(message)
    sentiment = blob.sentiment.polarity

    if sentiment > 0:
        return 'positive'
    elif sentiment < 0:
        return 'negative'
    else:
        return 'neutral'

def send_message():
    user_message = entry.get()
    if user_message.strip() == '':
        return

    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, f'You: {user_message}\n')

    sentiment = analyze_sentiment(user_message)
    chat_log.insert(tk.END, f'Bot: Your message sentiment is {sentiment}\n\n')
    chat_log.config(state=tk.DISABLED)
    chat_log.yview(tk.END)

    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title('Sentiment Analysis Chatbot')
root.geometry('500x500')

# Create the chat log
chat_log = scrolledtext.ScrolledText(root, state='disabled', wrap='word', height=20)
chat_log.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create the entry box
entry_frame = tk.Frame(root)
entry_frame.pack(fill=tk.X, padx=10, pady=10)

entry = tk.Entry(entry_frame, width=80)
entry.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.X, expand=True)
entry.bind('<Return>', lambda event: send_message())

send_button = tk.Button(entry_frame, text='Send', command=send_message)
send_button.pack(side=tk.RIGHT, padx=10, pady=10)

# Start the main loop
root.mainloop()
